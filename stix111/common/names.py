# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields

# internal
import stix111
import stix111.bindings.stix_common as common_binding

# relative
from .vocabs import VocabField


class Names(stix111.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = _binding.NamesType

    name = VocabField("Name", multiple=True)
