# Copyright 2016 NEC Corporation. All rights reserved.
#
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

from oslo_serialization import jsonutils
from oslo_utils import uuidutils
from tempest import config

from mistral_tempest_tests.services import base

CONF = config.CONF


class MistralClientV2(base.MistralClientBase):

    def post_request(self, url_path, file_name):
        headers = {"headers": "Content-Type:text/plain"}

        return self.post(
            url_path,
            base.get_resource(file_name),
            headers=headers
        )

    def get_request(self, url_path):
        headers = {"headers": "Content-Type:application/json"}

        return self.get(url_path, headers=headers)

    def post_json(self, url_path, obj, extra_headers=None):
        if extra_headers is None:
            extra_headers = {}
        headers = {"Content-Type": "application/json"}
        headers = dict(headers, **extra_headers)
        return self.post(url_path,
                         jsonutils.dump_as_bytes(obj),
                         headers=headers)

    def update_request(self, url_path, file_name):
        headers = {"headers": "Content-Type:text/plain"}

        resp, body = self.put(
            url_path,
            base.get_resource(file_name),
            headers=headers
        )

        return resp, jsonutils.loads(body)

    def get_definition(self, item, name):
        resp, body = self.get("%s/%s" % (item, name))

        return resp, jsonutils.loads(body)['definition']

    def create_workbook(self, yaml_file):
        resp, body = self.post_request('workbooks', yaml_file)

        wb_name = jsonutils.loads(body)['name']
        self.workbooks.append(wb_name)

        _, wfs = self.get_list_obj('workflows')

        for wf in wfs['workflows']:
            if wf['name'].startswith(wb_name):
                self.workflows.append(wf['id'])

        return resp, jsonutils.loads(body)

    def create_workflow(self, yaml_file, scope=None, namespace=None):
        url_path = 'workflows?'

        if scope:
            url_path += 'scope=public&'

        if namespace:
            url_path += 'namespace=' + namespace

        resp, body = self.post_request(url_path, yaml_file)

        for wf in jsonutils.loads(body)['workflows']:
            self.workflows.append(wf['id'])

        return resp, jsonutils.loads(body)

    def get_workflow(self, wf_identifier, namespace=None):

        url_path = 'workflows/' + wf_identifier
        if namespace:
            url_path += 'namespace=' + namespace

        resp, body = self.get_request(url_path)

        return resp, jsonutils.loads(body)

    def update_workflow(self, file_name, namespace=None):
        url_path = "workflows?"

        if namespace:
            url_path += 'namespace=' + namespace

        return self.update_request(url_path, file_name=file_name)

    def get_action_execution(self, action_execution_id):
        return self.get('action_executions/%s' % action_execution_id)

    def get_action_executions(self, task_id=None):
        url_path = 'action_executions'
        if task_id:
            url_path += '?task_execution_id=%s' % task_id

        return self.get_list_obj(url_path)

    def create_execution(self, identifier, wf_namespace=None, wf_input=None,
                         params=None):
        if uuidutils.is_uuid_like(identifier):
            body = {"workflow_id": "%s" % identifier}
        else:
            body = {"workflow_name": "%s" % identifier}

        if wf_namespace:
            body.update({'workflow_namespace': wf_namespace})

        if wf_input:
            body.update({'input': jsonutils.dump_as_bytes(wf_input)})
        if params:
            body.update({'params': jsonutils.dump_as_bytes(params)})

        resp, body = self.post('executions', jsonutils.dump_as_bytes(body))

        self.executions.append(jsonutils.loads(body)['id'])

        return resp, jsonutils.loads(body)

    def update_execution(self, execution_id, put_body):
        resp, body = self.put('executions/%s' % execution_id, put_body)

        return resp, jsonutils.loads(body)

    def get_execution(self, execution_id):
        return self.get('executions/%s' % execution_id)

    def get_executions(self, task_id):
        url_path = 'executions'
        if task_id:
            url_path += '?task_execution_id=%s' % task_id

        return self.get_list_obj(url_path)

    def get_tasks(self, execution_id=None):
        url_path = 'tasks'
        if execution_id:
            url_path += '?workflow_execution_id=%s' % execution_id

        return self.get_list_obj(url_path)

    def create_cron_trigger(self, name, wf_name, wf_input=None, pattern=None,
                            first_time=None, count=None):
        post_body = {
            'name': name,
            'workflow_name': wf_name,
            'pattern': pattern,
            'remaining_executions': count,
            'first_execution_time': first_time
        }

        if wf_input:
            post_body.update({
                'workflow_input': jsonutils.dump_as_bytes(wf_input)})

        rest, body = self.post('cron_triggers',
                               jsonutils.dump_as_bytes(post_body))

        self.triggers.append(name)

        return rest, jsonutils.loads(body)

    def create_action(self, yaml_file):
        resp, body = self.post_request('actions', yaml_file)

        self.actions.extend(
            [action['name'] for action in jsonutils.loads(body)['actions']])

        return resp, jsonutils.loads(body)

    def get_wf_tasks(self, wf_name):
        all_tasks = self.get_list_obj('tasks')[1]['tasks']

        return [t for t in all_tasks if t['workflow_name'] == wf_name]

    def create_action_execution(self, request_body, extra_headers=None):
        if extra_headers is None:
            extra_headers = {}
        resp, body = self.post_json('action_executions', request_body,
                                    extra_headers)

        params = jsonutils.loads(request_body.get('params', '{}'))
        if params.get('save_result', False):
            self.action_executions.append(jsonutils.loads(body)['id'])

        return resp, jsonutils.loads(body)

    def create_event_trigger(self, wf_id, exchange, topic, event, name='',
                             wf_input=None, wf_params=None):
        post_body = {
            'workflow_id': wf_id,
            'exchange': exchange,
            'topic': topic,
            'event': event,
            'name': name
        }

        if wf_input:
            post_body.update({
                'workflow_input': jsonutils.dump_as_bytes(wf_input)})

        if wf_params:
            post_body.update({
                'workflow_params': jsonutils.dump_as_bytes(wf_params)})

        rest, body = self.post('event_triggers',
                               jsonutils.dump_as_bytes(post_body))

        event_trigger = jsonutils.loads(body)
        self.event_triggers.append(event_trigger['id'])

        return rest, event_trigger
