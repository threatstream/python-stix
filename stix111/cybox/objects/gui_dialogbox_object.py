# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.gui_dialogbox_object as gui_dialogbox_binding
from stix111.cybox.common import String
from stix111.cybox.objects.gui_object import GUI


class GUIDialogbox(GUI):
    _binding = gui_dialogbox_binding
    _binding_class = gui_dialogbox_binding.GUIDialogboxObjectType
    _namespace = "http://cybox.mitre.org/objects#GUIDialogboxObject-2"
    _XSI_NS = "GUIDialogBoxObj"
    _XSI_TYPE = "GUIDialogboxObjectType"

    box_caption = fields.TypedField("Box_Caption", String)
    box_text = fields.TypedField("Box_Text", String)
