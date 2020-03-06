# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix111.test import EntityTestCase
from stix111 import common


class ToolInformationTests(EntityTestCase, unittest.TestCase):
    klass = common.ToolInformation

    _full_dict = {
        'id': 'example:test-1',   # from python-cybox
        'name': 'Test Tool Name',  # from python-cybox
        'title': 'Test Title',
        'short_description': 'Test Short Description'
    }


if __name__ == "__main__":
    unittest.main()
