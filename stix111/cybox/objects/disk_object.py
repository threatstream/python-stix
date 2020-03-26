# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import entities, fields

import stix111.cybox.bindings.disk_object as disk_binding
from stix111.cybox.objects.disk_partition_object import DiskPartition
from stix111.cybox.common import ObjectProperties, String, UnsignedLong


class PartitionList(entities.EntityList):
    _binding = disk_binding
    _binding_class = disk_binding.PartitionListType
    _namespace = "http://cybox.mitre.org/objects#DiskObject-2"

    partition = fields.TypedField("Partition", DiskPartition, multiple=True)


class Disk(ObjectProperties):
    _binding = disk_binding
    _binding_class = disk_binding.DiskObjectType
    _namespace = "http://cybox.mitre.org/objects#DiskObject-2"
    _XSI_NS = "DiskObj"
    _XSI_TYPE = "DiskObjectType"

    disk_name = fields.TypedField('Disk_Name', String)
    disk_size = fields.TypedField('Disk_Size', UnsignedLong)
    free_space = fields.TypedField('Free_Space', UnsignedLong)
    partition_list = fields.TypedField('Partition_List', PartitionList)
    type_ = fields.TypedField('Type', String)
