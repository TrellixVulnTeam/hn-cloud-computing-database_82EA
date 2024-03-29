# Copyright 2013 OpenStack Foundation
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

from manilaclient import base
from manilaclient.common import cliutils


class ListExtResource(base.Resource):
    @property
    def summary(self):
        descr = self.description.strip()
        if not descr:
            return '??'
        lines = descr.split("\n")
        if len(lines) == 1:
            return lines[0]
        else:
            return lines[0] + "..."


class ListExtManager(base.Manager):
    resource_class = ListExtResource

    def show_all(self):
        return self._list("/extensions", 'extensions')


@cliutils.service_type('share')
def do_list_extensions(client, _args):
    """List all the os-api extensions that are available."""
    extensions = client.list_extensions.show_all()
    fields = ["Name", "Summary", "Alias", "Updated"]
    cliutils.print_list(extensions, fields)
