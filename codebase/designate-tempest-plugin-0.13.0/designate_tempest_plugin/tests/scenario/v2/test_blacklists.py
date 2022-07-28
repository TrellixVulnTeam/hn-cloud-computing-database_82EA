# Copyright 2021 Red Hat.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_log import log as logging
from tempest import config
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc

from designate_tempest_plugin import data_utils as dns_data_utils
from designate_tempest_plugin.tests import base

CONF = config.CONF
LOG = logging.getLogger(__name__)


class BaseBlacklistsTest(base.BaseDnsV2Test):
    excluded_keys = ['created_at', 'updated_at', 'links']


class BlacklistE2E(BaseBlacklistsTest):

    credentials = ["admin", 'primary', 'system_admin']

    @classmethod
    def setup_credentials(cls):
        # Do not create network resources for these test.
        cls.set_network_resources()
        super(BlacklistE2E, cls).setup_credentials()

    @classmethod
    def setup_clients(cls):
        super(BlacklistE2E, cls).setup_clients()
        if CONF.enforce_scope.designate:
            cls.admin_blacklist_client = (
                cls.os_system_admin.dns_v2.BlacklistsClient())
            cls.admin_zone_client = cls.os_system_admin.dns_v2.ZonesClient()
        else:
            cls.admin_blacklist_client = cls.os_admin.dns_v2.BlacklistsClient()
            cls.admin_zone_client = cls.os_admin.dns_v2.ZonesClient()
        cls.primary_zone_client = cls.os_primary.dns_v2.ZonesClient()

    @decorators.idempotent_id('22b1ee72-d8d2-11eb-bcdc-74e5f9e2a801')
    def test_primary_fails_to_create_zone_matches_blacklist_regex(self):
        LOG.info('Create a blacklist using regex')
        blacklist = {
            'pattern': '^blacklistregextest.*',
            'description': 'Zone starts with "blacklistregextest" char'}
        body = self.admin_blacklist_client.create_blacklist(**blacklist)[1]
        self.addCleanup(
            self.admin_blacklist_client.delete_blacklist, body['id'])

        LOG.info('Try to create a zone that is starts with '
                 '"blacklistregextest".')
        self.assertRaisesDns(
            lib_exc.BadRequest, 'invalid_zone_name', 400,
            self.primary_zone_client.create_zone,
            name='blacklistregextest' + dns_data_utils.rand_zone_name())

    @decorators.idempotent_id('6956f20c-d8d5-11eb-bcdc-74e5f9e2a801')
    def test_primary_fails_to_create_zone_matches_blacklist_name(self):
        LOG.info('Create a blacklist using the exact name(string)')
        zone_name = 'blacklistnametest' + dns_data_utils.rand_zone_name()
        blacklist = {
            'pattern': zone_name,
            'description': 'Zone named:{} '.format(zone_name)}
        body = self.admin_blacklist_client.create_blacklist(**blacklist)[1]
        self.addCleanup(
            self.admin_blacklist_client.delete_blacklist, body['id'])

        LOG.info('Try to create a zone named:{}'.format(zone_name))
        self.assertRaisesDns(
            lib_exc.BadRequest, 'invalid_zone_name', 400,
            self.primary_zone_client.create_zone, name=zone_name)

    @decorators.idempotent_id('de030088-d97e-11eb-8ab8-74e5f9e2a801')
    def test_admin_creates_zone_matches_blacklist_name_or_regex(self):
        LOG.info('Create a blacklists using: regex and exact string(name)')
        zone_name = 'blacklistnameregextest1' + dns_data_utils.rand_zone_name()
        blacklists = [
            {'pattern': '^blacklistnameregextest2.*',
             'description': 'Zone starts with "a" char'},
            {'pattern': zone_name,
             'description': 'Deny if Zone named:{} '.format(zone_name)}]
        for blacklist in blacklists:
            body = self.admin_blacklist_client.create_blacklist(**blacklist)[1]
            self.addCleanup(
                self.admin_blacklist_client.delete_blacklist, body['id'])

        LOG.info('As Admin user try to create zones that are '
                 'supposed to be blocked')
        zone = self.admin_zone_client.create_zone(
            name='blacklistnameregextest2' +
                 dns_data_utils.rand_zone_name(),
            project_id=self.primary_zone_client.project_id)[1]
        self.addCleanup(
            self.wait_zone_delete, self.admin_zone_client, zone['id'])
        zone = self.admin_zone_client.create_zone(
            name=zone_name, project_id=self.primary_zone_client.project_id)[1]
        self.addCleanup(
            self.wait_zone_delete, self.admin_zone_client, zone['id'])
