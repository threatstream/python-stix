# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import unittest

from stix111.cybox.utils.normalize import normalize_object_properties
from stix111.cybox.objects.file_object import File
from stix111.cybox.objects.win_registry_key_object import WinRegistryKey, RegistryValues, RegistryValue
from stix111.cybox.objects.process_object import Process, ImageInfo
from stix111.cybox.objects.mutex_object import Mutex

class TestNormalization(unittest.TestCase):

    def test_file_path(self):
        file_path_string = "%WinDir%\abcd.dll"
        normalized_file_path_string = "CSIDL_WINDOWS\abcd.dll"

        file_obj = File()
        file_obj.file_path = file_path_string

        normalize_object_properties(file_obj)

        self.assertEqual(file_obj.file_path.value, normalized_file_path_string)

    def test_registry_value_data(self):
        file_path_string = "C:"
        normalized_file_path_string = "%SystemDrive%"

        registry_key_obj = WinRegistryKey()
        registry_key_obj.values = RegistryValues()
        registry_value = RegistryValue()
        registry_value.data = file_path_string
        registry_key_obj.values.append(registry_value)

        normalize_object_properties(registry_key_obj)

        self.assertEqual(registry_key_obj.values[0].data.value, normalized_file_path_string)

    def test_registry_hive(self):
        hive_string = "HKLM"
        normalized_hive_string = "HKEY_LOCAL_MACHINE"

        registry_key_obj = WinRegistryKey()
        registry_key_obj.hive = hive_string

        normalize_object_properties(registry_key_obj)

        self.assertEqual(registry_key_obj.hive.value, normalized_hive_string)
        
    def test_process_image_info_path(self):
        file_path_string = "C:\Windows\System32\abcd.dll"
        normalized_file_path_string = "CSIDL_SYSTEM\abcd.dll"

        process_obj = Process()
        process_obj.image_info = ImageInfo()
        process_obj.image_info.path = file_path_string

        normalize_object_properties(process_obj)

        self.assertEqual(process_obj.image_info.path.value, normalized_file_path_string)

if __name__ == "__main__":
    unittest.main()
