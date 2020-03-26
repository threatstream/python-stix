# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import uuid

from stix111.cybox.objects.dns_query_object import DNSQuestion
from stix111.cybox.test import EntityTestCase


class TestQuestion(EntityTestCase, unittest.TestCase):
    klass = DNSQuestion

    _full_dict = {
        'qname': {
            'value': "www.example.com",
            'xsi:type': "URIObjectType",
        },
        'qtype': "A",
        'qclass': "IN",
    }


if __name__ == "__main__":
    unittest.main()
