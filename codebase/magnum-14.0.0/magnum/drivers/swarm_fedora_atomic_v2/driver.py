# Copyright 2016 Rackspace Inc. All rights reserved.
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

from magnum.drivers.heat import driver
from magnum.drivers.swarm_fedora_atomic_v2 import monitor
from magnum.drivers.swarm_fedora_atomic_v2 import template_def


class Driver(driver.HeatDriver):

    @property
    def provides(self):
        return [
            {'server_type': 'vm',
             'os': 'fedora-atomic',
             'coe': 'swarm-mode'},
        ]

    def get_template_definition(self):
        return template_def.AtomicSwarmTemplateDefinition()

    def get_monitor(self, context, cluster):
        return monitor.SwarmMonitor(context, cluster)

    def upgrade_cluster(self, context, cluster, cluster_template,
                        max_batch_size, nodegroup, scale_manager=None,
                        rollback=False):
        raise NotImplementedError("Must implement 'upgrade_cluster'")
