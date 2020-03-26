# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111
from stix111.common import StructuredText, Confidence
import stix111.bindings.course_of_action as coa_binding


class Objective(stix111.Entity):
    _binding = coa_binding
    _binding_class = coa_binding.ObjectiveType
    _namespace = "http://stix.mitre.org/CourseOfAction-1"

    applicability_confidence = fields.TypedField("Applicability_Confidence", Confidence)
    description = fields.TypedField("Description", StructuredText)
    short_description = fields.TypedField("Short_Description", StructuredText)

    def __init__(self, description=None, short_description=None):
        super(Objective, self).__init__()

        self.description = description
        self.short_description = short_description
