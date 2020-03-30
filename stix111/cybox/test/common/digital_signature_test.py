# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.cybox.common import DigitalSignature, DigitalSignatureList
import stix111.cybox.test
from stix111.cybox.test import EntityTestCase


class TestDigitalSignature(EntityTestCase, unittest.TestCase):
    klass = DigitalSignature

    _full_dict = {
        'signature_exists': True,
        'signature_verified': False,
        'certificate_issuer': "SomeIssuer",
        'certificate_subject': "The Subject",
        'signature_description': "A Fake Signature",
    }


class TestDigitalSignatureList(unittest.TestCase):

    def test_round_trip(self):
        siglist_list = [
                {'certificate_issuer': "IssuerA", 'signature_verified': True},
                {'signature_description': "A Signature"},
            ]
        siglist_list2 = stix111.cybox.test.round_trip_list(DigitalSignatureList,
                                                       siglist_list)
        self.assertEqual(siglist_list, siglist_list2)


if __name__ == "__main__":
    unittest.main()