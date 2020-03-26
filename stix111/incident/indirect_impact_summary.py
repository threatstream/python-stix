# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111
import stix111.bindings.incident as incident_binding
from stix111.common import vocabs, VocabString


class IndirectImpactSummary(stix111.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.IndirectImpactSummaryType

    loss_of_competitive_advantage = vocabs.VocabField("Loss_Of_Competitive_Advantage", vocabs.SecurityCompromise)
    brand_and_market_damage = vocabs.VocabField("Brand_And_Market_Damage", vocabs.SecurityCompromise)
    increased_operating_costs = vocabs.VocabField("Increased_Operating_Costs", vocabs.SecurityCompromise)
    legal_and_regulatory_costs = vocabs.VocabField("Legal_And_Regulatory_Costs", vocabs.SecurityCompromise)

    def __init__(self):
        super(IndirectImpactSummary, self).__init__()
