# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.win_event_object as win_event_binding
from stix111.cybox.objects.win_handle_object import WinHandle
from stix111.cybox.common import ObjectProperties, String


class WinEvent(ObjectProperties):
    _binding = win_event_binding
    _binding_class = win_event_binding.WindowsEventObjectType
    _namespace = "http://cybox.mitre.org/objects#WinEventObject-2"
    _XSI_NS = "WinEventObj"
    _XSI_TYPE = "WindowsEventObjectType"

    name = fields.TypedField("Name", String)
    handle = fields.TypedField("Handle", WinHandle)
    type_ = fields.TypedField("Type", String)
