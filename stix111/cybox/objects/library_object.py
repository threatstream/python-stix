# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.library_object as library_binding
from stix111.cybox.common.extracted_features import ExtractedFeatures
from stix111.cybox.common import ObjectProperties, String, UnsignedLong, HexBinary


class Library(ObjectProperties):
    _binding = library_binding
    _binding_class = library_binding.LibraryObjectType
    _namespace = "http://cybox.mitre.org/objects#LibraryObject-2"
    _XSI_NS = "LibraryObj"
    _XSI_TYPE = "LibraryObjectType"

    name = fields.TypedField("Name", String)
    path = fields.TypedField("Path", String)
    size = fields.TypedField("Size", UnsignedLong)
    type_ = fields.TypedField("Type", String)
    version = fields.TypedField("Version", String)
    base_address = fields.TypedField("Base_Address", HexBinary)
    extracted_features = fields.TypedField("Extracted_Features", ExtractedFeatures)
