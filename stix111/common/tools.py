# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from stix111.mixbox import fields

import stix111.cybox.common
from stix111.cybox.common.vocabs import VocabField

# internal
import stix111
import stix111.bindings.stix_common as common_binding

# relative
from .structured_text import StructuredText
from .vocabs import AttackerToolType


class ToolInformation(stix111.Entity, stix111.cybox.common.ToolInformation):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ToolInformationType

    title = fields.TypedField("Title")
    short_description = fields.TypedField("Short_Description", StructuredText)
    type_ = VocabField("Type", AttackerToolType, multiple=True)

    def __init__(self, title=None, short_description=None, tool_name=None,
                 tool_vendor=None):

        super(ToolInformation, self).__init__(
            tool_name=tool_name,
            tool_vendor=tool_vendor
        )

        self.title = title
        self.short_description = short_description
