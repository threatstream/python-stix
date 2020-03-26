# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox.vendor.six import u

from stix111.cybox.objects.win_hook_object import WinHook

from stix111.cybox.test.objects import ObjectTestCase


class TestWinHook(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsHookObjectType"
    klass = WinHook

    _full_dict = {
        'type': u("Test Hook"),
        #TODO: add 'handle'
        'hooking_function_name': u("test_function"),
        #TODO: add 'hooking_module'
        'thread_id': 2,
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
