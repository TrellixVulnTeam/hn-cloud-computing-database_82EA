# Copyright 2016 Huawei
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import ddt
from tempest import config
from tempest.lib import decorators
from testtools import testcase as tc

from manila_tempest_tests.common import waiters
from manila_tempest_tests.tests.api import base
from manila_tempest_tests import utils

CONF = config.CONF


@ddt.ddt
class ShareSnapshotInstancesTest(base.BaseSharesAdminTest):

    @classmethod
    def skip_checks(cls):
        super(ShareSnapshotInstancesTest, cls).skip_checks()
        if not CONF.share.run_snapshot_tests:
            raise cls.skipException('Snapshot tests are disabled.')

        utils.check_skip_if_microversion_not_supported("2.19")

    @classmethod
    def resource_setup(cls):
        super(ShareSnapshotInstancesTest, cls).resource_setup()
        # create share type
        extra_specs = {'snapshot_support': True}
        cls.share_type = cls.create_share_type(extra_specs=extra_specs)
        cls.share_type_id = cls.share_type['id']
        # create share
        cls.share = cls.create_share(share_type_id=cls.share_type_id)
        snap = cls.create_snapshot_wait_for_active(cls.share["id"])
        cls.snapshot = cls.shares_v2_client.get_snapshot(
            snap['id'])['snapshot']

    @ddt.data(True, False)
    @decorators.idempotent_id('bcb29129-9713-4481-8e74-97682c62f218')
    @tc.attr(base.TAG_POSITIVE, base.TAG_API_WITH_BACKEND)
    def test_list_snapshot_instances_by_snapshot(self, detail):
        """Test that we get only the 1 snapshot instance from snapshot."""
        snapshot_instances = self.shares_v2_client.list_snapshot_instances(
            detail=detail,
            snapshot_id=self.snapshot['id'])['snapshot_instances']

        expected_keys = ['id', 'snapshot_id', 'status']

        if detail:
            extra_detail_keys = ['provider_location', 'share_id',
                                 'share_instance_id', 'created_at',
                                 'updated_at', 'progress']
            expected_keys.extend(extra_detail_keys)

        si_num = len(snapshot_instances)
        self.assertEqual(1, si_num,
                         'Incorrect amount of snapshot instances found; '
                         'expected 1, found %s.' % si_num)

        si = snapshot_instances[0]
        self.assertEqual(self.snapshot['id'], si['snapshot_id'],
                         'Snapshot instance %s has incorrect snapshot id;'
                         ' expected %s, got %s.' % (si['id'],
                                                    self.snapshot['id'],
                                                    si['snapshot_id']))
        if detail:
            self.assertEqual(self.snapshot['share_id'], si['share_id'])

        for key in si:
            self.assertIn(key, expected_keys)
        self.assertEqual(len(expected_keys), len(si))

    @decorators.idempotent_id('1d0bd333-300d-4af2-81eb-176b550f2c36')
    @tc.attr(base.TAG_POSITIVE, base.TAG_API_WITH_BACKEND)
    def test_list_snapshot_instances(self):
        """Test that we get at least the snapshot instance."""
        snapshot_instances = self.shares_v2_client.list_snapshot_instances(
            )['snapshot_instances']

        snapshot_ids = [si['snapshot_id'] for si in snapshot_instances]

        msg = ('Snapshot instance for snapshot %s was not found.' %
               self.snapshot['id'])
        self.assertIn(self.snapshot['id'], snapshot_ids, msg)

    @decorators.idempotent_id('d21bf82d-2b3b-4061-8db5-502b7376a44d')
    @tc.attr(base.TAG_POSITIVE, base.TAG_API_WITH_BACKEND)
    def test_get_snapshot_instance(self):
        instances = self.shares_v2_client.list_snapshot_instances(
            snapshot_id=self.snapshot['id'])['snapshot_instances']
        instance_detail = self.shares_v2_client.get_snapshot_instance(
            instance_id=instances[0]['id'])['snapshot_instance']

        expected_keys = (
            'id', 'created_at', 'updated_at', 'progress', 'provider_location',
            'share_id', 'share_instance_id', 'snapshot_id', 'status',
        )

        for key in instance_detail:
            self.assertIn(key, expected_keys)
        self.assertEqual(len(expected_keys), len(instance_detail))
        self.assertEqual(self.snapshot['id'], instance_detail['snapshot_id'])
        self.assertEqual(self.snapshot['share_id'],
                         instance_detail['share_id'])
        self.assertEqual(self.snapshot['provider_location'],
                         instance_detail['provider_location'])

    @decorators.idempotent_id('c7724848-4e17-4d28-801d-2ec77dfcf502')
    @tc.attr(base.TAG_POSITIVE, base.TAG_API_WITH_BACKEND)
    def test_reset_snapshot_instance_status_and_delete(self):
        """Test resetting a snapshot instance's status attribute."""
        snapshot = self.create_snapshot_wait_for_active(self.share["id"])

        snapshot_instances = self.shares_v2_client.list_snapshot_instances(
            snapshot_id=snapshot['id'])['snapshot_instances']

        sii = snapshot_instances[0]['id']

        for status in ("error", "available"):
            self.shares_v2_client.reset_snapshot_instance_status(
                sii, status=status)
            waiters.wait_for_resource_status(
                self.shares_v2_client, sii, status,
                resource_name='snapshot_instance')
        self.shares_v2_client.delete_snapshot(snapshot['id'])
        self.shares_v2_client.wait_for_resource_deletion(
            snapshot_id=snapshot['id'])
