# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox import u

from stix111.cybox.objects.win_waitable_timer_object import WinWaitableTimer

from stix111.cybox.test.objects import ObjectTestCase


class TestWinWaitableTimer(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsWaitableTimerObjectType"
    klass = WinWaitableTimer

    _full_dict = {
        'security_attributes': u("timer attributes"),
        'name': u("timer name"),
        'type': u("timer type"),
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
