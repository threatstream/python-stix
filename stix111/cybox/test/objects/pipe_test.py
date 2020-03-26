# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox import u

from stix111.cybox.objects.pipe_object import Pipe
from stix111.cybox.test.objects import ObjectTestCase


class TestPipe(ObjectTestCase, unittest.TestCase):
    object_type = "PipeObjectType"
    klass = Pipe

    _full_dict = {
        'name': u("pipe1"),
        'named': True,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
