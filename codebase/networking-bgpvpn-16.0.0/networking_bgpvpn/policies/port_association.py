#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from oslo_policy import policy

from networking_bgpvpn.policies import base


rules = [
    policy.DocumentedRuleDefault(
        'create_bgpvpn_port_association',
        base.RULE_ADMIN_OR_OWNER,
        'Create a port association',
        [
            {
                'method': 'POST',
                'path': '/bgpvpn/bgpvpns/{bgpvpn_id}/port_associations',
            },
        ]
    ),
    policy.DocumentedRuleDefault(
        'update_bgpvpn_port_association',
        base.RULE_ADMIN_OR_OWNER,
        'Update a port association',
        [
            {
                'method': 'PUT',
                'path': ('/bgpvpn/bgpvpns/{bgpvpn_id}/'
                         'port_associations/{port_association_id}'),
            },
        ]
    ),
    policy.DocumentedRuleDefault(
        'delete_bgpvpn_port_association',
        base.RULE_ADMIN_OR_OWNER,
        'Delete a port association',
        [
            {
                'method': 'DELETE',
                'path': ('/bgpvpn/bgpvpns/{bgpvpn_id}/'
                         'port_associations/{port_association_id}'),
            },
        ]
    ),
    policy.DocumentedRuleDefault(
        'get_bgpvpn_port_association',
        base.RULE_ADMIN_OR_OWNER,
        'Get port associations',
        [
            {
                'method': 'GET',
                'path': '/bgpvpn/bgpvpns/{bgpvpn_id}/port_associations',
            },
            {
                'method': 'GET',
                'path': ('/bgpvpn/bgpvpns/{bgpvpn_id}/'
                         'port_associations/{port_association_id}'),
            },
        ]
    ),
    policy.DocumentedRuleDefault(
        'get_bgpvpn_port_association:tenant_id',
        base.RULE_ADMIN_ONLY,
        'Get ``tenant_id`` attributes of port associations',
        [
            {
                'method': 'GET',
                'path': '/bgpvpn/bgpvpns/{bgpvpn_id}/port_associations',
            },
            {
                'method': 'GET',
                'path': ('/bgpvpn/bgpvpns/{bgpvpn_id}/'
                         'port_associations/{port_association_id}'),
            },
        ]
    ),
]


def list_rules():
    return rules
