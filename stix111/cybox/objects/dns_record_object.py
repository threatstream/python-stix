# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.dns_record_object as dns_record_binding
from stix111.cybox.common import (Integer, HexBinary, ObjectProperties, String,
        StructuredText, DateTime)
from stix111.cybox.objects.address_object import Address
from stix111.cybox.objects.uri_object import URI


class DNSRecord(ObjectProperties):
    _binding = dns_record_binding
    _binding_class = dns_record_binding.DNSRecordObjectType
    _namespace = 'http://cybox.mitre.org/objects#DNSRecordObject-2'
    _XSI_NS = "DNSRecordObj"
    _XSI_TYPE = "DNSRecordObjectType"

    description = fields.TypedField("Description", StructuredText)
    domain_name = fields.TypedField("Domain_Name", URI)
    queried_date = fields.TypedField("Queried_Date", DateTime)
    ip_address = fields.TypedField("IP_Address", Address)
    address_class = fields.TypedField("Address_Class", String)
    entry_type = fields.TypedField("Entry_Type", String)
    record_name = fields.TypedField("Record_Name", String)
    record_type = fields.TypedField("Record_Type", String)
    ttl = fields.TypedField("TTL", Integer)
    flags = fields.TypedField("Flags", HexBinary)
    data_length = fields.TypedField("Data_Length", Integer)
    record_data = fields.TypedField("Record_Data")
