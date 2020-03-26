# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111
import stix111.bindings.incident as incident_binding


class LossEstimation(stix111.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.LossEstimationType

    iso_currency_code = fields.TypedField("iso_currency_code")
    amount = fields.TypedField("amount")

    def __init__(self):
        super(LossEstimation, self).__init__()
