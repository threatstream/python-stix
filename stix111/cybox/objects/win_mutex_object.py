# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.win_mutex_object as win_mutex_binding
from stix111.cybox.objects.mutex_object import Mutex
from stix111.cybox.objects.win_handle_object import WinHandle
from stix111.cybox.common import String


class WinMutex(Mutex):
    _binding = win_mutex_binding
    _binding_class = win_mutex_binding.WindowsMutexObjectType
    _namespace = "http://cybox.mitre.org/objects#WinMutexObject-2"
    _XSI_NS = "WinMutexObj"
    _XSI_TYPE = "WindowsMutexObjectType"

    handle = fields.TypedField("Handle", WinHandle)
    security_attributes = fields.TypedField("Security_Attributes", String)
