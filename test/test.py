# coding: utf-8
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

import time
import unittest

import sys
from app.errors import InvalidParameterError
from app.utils import (filter_out_none, check_params, check_integer_params, 
                    check_list_params, check_required_params)


class UtilsTestCase(unittest.TestCase):
    def test_filter_out_none(self):
        data = {'a': 1, 'b': 2, 'c': None}
        self.assertEqual(filter_out_none(data), {})
        self.assertEqual(filter_out_none(data, keys=['a', 'c']), {'a': 1})

    def test_check_integer_params(self):
        data = {'a': 1, 'b': 2, 'c': None}
        self.assertEqual(check_integer_params(data, ['a','b']), None)
        self.assertRaises(InvalidParameterError, check_integer_params, data, ['a','c'])

    def test_check_required_params(self):
        data = {'a': 1, 'b': 2, 'c': None}
        self.assertEqual(check_required_params(data, ['a','b']), None)
        self.assertRaises(InvalidParameterError, check_required_params, data, ['a','d']) 

    def test_check_list_params(self):
        data = {'a': [], 'b': [], 'c': None}
        self.assertEqual(check_list_params(data, ['a','b','d']), None)
        self.assertRaises(InvalidParameterError, check_list_params, data, ['a','c']) 

    def test_check_params(self):
        data = {'a': 1, 'b': [], 'c': None}
        self.assertEqual(check_params(data,integer_params=['a'], 
                                            list_params=['b','d']), True)
        self.assertRaises(InvalidParameterError, check_params, data, 
                            {"integer_params":['a'], "list_params":['b','d']}) 


if __name__ == "__main__":
    unittest.main()