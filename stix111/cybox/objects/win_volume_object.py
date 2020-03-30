# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import entities, fields

import stix111.cybox.bindings.win_volume_object as win_volume_binding
from stix111.cybox.objects.volume_object import Volume
from stix111.cybox.common import String


class WindowsVolumeAttributesList(entities.EntityList):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeAttributesListType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"

    attribute = fields.TypedField("Attribute", String, multiple=True)


class WinVolume(Volume):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeObjectType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"
    _XSI_NS = "WinVolumeObj"
    _XSI_TYPE = "WindowsVolumeObjectType"

    attributes_list = fields.TypedField("Attributes_List", WindowsVolumeAttributesList)
    drive_letter = fields.TypedField("Drive_Letter", String)
    drive_type = fields.TypedField("Drive_Type", String)