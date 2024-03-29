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
#

import sys


AUTH_TOKEN = "foobar"
AUTH_URL = "http://0.0.0.0"
API_VERSION = '2'


class FakeApp(object):
    def __init__(self):
        _stdout = None
        self.client_manager = None
        self.stdin = sys.stdin
        self.stdout = _stdout or sys.stdout
        self.stderr = sys.stderr
        self.restapi = None


class FakeClientManager(object):
    def __init__(self):
        self.identity = None
        self.auth_ref = None
        self.interface = 'public'
        self._region_name = 'RegionOne'
        self.session = 'fake session'
        self._api_version = {'accelerator': API_VERSION}


class FakeResource(object):
    def __init__(self, manager, info, loaded=False):
        self.__name__ = type(self).__name__
        self.manager = manager
        self._info = info
        self._add_details(info)
        self._loaded = loaded

    def _add_details(self, info):
        for (k, v) in info.items():
            setattr(self, k, v)

    def __repr__(self):
        reprkeys = sorted(k for k in self.__dict__.keys() if k[0] != '_' and
                          k != 'manager')
        info = ", ".join("%s=%s" % (k, getattr(self, k)) for k in reprkeys)
        return "<%s %s>" % (self.__class__.__name__, info)

    def to_dict(self):
        return dict(self.__dict__)
