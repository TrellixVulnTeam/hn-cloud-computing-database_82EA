/**
 * Licensed under the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License. You may obtain
 * a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 */

(function() {
  'use strict';

  describe('horizon.cluster.clusters.actions.workflow', function() {

    var workflow, senlin;

    function fakePromise() {
      return { then: angular.noop };
    }

    beforeEach(module('horizon.app.core'));
    beforeEach(module('horizon.framework'));
    beforeEach(module('horizon.cluster.clusters', function($provide) {
      $provide.value('horizon.cluster.clusters.actions.manage-policy.service');
    }));

    beforeEach(inject(function($injector) {
      workflow = $injector.get('horizon.cluster.clusters.actions.workflow');
      senlin = $injector.get('horizon.app.core.openstack-service-api.senlin');
      spyOn(senlin, 'getProfiles').and.callFake(fakePromise);
      spyOn(senlin, 'getClusters').and.callFake(fakePromise);
    }));

    function testInitWorkflow(actionType, title, submitText) {
      var submitIcon, helpUrl;
      submitIcon = 'fa fa-check';
      helpUrl = 'cluster.help.html';

      var config = workflow.init(actionType, title, submitText, submitIcon, helpUrl);

      expect(senlin.getProfiles).toHaveBeenCalled();

      expect(config.title).toEqual(title);
      expect(config.submitText).toEqual(submitText);
      expect(config.schema).toBeDefined();
      expect(config.form).toBeDefined();
      return config;
    }

    it('should be create workflow config for create', function() {
      var config = testInitWorkflow('create', 'Create Cluster', 'Create');
      expect(config.form[0].items[0].items[0].required).toEqual(true);
      expect(config.form[0].items[0].items[1].required).toEqual(true);
      expect(config.form[0].items[0].items[4].required).toEqual(true);
    });

    it('should be create workflow config for update', function() {
      var config = testInitWorkflow('update', 'Update Cluster', 'Update');
      expect(config.form[0].items[0].items[0].required).toEqual(true);
      expect(config.form[0].items[0].items[1].required).toEqual(true);
      expect(config.form[0].items[0].items[2].readonly).toEqual(true);
      expect(config.form[0].items[0].items[3].readonly).toEqual(true);
      expect(config.form[0].items[0].items[4].required).toEqual(false);
      expect(config.form[0].items[0].items[4].readonly).toEqual(true);
    });
  });
})();
