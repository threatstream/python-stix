# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from stix111.mixbox import fields, entities

# internal
import stix111
from stix111.common import InformationSource, Statement

# bindings
import stix111.bindings.indicator as indicator_binding


class _BaseTestMechanism(stix111.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = indicator_binding.TestMechanismType

    id_ = fields.IdField("id")
    idref = fields.IdField("idref")
    efficacy = fields.TypedField("Efficacy", Statement)
    producer = fields.TypedField("Producer", InformationSource)

    def __init__(self, id_=None, idref=None):
        super(_BaseTestMechanism, self).__init__()

        self.id_ = id_
        self.idref = idref
        self.efficacy = None
        self.producer = None

    def to_obj(self, ns_info=None):
        obj = super(_BaseTestMechanism, self).to_obj(ns_info=ns_info)
        obj.xsi_type = self._XSI_TYPE
        return obj

    def to_dict(self):
        d = super(_BaseTestMechanism, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE  # added by subclass
        return d


class TestMechanismFactory(entities.EntityFactory):
    @classmethod
    def entity_class(self, key):
        import stix111.extensions.test_mechanism.snort_test_mechanism  # noqa
        import stix111.extensions.test_mechanism.open_ioc_2010_test_mechanism  # noqa
        import stix111.extensions.test_mechanism.yara_test_mechanism  # noqa
        import stix111.extensions.test_mechanism.generic_test_mechanism  # noqa
        return stix111.lookup_extension(key)


class TestMechanisms(stix111.EntityList):
    _binding = indicator_binding
    _namespace = 'http://stix.mitre.org/Indicator-2'
    _binding_class = _binding.TestMechanismsType

    test_mechanism = fields.TypedField(
        name="Test_Mechanism",
        type_=_BaseTestMechanism,
        factory=TestMechanismFactory,
        multiple=True
    )



# Backwards compatibility
add_extension = stix111.add_extension
