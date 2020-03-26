#MAEC Action Reference List Class

#Copyright (c) 2018, The MITRE Corporation
#All rights reserved

from cybox.core import ActionReference

import stix111.maec
from . import _namespace
import stix111.maec.bindings.maec_bundle as bundle_binding
from stix111.mixbox import fields

class ActionReferenceList(maec.EntityList):
    _binding_class = bundle_binding.ActionReferenceListType
    _namespace = _namespace
    action_reference = fields.TypedField("Action_Reference", ActionReference, multiple=True)
