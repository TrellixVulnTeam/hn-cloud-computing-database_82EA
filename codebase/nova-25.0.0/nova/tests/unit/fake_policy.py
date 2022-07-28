# Copyright (c) 2012 OpenStack Foundation
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


policy_data = """
{
    "context_is_admin": "role:admin or role:administrator",

    "network:attach_external_network": "",
    "os_compute_api:servers:create": "",
    "os_compute_api:servers:create:attach_volume": "",
    "os_compute_api:servers:create:attach_network": "",
    "os_compute_api:servers:create:forced_host": "",
    "compute:servers:create:requested_destination": "",
    "os_compute_api:servers:create:trusted_certs": "",
    "os_compute_api:servers:create_image": "",
    "os_compute_api:servers:create_image:allow_volume_backed": "",
    "os_compute_api:servers:update": "",
    "os_compute_api:servers:index": "",
    "os_compute_api:servers:index:get_all_tenants": "",
    "os_compute_api:servers:delete": "",
    "os_compute_api:servers:detail": "",
    "os_compute_api:servers:detail:get_all_tenants": "",
    "os_compute_api:servers:show": "",
    "os_compute_api:servers:rebuild": "",
    "os_compute_api:servers:rebuild:trusted_certs": "",
    "os_compute_api:servers:reboot": "",
    "os_compute_api:servers:resize": "",
    "os_compute_api:servers:revert_resize": "",
    "os_compute_api:servers:confirm_resize": "",
    "os_compute_api:servers:start": "",
    "os_compute_api:servers:stop": "",
    "os_compute_api:servers:trigger_crash_dump": "",
    "os_compute_api:servers:show:host_status": "",
    "os_compute_api:servers:show": "",
    "os_compute_api:servers:show:flavor-extra-specs" : "",
    "os_compute_api:servers:show:host_status:unknown-only": "",
    "os_compute_api:servers:allow_all_filters": "",
    "os_compute_api:servers:migrations:force_complete": "",
    "os_compute_api:servers:migrations:index": "",
    "os_compute_api:servers:migrations:show": "",
    "os_compute_api:servers:migrations:delete": "",
    "os_compute_api:os-admin-actions:inject_network_info": "",
    "os_compute_api:os-admin-actions:reset_state": "",
    "os_compute_api:os-admin-password": "",
    "os_compute_api:os-aggregates:set_metadata": "",
    "os_compute_api:os-aggregates:remove_host": "",
    "os_compute_api:os-aggregates:add_host": "",
    "os_compute_api:os-aggregates:create": "",
    "os_compute_api:os-aggregates:index": "",
    "os_compute_api:os-aggregates:update": "",
    "os_compute_api:os-aggregates:delete": "",
    "os_compute_api:os-aggregates:show": "",
    "compute:aggregates:images": "",
    "os_compute_api:os-attach-interfaces:list": "",
    "os_compute_api:os-attach-interfaces:show": "",
    "os_compute_api:os-attach-interfaces:create": "",
    "os_compute_api:os-attach-interfaces:delete": "",
    "os_compute_api:os-baremetal-nodes:list": "",
    "os_compute_api:os-baremetal-nodes:show": "",
    "os_compute_api:os-console-auth-tokens": "",
    "os_compute_api:os-console-output": "",
    "os_compute_api:os-remote-consoles": "",
    "os_compute_api:os-create-backup": "",
    "os_compute_api:os-deferred-delete:restore": "",
    "os_compute_api:os-deferred-delete:force": "",
    "os_compute_api:os-extended-server-attributes": "",
    "os_compute_api:ips:index": "",
    "os_compute_api:ips:show": "",
    "os_compute_api:extensions": "",
    "os_compute_api:os-evacuate": "",
    "os_compute_api:os-flavor-access:remove_tenant_access": "",
    "os_compute_api:os-flavor-access:add_tenant_access": "",
    "os_compute_api:os-flavor-access": "",
    "os_compute_api:os-flavor-extra-specs:create": "",
    "os_compute_api:os-flavor-extra-specs:update": "",
    "os_compute_api:os-flavor-extra-specs:delete": "",
    "os_compute_api:os-flavor-extra-specs:index": "",
    "os_compute_api:os-flavor-extra-specs:show": "",
    "os_compute_api:os-flavor-manage:create": "",
    "os_compute_api:os-flavor-manage:update": "",
    "os_compute_api:os-flavor-manage:delete": "",
    "os_compute_api:os-floating-ip-pools": "",
    "os_compute_api:os-floating-ips:list": "",
    "os_compute_api:os-floating-ips:show": "",
    "os_compute_api:os-floating-ips:create": "",
    "os_compute_api:os-floating-ips:delete": "",
    "os_compute_api:os-floating-ips:add": "",
    "os_compute_api:os-floating-ips:remove": "",
    "os_compute_api:os-instance-actions:list": "",
    "os_compute_api:os-instance-actions:show": "",
    "os_compute_api:os-instance-actions:events": "",
    "os_compute_api:os-instance-actions:events:details": "",
    "os_compute_api:os-instance-usage-audit-log:list": "",
    "os_compute_api:os-instance-usage-audit-log:show": "",
    "os_compute_api:os-keypairs:index": "",
    "os_compute_api:os-keypairs:create": "",
    "os_compute_api:os-keypairs:show": "",
    "os_compute_api:os-keypairs:delete": "",
    "os_compute_api:os-hosts:list": "",
    "os_compute_api:os-hosts:show": "",
    "os_compute_api:os-hosts:update": "",
    "os_compute_api:os-hosts:reboot": "",
    "os_compute_api:os-hosts:shutdown": "",
    "os_compute_api:os-hosts:start": "",
    "os_compute_api:os-hypervisors:list": "",
    "os_compute_api:os-hypervisors:list-detail": "",
    "os_compute_api:os-hypervisors:statistics": "",
    "os_compute_api:os-hypervisors:show": "",
    "os_compute_api:os-hypervisors:uptime": "",
    "os_compute_api:os-hypervisors:search": "",
    "os_compute_api:os-hypervisors:servers": "",

    "os_compute_api:os-lock-server:lock": "",
    "os_compute_api:os-lock-server:unlock": "",
    "os_compute_api:os-migrate-server:migrate": "",
    "os_compute_api:os-migrate-server:migrate_live": "",
    "os_compute_api:os-migrations:index": "",
    "os_compute_api:os-multinic:add": "",
    "os_compute_api:os-multinic:remove": "",
    "os_compute_api:os-networks:list": "",
    "os_compute_api:os-networks:show": "",
    "os_compute_api:os-tenant-networks:list": "",
    "os_compute_api:os-tenant-networks:show": "",
    "os_compute_api:os-pause-server:pause": "",
    "os_compute_api:os-pause-server:unpause": "",
    "os_compute_api:os-quota-sets:show": "",
    "os_compute_api:os-quota-sets:update": "",
    "os_compute_api:os-quota-sets:delete": "",
    "os_compute_api:os-quota-sets:detail": "",
    "os_compute_api:os-quota-sets:defaults": "",
    "os_compute_api:os-quota-class-sets:update": "",
    "os_compute_api:os-quota-class-sets:show": "",
    "os_compute_api:os-rescue": "",
    "os_compute_api:os-unrescue": "",
    "os_compute_api:os-security-groups:list": "",
    "os_compute_api:os-security-groups:add": "",
    "os_compute_api:os-security-groups:remove": "",
    "os_compute_api:os-security-groups:get": "",
    "os_compute_api:os-security-groups:show": "",
    "os_compute_api:os-security-groups:create": "",
    "os_compute_api:os-security-groups:delete": "",
    "os_compute_api:os-security-groups:update": "",
    "os_compute_api:os-security-groups:rule:create": "",
    "os_compute_api:os-security-groups:rule:delete": "",
    "os_compute_api:os-server-diagnostics": "",
    "os_compute_api:os-server-password:show": "",
    "os_compute_api:os-server-password:clear": "",
    "os_compute_api:os-server-external-events:create": "",
    "os_compute_api:os-server-tags:index": "",
    "os_compute_api:os-server-tags:show": "",
    "os_compute_api:os-server-tags:update": "",
    "os_compute_api:os-server-tags:update_all": "",
    "os_compute_api:os-server-tags:delete": "",
    "os_compute_api:os-server-tags:delete_all": "",
    "os_compute_api:os-server-groups:show": "",
    "os_compute_api:os-server-groups:index": "",
    "os_compute_api:os-server-groups:index:all_projects": "",
    "os_compute_api:os-server-groups:create": "",
    "os_compute_api:os-server-groups:delete": "",
    "os_compute_api:os-services:list": "",
    "os_compute_api:os-services:update": "",
    "os_compute_api:os-services:delete": "",
    "os_compute_api:os-shelve:shelve": "",
    "os_compute_api:os-shelve:shelve_offload": "",
    "os_compute_api:os-simple-tenant-usage:show": "",
    "os_compute_api:os-simple-tenant-usage:list": "",
    "os_compute_api:os-shelve:unshelve": "",
    "os_compute_api:os-suspend-server:suspend": "",
    "os_compute_api:os-suspend-server:resume": "",
    "os_compute_api:os-volumes:list": "",
    "os_compute_api:os-volumes:detail": "",
    "os_compute_api:os-volumes:create": "",
    "os_compute_api:os-volumes:show": "",
    "os_compute_api:os-volumes:delete": "",
    "os_compute_api:os-volumes:snapshots:create": "",
    "os_compute_api:os-volumes:snapshots:show": "",
    "os_compute_api:os-volumes:snapshots:delete": "",
    "os_compute_api:os-volumes:snapshots:list": "",
    "os_compute_api:os-volumes:snapshots:detail": "",
    "os_compute_api:os-volumes-attachments:index": "",
    "os_compute_api:os-volumes-attachments:show": "",
    "os_compute_api:os-volumes-attachments:create": "",
    "os_compute_api:os-volumes-attachments:update": "",
    "os_compute_api:os-volumes-attachments:swap":"",
    "os_compute_api:os-volumes-attachments:delete": "",
    "os_compute_api:os-availability-zone:list": "",
    "os_compute_api:os-availability-zone:detail": "",
    "os_compute_api:limits": "",
    "os_compute_api:os-assisted-volume-snapshots:create": "",
    "os_compute_api:os-assisted-volume-snapshots:delete": "",
    "os_compute_api:server-metadata:create": "",
    "os_compute_api:server-metadata:update": "",
    "os_compute_api:server-metadata:update_all": "",
    "os_compute_api:server-metadata:delete": "",
    "os_compute_api:server-metadata:show": "",
    "os_compute_api:server-metadata:index": "",
    "compute:server:topology:index": "",
    "compute:server:topology:host:index": "is_admin:True"
}
"""
