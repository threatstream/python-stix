# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.win_filemapping_object as win_filemapping_binding
from stix111.cybox.objects.win_handle_object import WinHandle
from stix111.cybox.common import ObjectProperties, String, UnsignedLong


class WinFilemapping(ObjectProperties):
    _binding = win_filemapping_binding
    _binding_class = win_filemapping_binding.WindowsFilemappingObjectType
    _namespace = "http://cybox.mitre.org/objects#WinFilemappingObject-1"
    _XSI_NS = "WinFilemappingObj"
    _XSI_TYPE = "WindowsFilemappingObjectType"

    name = fields.TypedField("Name", String)
    file_handle = fields.TypedField("File_Handle", WinHandle)
    handle = fields.TypedField("Handle", WinHandle)
    page_protection_value = fields.TypedField("Page_Protection_Value", String)
    page_protection_attribute = fields.TypedField("Page_Protection_Attribute", String, multiple=True)
    maximum_size = fields.TypedField("Maximum_Size", UnsignedLong)
    actual_size = fields.TypedField("Actual_Size", UnsignedLong)
    security_attributes = fields.TypedField("Security_Attributes", String)