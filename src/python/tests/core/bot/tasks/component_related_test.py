# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for blame task."""
# pylint: disable=protected-access

import ast
import os
import unittest

from tests.test_libs import helpers
from tests.test_libs import test_utils

DATA_DIRECTORY = os.path.join(
    os.path.dirname(__file__), 'component_related_test_data')


@test_utils.with_cloud_emulators('datastore')
class ComponentRelatedTest(unittest.TestCase):
  """Test prepare_predator_message."""

  def setUp(self):
    helpers.patch_environ(self)

    helpers.patch(self, [
        'build_management.revisions.get_component_revisions_dict',
    ])

    self.mock.get_component_revisions_dict.side_effect = (
        self.mock_get_component_revisions_dict)

  @staticmethod
  def mock_get_component_revisions_dict(revision, _):
    if revision == 0:
      return {}

    component_revisions_file_path = os.path.join(
        DATA_DIRECTORY, 'component_revisions_%s.txt' % revision)
    with open(component_revisions_file_path) as file_handle:
      return ast.literal_eval(file_handle.read())
