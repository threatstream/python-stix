# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.pipe_object as pipe_binding
from stix111.cybox.common import ObjectProperties, String


class Pipe(ObjectProperties):
    _namespace = 'http://cybox.mitre.org/objects#PipeObject-2'
    _XSI_NS = "PipeObj"
    _XSI_TYPE = "PipeObjectType"
    _binding = pipe_binding
    _binding_class = pipe_binding.PipeObjectType

    name = fields.TypedField("Name", String)
    named = fields.TypedField("named")
