# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from stix111.cybox.core import Observables

# internal
import stix111
import stix111.bindings.ttp as ttp_binding
from stix111.common import vocabs
from stix111.common.identity import Identity, IdentityFactory
from stix111.mixbox import fields


class VictimTargeting(stix111.Entity):
    _binding = ttp_binding
    _binding_class = _binding.VictimTargetingType
    _namespace = "http://stix.mitre.org/TTP-1"

    identity = fields.TypedField("Identity", Identity, factory=IdentityFactory)
    targeted_systems = vocabs.VocabField("Targeted_Systems", vocabs.SystemType, multiple=True)
    targeted_information = vocabs.VocabField("Targeted_Information", vocabs.InformationType, multiple=True)
    targeted_technical_details = fields.TypedField("Targeted_Technical_Details", Observables)

    def __init__(self):
        super(VictimTargeting, self).__init__()

    def add_targeted_system(self, system):
        self.targeted_systems.append(system)

    def add_targeted_information(self, targeted_information):
        self.targeted_information.append(targeted_information)
