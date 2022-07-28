# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from magnum_tempest_plugin.common import models


class MagnumServiceData(models.BaseModel):
    """Data that encapsulates magnum_service attributes"""
    pass


class MagnumServiceEntity(models.EntityModel):
    """Entity Model that represents a single instance of MagnumServiceData"""
    ENTITY_NAME = 'mservice'
    MODEL_TYPE = MagnumServiceData


class MagnumServiceCollection(models.CollectionModel):
    """Collection Model that represents a list of MagnumServiceData objects"""
    COLLECTION_NAME = 'mservicelists'
    MODEL_TYPE = MagnumServiceData
