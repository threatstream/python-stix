# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix111
from stix111.xmlconst import TAG_STIX_PACKAGE

import stix111.mixbox.parser
# Import these from stix111.mixbox for backward compatibility
from stix111.mixbox.parser import (UnknownVersionError, UnsupportedVersionError,
                           UnsupportedRootElementError)

# Alias for backwards compatibility
UnsupportedRootElement = UnsupportedRootElementError


class EntityParser(stix111.mixbox.parser.EntityParser):

    def supported_tags(self):
        return [TAG_STIX_PACKAGE]

    def get_version(self, root):
        return root.attrib.get('version')

    def supported_versions(self, tag=TAG_STIX_PACKAGE):
        return stix111.supported_stix_version()

    def get_entity_class(self, tag=TAG_STIX_PACKAGE):
        return stix111.core.STIXPackage