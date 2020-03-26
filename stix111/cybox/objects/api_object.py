# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.api_object as api_binding
from stix111.cybox.common import ObjectProperties, String, HexBinary, StructuredText, PlatformSpecification


class API(ObjectProperties):
    _binding = api_binding
    _binding_class = api_binding.APIObjectType
    _namespace = "http://cybox.mitre.org/objects#APIObject-2"
    _XSI_NS = "APIObj"
    _XSI_TYPE = "APIObjectType"

    description = fields.TypedField("Description", StructuredText)
    function_name = fields.TypedField("Function_Name", String)
    normalized_function_name = fields.TypedField("Normalized_Function_Name", String)
    platform = fields.TypedField("Platform", PlatformSpecification)
    address = fields.TypedField("Address", HexBinary)
