# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import entities, fields

import stix111.cybox.bindings.dns_cache_object as dns_cache_binding
from stix111.cybox.common import ObjectProperties, PositiveInteger
from stix111.cybox.objects.dns_record_object import DNSRecord


class DNSCacheEntry(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#DNSCacheObject-2"
    _binding = dns_cache_binding
    _binding_class = dns_cache_binding.DNSCacheEntryType

    dns_entry = fields.TypedField("DNS_Entry", DNSRecord)
    ttl = fields.TypedField("TTL", PositiveInteger)


class DNSCache(ObjectProperties):
    _binding = dns_cache_binding
    _binding_class = dns_cache_binding.DNSCacheObjectType
    _namespace = "http://cybox.mitre.org/objects#DNSCacheObject-2"
    _XSI_NS = "DNSCacheObj"
    _XSI_TYPE = "DNSCacheObjectType"

    dns_cache_entry = fields.TypedField("DNS_Cache_Entry", DNSCacheEntry, multiple=True)
