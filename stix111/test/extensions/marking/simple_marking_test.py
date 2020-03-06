# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.test import EntityTestCase

from stix111.extensions.marking.simple_marking import SimpleMarkingStructure


class SimpleMarkingStructureTests(EntityTestCase, unittest.TestCase):
    klass = SimpleMarkingStructure
    _full_dict = {
        'statement': "This is a marking statement",
        'xsi:type': "simpleMarking:SimpleMarkingStructureType",
    }


if __name__ == "__main__":
    unittest.main()

