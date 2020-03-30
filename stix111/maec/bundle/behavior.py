# MAEC Behavior Class

# Copyright (c) 2018, The MITRE Corporation
# All rights reserved

from stix111.mixbox import fields
from stix111.mixbox import idgen

import stix111.maec
from . import _namespace
import stix111.maec.bindings.maec_bundle as bundle_binding
from stix111.cybox.core.action_reference import ActionReference
from stix111.cybox.common.measuresource import MeasureSource
from stix111.cybox.common.platform_specification import PlatformSpecification
from stix111.cybox.objects.code_object import Code

class BehavioralActionEquivalenceReference(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.BehavioralActionEquivalenceReferenceType
    _namespace = _namespace

    action_equivalence_idref = fields.TypedField('action_equivalence_idref')
    behavioral_ordering = fields.TypedField('behavioral_ordering')

class BehavioralActionReference(ActionReference):
    _binding = bundle_binding
    _binding_class = bundle_binding.BehavioralActionReferenceType
    _namespace = _namespace

    behavioral_ordering = fields.TypedField('behavioral_ordering')

class BehavioralAction(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.BehavioralActionType
    _namespace = _namespace

    behavioral_ordering = fields.TypedField('behavioral_ordering')

class BehavioralActions(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.BehavioralActionsType
    _namespace = _namespace

    #TODO: action_collection.type_ is set below to avoid circular import.
    action_collection = fields.TypedField('Action_Collection', None, multiple=True)
    action = fields.TypedField('Action', BehavioralAction, multiple=True)
    action_reference = fields.TypedField('Action_Reference', BehavioralActionReference, multiple=True)
    action_equivalence_reference = fields.TypedField('Action_Equivalence_Reference', BehavioralActionEquivalenceReference, multiple=True)

class PlatformList(stix111.maec.EntityList):
    _binding = bundle_binding
    _binding_class = bundle_binding.PlatformListType
    _namespace = _namespace
    platform = fields.TypedField("Platform", PlatformSpecification, multiple=True)

class CVEVulnerability(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.CVEVulnerabilityType
    _namespace = _namespace

    cve_id = fields.TypedField('cve_id')
    description = fields.TypedField('Description')

class Exploit(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.ExploitType
    _namespace = _namespace

    known_vulnerability = fields.TypedField('known_vulnerability')
    cve = fields.TypedField('CVE', CVEVulnerability)
    cwe_id = fields.TypedField('CWE_ID', multiple=True)
    targeted_platforms = fields.TypedField('Targeted_Platforms', PlatformList)

class BehaviorPurpose(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.BehaviorPurposeType
    _namespace = _namespace

    description = fields.TypedField('Description')
    vulnerability_exploit = fields.TypedField('Vulnerability_Exploit', Exploit)

class AssociatedCode(stix111.maec.EntityList):
    _binding = bundle_binding
    _binding_class = bundle_binding.AssociatedCodeType
    _namespace = _namespace
    code_snippet = fields.TypedField("Code_Snippet", Code, multiple=True)

class Behavior(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.BehaviorType
    _namespace = _namespace

    id_ = fields.TypedField('id')
    ordinal_position = fields.TypedField('ordinal_position')
    status = fields.TypedField('status')
    duration = fields.TypedField('duration')
    purpose = fields.TypedField('Purpose', BehaviorPurpose)
    description = fields.TypedField('Description')
    discovery_method = fields.TypedField('Discovery_Method', MeasureSource)
    action_composition = fields.TypedField('Action_Composition', BehavioralActions)
    associated_code = fields.TypedField('Associated_Code', AssociatedCode)
    #relationships = fields.TypedField('Relationships', BehaviorRelationshipList) # TODO: implement

    def __init__(self, id = None, description = None):
        super(Behavior, self).__init__()
        if id:
            self.id_ = id
        else:
            self.id_ = idgen.create_id(prefix="behavior")
        self.description = description


from stix111.maec.bundle.bundle import ActionCollection
BehavioralActions.action_collection.type_ = ActionCollection