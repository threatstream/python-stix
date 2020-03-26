# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox import u

from stix111.cybox.objects.win_critical_section_object import WinCriticalSection
from stix111.cybox.test.objects import ObjectTestCase


class TestWinCriticalSection(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsCriticalSectionObjectType"
    klass = WinCriticalSection

    _full_dict = {
        'address': u("deadbeef"),
        'spin_count': 12345,
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
