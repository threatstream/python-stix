# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import entities, fields

import stix111.cybox.bindings.cybox_common as common_binding
from stix111.cybox.common import DateWithPrecision


class DateRange(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateRangeType
    _namespace = 'http://cybox.mitre.org/common-2'

    start_date = fields.TypedField("Start_Date", DateWithPrecision)
    end_date = fields.TypedField("End_Date", DateWithPrecision)
