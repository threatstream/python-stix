# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox import u

from stix111.cybox.objects.network_route_object import NetRoute

from stix111.cybox.test.objects import ObjectTestCase


class TestNetworkRoute(ObjectTestCase, unittest.TestCase):
    object_type = "NetRouteObjectType"
    klass = NetRoute

    _full_dict = {
        'is_ipv6': False,
        'is_autoconfigure_address': True,
        'is_immortal': False,
        'is_loopback': False,
        'is_publish': True,
        'description': "A description",
        'preferred_lifetime': u("P10D"),
        'valid_lifetime': u("P5D"),
        'route_age': u("P1D"),
        #'network_route_entries': [],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
