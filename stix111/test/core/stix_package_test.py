# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import copy
import unittest

from stix111.mixbox.vendor.six import BytesIO

from stix111.test import EntityTestCase
from stix111.test.common import kill_chains_test, related_test

from . import stix_header_test

from stix111 import core
from stix111.core import stix_package


class CampaignsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Campaigns

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class COAsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.CoursesOfAction

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class ExploitTargetsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.ExploitTargets

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class IncidentsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Incidents

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class IndicatorsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Indicators

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class ThreatActorsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.ThreatActors

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class TTPsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.TTPs

    _full_dict = {
        'kill_chains': kill_chains_test.KillChainsTests._full_dict,
        'ttps': [
            {'idref': 'example:test-1'}
        ]
    }


class STIXPackageTests(EntityTestCase, unittest.TestCase):
    klass = core.STIXPackage
    _full_dict = {
        'stix_header': stix_header_test.STIXHeaderTests._full_dict,
        'campaigns': CampaignsTests._full_dict,
        'courses_of_action': COAsTests._full_dict,
        'exploit_targets': ExploitTargetsTests._full_dict,
        'incidents': IncidentsTests._full_dict,
        'indicators': IndicatorsTests._full_dict,
        'observables':  {
            'major_version': 2,
            'minor_version': 1,
            'update_version': 0,
            'observables': [
                {
                    'idref': "example:Observable-1"
                }
            ]
        },
        'threat_actors': ThreatActorsTests._full_dict,
        'ttps': TTPsTests._full_dict,
        'related_packages': related_test.RelatedPackagesTests._full_dict,
        'version': "1.1.1"
    }

    def test_deepcopy(self):
        """Test copy.deepcopy() against parsed document.

        Previous versions of python-stix would cause an exception with
        copy.deepcopy() when applied to a parsed STIX component which contained
        timestamp information.

        This was due to the lack of a __reduce__ function defined on the
        bindings._FixedTZOffset class.

        """
        package = core.STIXPackage.from_xml(
            BytesIO(
                core.STIXPackage().to_xml()
            )
        )

        copied = copy.deepcopy(package)
        self.assertEqual(package.timestamp, copied.timestamp)


if __name__ == "__main__":
    unittest.main()
