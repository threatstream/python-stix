# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.link_object as link_binding
from stix111.cybox.objects.uri_object import URI
from stix111.cybox.common import String


class Link(URI):
    _binding = link_binding
    _binding_class = link_binding.LinkObjectType
    _namespace = "http://cybox.mitre.org/objects#LinkObject-1"
    _XSI_NS = "LinkObj"
    _XSI_TYPE = "LinkObjectType"

    url_label = fields.TypedField("URL_Label", String)
