# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------
#Change the implementation of InstanceAction class
#Original code reference https://github.com/yunify/qingcloud-sdk-python/tree/master/qingcloud
# =========================================================================

from app.constants import INSTANCES
from app.errors import InvalidParameterError
from app.utils import filter_out_none,check_params

class InstanceAction(object):

    def __init__(self, conn):
        self.conn = conn

    def describe_instances(self, body):
        """ Describe instances filtered by conditions
        :param body :a dictionary of conditions required to filter instance
        :param body.instances : the array of IDs of instances
        :param body.image_id : ID of the image which is used to launch this instance.
        :param body.instance_type: The instance type.
                              See: https://docs.qingcloud.com/api/common/includes/instance_type.html
        :param body.status : Status of the instance, including pending, running, stopped, terminated.
        :param body.verbose: the number to specify the verbose level, larger the number, the more detailed information will be returned.
        :param body.search_word: the combined search column.
        :param body.offset: the starting offset of the returning results.
        :param body.limit: specify the number of the returning results.
        :param body.tags : the array of IDs of tags.
        :rtype: the array of instances filtered by conditions
        """
        action = INSTANCES['ACTION_DESCRIBE_INSTANCES']
        valid_keys = ('instances', 'image_id', 'instance_type', 'status',
                      'search_word', 'verbose', 'offset', 'limit', 'tags', 'owner')
        #将locals()修改为入参body
        body = filter_out_none(body, valid_keys)
        if not check_params(body, required_params=[],
                                  integer_params=['offset', 'limit', 'verbose'],
                                  list_params=['instances', 'status', 'tags']):
            # throw an exception instead of returning an empty list
            # check_params will throw an exception when params are not valid.
            raise InvalidParameterError('describe instances params invalid')
        return self.conn.send_request(action, body)

    def stop_instances(self, body):
        """ Stop one or more instances.
        :param body :a dictionary needed to stop the instance
        :param body.instances : An array including IDs of the instances you want to stop.
        :param body.force: False for gracefully shutdown and True for forcibly shutdown.
        :rtype: Whether the instance has been stopped
        """
        action = INSTANCES['ACTION_STOP_INSTANCES']
        valid_keys = ('instances', 'force')
        body = filter_out_none(body, valid_keys)
        if not check_params(body, required_params=['instances'],
                                  integer_params=['force'],
                                  list_params=['instances']):
            raise InvalidParameterError('stop instances params invalid')
        return self.conn.send_request(action, body)