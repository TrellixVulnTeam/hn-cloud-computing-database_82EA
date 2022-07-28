# Copyright 2016 OpenStack Foundation
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
#

"""rename device db tables

Revision ID: 22f5385a3d50
Revises: 22f5385a3d4f
Create Date: 2016-08-01 15:47:51.161749

"""

# flake8: noqa: E402

# revision identifiers, used by Alembic.
revision = '22f5385a3d50'
down_revision = '22f5385a3d4f'

from alembic import op
import sqlalchemy as sa

from tacker.db import migration


def upgrade(active_plugins=None, options=None):
    # commands auto generated by Alembic - please adjust! #
    op.rename_table('devicetemplates', 'vnfd')
    op.rename_table('devicetemplateattributes', 'vnfd_attribute')
    op.rename_table('devices', 'vnf')
    op.rename_table('deviceattributes', 'vnf_attribute')
    migration.modify_foreign_keys_constraint_with_col_change(
        'vnfd_attribute', 'template_id', 'vnfd_id',
        sa.String(length=36))
    migration.modify_foreign_keys_constraint_with_col_change(
        'servicetypes', 'template_id', 'vnfd_id',
        sa.String(length=36))
    migration.modify_foreign_keys_constraint_with_col_change(
        'vnf', 'template_id', 'vnfd_id',
        sa.String(length=36))
    migration.modify_foreign_keys_constraint_with_col_change(
        'vnf_attribute', 'device_id', 'vnf_id',
        sa.String(length=36))
    # end Alembic commands #
