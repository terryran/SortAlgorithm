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
# =========================================================================

from app.errors import InvalidParameterError

def filter_out_none(dictionary, keys=None):
    """ Filter out items whose value is None.
    If `keys` specified, only return non-None items with matched key.
    """
    if keys is None:
        return {}
    return {i:dictionary.get(i) for i in keys if dictionary.get(i) is not None}

def check_integer_params(directive, params):
    """ Specified params should be `int` type if in directive
    :param directive: the directive to check
    :param params: the params that should be `int` type.
    """
    for param in params:
        if param not in directive:
            continue
        val = directive.get(param)
        if is_integer(val):
            directive[param] = int(val)
        else:
            raise InvalidParameterError(
                "parameter [%s] should be integer in directive [%s]" % (param, directive))

def is_integer(value):
    try:
        int(value)
    except:
        return False
    return True

def check_list_params(directive, params):
    """ Specified params should be `list` type if in directive
    :param directive: the directive to check
    :param params: the params that should be `list` type.
    """
    for param in params:
        if param not in directive:
            continue
        if not isinstance(directive[param], list):
            raise InvalidParameterError(
                "parameter [%s] should be list in directive [%s]" % (param, directive))

def check_required_params(directive, params):
    """ Specified params should be in directive
    :param directive: the directive to check
    :param params: the params that should be in directive.
    """
    for param in params:
        if param not in directive:
            raise InvalidParameterError(
                "[%s] should be specified in directive [%s]" % (param, directive))


def check_params(directive, required_params=None,
                integer_params=None, list_params=None):
    """ Check parameters in directive
    :param directive: the directive to check, should be `dict` type.
    :param required_params: a list of parameter that should be in directive.
    :param integer_params: a list of parameter that should be `integer` type
                            if it exists in directive.
    :param list_params: a list of parameter that should be `list` type
                        if it exists in directive.
    """
    if not isinstance(directive, dict):
        raise InvalidParameterError('[%s] should be dict type' % directive)

    if required_params:
        check_required_params(directive, required_params)
    if integer_params:
        check_integer_params(directive, integer_params)
    if list_params:
        check_list_params(directive, list_params)
    return True