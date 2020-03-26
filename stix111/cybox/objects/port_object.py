# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.port_object as port_binding
from stix111.cybox.common import ObjectProperties, String, PositiveInteger


class Port(ObjectProperties):
    _binding = port_binding
    _binding_class = port_binding.PortObjectType
    _namespace = 'http://cybox.mitre.org/objects#PortObject-2'
    _XSI_NS = "PortObj"
    _XSI_TYPE = "PortObjectType"

    port_value = fields.TypedField("Port_Value", PositiveInteger)
    layer4_protocol = fields.TypedField("Layer4_Protocol", String)
