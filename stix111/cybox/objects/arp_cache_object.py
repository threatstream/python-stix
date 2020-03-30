# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import entities, fields

import stix111.cybox.bindings.arp_cache_object as arp_binding
from stix111.cybox.objects.address_object import Address
from stix111.cybox.objects.system_object import NetworkInterface
from stix111.cybox.common import ObjectProperties, String


class ARPCacheEntry(entities.Entity):
    _binding = arp_binding
    _binding_class = arp_binding.ARPCacheEntryType
    _namespace = "http://cybox.mitre.org/objects#ARPCacheObject-1"

    ip_address = fields.TypedField("IP_Address", Address)
    physical_address = fields.TypedField("Physical_Address", String)
    type_ = fields.TypedField("Type", String)
    network_interface = fields.TypedField("Network_Interface", NetworkInterface)


class ARPCache(ObjectProperties):
    _binding = arp_binding
    _binding_class = arp_binding.ARPCacheObjectType
    _namespace = "http://cybox.mitre.org/objects#ARPCacheObject-1"
    _XSI_NS = "ARPCacheObj"
    _XSI_TYPE = "ARPCacheObjectType"

    arp_cache_entry = fields.TypedField("ARP_Cache_Entry", ARPCacheEntry, multiple=True)