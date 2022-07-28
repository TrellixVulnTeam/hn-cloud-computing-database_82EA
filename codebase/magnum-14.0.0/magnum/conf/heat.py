# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import itertools

from oslo_config import cfg

from magnum.i18n import _

heat_group = cfg.OptGroup(name='heat_client',
                          title='Options for the Heat client')

heat_client_opts = [
    cfg.StrOpt('region_name',
               help=_('Region in Identity service catalog to use for '
                      'communication with the OpenStack service.')),
    cfg.StrOpt('endpoint_type',
               default='publicURL',
               help=_('Type of endpoint in Identity service catalog to use '
                      'for communication with the OpenStack service.')),
    cfg.StrOpt('api_version',
               default='1',
               help=_('Version of Heat API to use in heatclient.'))]

common_security_opts = [
    cfg.StrOpt('ca_file',
               help=_('Optional CA cert file to use in SSL connections.')),
    cfg.StrOpt('cert_file',
               help=_('Optional PEM-formatted certificate chain file.')),
    cfg.StrOpt('key_file',
               help=_('Optional PEM-formatted file that contains the '
                      'private key.')),
    cfg.BoolOpt('insecure',
                default=False,
                help=_("If set, then the server's certificate will not "
                       "be verified."))]

ALL_OPTS = list(itertools.chain(
    heat_client_opts,
    common_security_opts
))


def register_opts(conf):
    conf.register_group(heat_group)
    conf.register_opts(ALL_OPTS, group=heat_group)


def list_opts():
    return {
        heat_group: ALL_OPTS
    }
