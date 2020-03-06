# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix111
import stix111.utils
import stix111.indicator.test_mechanism
from stix111.common import EncodedCDATA
from stix111.indicator.test_mechanism import _BaseTestMechanism
import stix111.bindings.extensions.test_mechanism.yara as yara_tm_binding


@stix.register_extension
class YaraTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#YARA-1"
    _binding = yara_tm_binding
    _binding_class = _binding.YaraTestMechanismType
    _XSI_TYPE = "yaraTM:YaraTestMechanismType"

    version = fields.TypedField("Version")
    rule = fields.TypedField("Rule", EncodedCDATA)

    def __init__(self, id_=None, idref=None):
        super(YaraTestMechanism, self).__init__(id_=id_, idref=idref)
