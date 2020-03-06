# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields

# internal
import stix111
from stix111.common import EncodedCDATA, StructuredText
from stix111.common.vocabs import VocabField
from stix111.coa.structured_coa import _BaseStructuredCOA

# bindings
import stix111.bindings.extensions.structured_coa.generic as generic_structured_coa_binding


@stix111.register_extension
class GenericStructuredCOA(_BaseStructuredCOA):
    _namespace = "http://stix.mitre.org/extensions/StructuredCOA#Generic-1"
    _binding = generic_structured_coa_binding
    _binding_class = _binding.GenericStructuredCOAType
    _XSI_TYPE = "genericStructuredCOA:GenericStructuredCOAType"

    specification = fields.TypedField("Specification", EncodedCDATA)
    description = fields.TypedField("Description", StructuredText)
    reference_location = fields.TypedField("reference_location")
    type_ = VocabField("Type")

    def __init__(self, id_=None, idref=None):
        super(GenericStructuredCOA, self).__init__(id_=id_, idref=idref)
