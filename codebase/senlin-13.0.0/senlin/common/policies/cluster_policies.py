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


from oslo_policy import policy

from senlin.common.policies import base

rules = [
    policy.DocumentedRuleDefault(
        name="cluster_policies:index",
        check_str=base.UNPROTECTED,
        description="List cluster policies",
        operations=[
            {
                'path': '/v1/clusters/{cluster_id}/policies',
                'method': 'GET'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="cluster_policies:attach",
        check_str=base.UNPROTECTED,
        description="Attach a Policy to a Cluster",
        operations=[
            {
                'path': '/v1/clusters/{cluster_id}/actions',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="cluster_policies:detach",
        check_str=base.UNPROTECTED,
        description="Detach a Policy from a Cluster",
        operations=[
            {
                'path': '/v1/clusters/{cluster_id}/actions',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="cluster_policies:update",
        check_str=base.UNPROTECTED,
        description="Update a Policy on a Cluster",
        operations=[
            {
                'path': '/v1/clusters/{cluster_id}/actions',
                'method': 'POST'
            }
        ]
    ),
    policy.DocumentedRuleDefault(
        name="cluster_policies:get",
        check_str=base.UNPROTECTED,
        description="Show cluster_policy details",
        operations=[
            {
                'path': '/v1/clusters/{cluster_id}/policies/{policy_id}',
                'method': 'GET'
            }
        ]
    )
]


def list_rules():
    return rules
