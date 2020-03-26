#MAEC Bundle Reference Class

#Copyright (c) 2018, The MITRE Corporation
#All rights reserved

from stix111.mixbox import fields

import stix111.maec
from . import _namespace
import stix111.maec.bindings.maec_bundle as bundle_binding

class BundleReference(stix111.maec.Entity):
    _namespace = _namespace
    _binding = bundle_binding
    _binding_class = bundle_binding.BundleReferenceType

    bundle_idref = fields.TypedField("bundle_idref")

    def __init__(self, bundle_idref = None):
        super(BundleReference, self).__init__()
        self.bundle_idref = bundle_idref
