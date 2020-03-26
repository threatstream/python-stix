# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox import u

from stix111.cybox.common import MeasureSource
from stix111.cybox.test import EntityTestCase


class TestMeasureSource(EntityTestCase, unittest.TestCase):
    klass = MeasureSource

    _full_dict = {
        'class': "Software",
        'source_type': "Information Source",
        'name': "ASource",
        'information_source_type': u("Web Logs"),
        'tool_type': u("Vulnerability Scanner"),
        'description': u("A description of the source"),
        'contributors': [
            {
                'name': u("An amazing dude"),
                'email': u("amazing@dude.com"),
            },
            {
                'name': u("Another amazing dude"),
                'role': u("President of Amazing"),
                'organization': u("AmazingCo."),
            },
        ],
        'time': {
            'start_time': "2013-02-14T11:28:42-05:00",
            'end_time': "2014-03-11T06:22:17-05:00",
        },
        'tools': [
            {'name': u("AmazingTool (TM)")}
        ],
        'platform': {'description': u("The best platform")},
        #TODO: Add System and Instance
    }


if __name__ == "__main__":
    unittest.main()
