# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from stix111.mixbox import fields

import stix111.cybox.bindings.image_file_object as image_binding
from stix111.cybox.common import String, Integer, PositiveInteger
from stix111.cybox.objects.file_object import File


class ImageFile(File):
    _binding = image_binding
    _binding_class = image_binding.ImageFileObjectType
    _namespace = 'http://cybox.mitre.org/objects#ImageFileObject-1'
    _XSI_NS = "ImageFileObj"
    _XSI_TYPE = "ImageFileObjectType"

    image_is_compressed = fields.TypedField("image_is_compressed")
    image_file_format = fields.TypedField("Image_File_Format", String)
    image_height = fields.TypedField("Image_Height", Integer)
    image_width = fields.TypedField("Image_Width", Integer)
    bits_per_pixel = fields.TypedField("Bits_Per_Pixel", PositiveInteger)
    compression_algorithm = fields.TypedField("Compression_Algorithm", String)
