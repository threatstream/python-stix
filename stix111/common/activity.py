# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix111
import stix111.bindings.stix_common as common_binding
import stix111.utils

from .datetimewithprecision import DateTimeWithPrecision
from .structured_text import StructuredText


class Activity(stix111.Entity):
    _binding = common_binding
    _binding_class = common_binding.ActivityType
    _namespace = 'http://stix.mitre.org/common-1'

    date_time = fields.TypedField("Date_Time", DateTimeWithPrecision)
    description = fields.TypedField("Description", StructuredText)

    def __init__(self):
        super(Activity, self).__init__()
