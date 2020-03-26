# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


class UnknownObjectType(Exception):
    pass


def get_class_for_object_type(object_type):
    return _OBJ_META.get_class_for_object_type(object_type)


class _ObjectType(object):

    def __init__(self, name, api_class, binding, namespace, dependencies):
        """Create a new namespace.

        Arguments (all strings)
        - name: the name of the Object
        - api_class: The fully qualified name of the class that implements
          the Object
        - binding: the name of the binding containing the Object
        - namespace: the namespace where the Object is defined
        - dependencies: a list of strings, where each string is another
          ObjectType
        """
        self.name = name
        self.api_class = api_class
        self.binding = binding
        self.namespace = namespace
        self.dependencies = dependencies


class _ObjectMetadata(object):
    """Metadata about CybOX objects."""

    def __init__(self, object_list):
        self._obj_dict = {}

        for obj in object_list:
            o = _ObjectType(*obj)
            self.add_object(o)

    def add_object(self, object_type):
        # TODO: are there other ways we want to look up this data?
        self._obj_dict[object_type.name] = object_type

    def lookup_object(self, object_name):
        return self._obj_dict.get(object_name)

    def get_class_for_object_type(self, object_type):
        """Gets the class where a given XML Type can be parsed.

        Each ObjectType instance should define a member api_class, which
        consists of a fully-qualified name of a class (including the module it
        is defined in).

        Arguments:
        - object_type: a string

        Raises:
        - UnknownObjectType, if object_type has not been defined in obj_list.
        - ImportError, if the specified module is not available.
        - AttributeError, if the module does not contain the given class.
        """
        otype = self.lookup_object(object_type)
        if not otype:
            err = "%s is not a known ObjectType" % object_type
            raise UnknownObjectType(err)

        full_class_name = otype.api_class
        if not full_class_name:
            err = "%s does not have a specified API class" % object_type
            raise UnknownObjectType(err)

        module = ".".join(full_class_name.split('.')[:-1])
        class_name = full_class_name.split('.')[-1]

        # May raise ImportError
        mod = __import__(module, fromlist=[class_name])

        # May raise AttributeError
        return getattr(mod, class_name)
# A list of (object_name, api_class, binding, namespace, dependencies) tuples
# This is loaded by the ObjectMetadata class and should not be accessed
# directly.
OBJ_LIST = [
    ('AccountObjectType', 'stix111.cybox.objects.account_object.Account', 'account_object', 'http://cybox.mitre.org/objects#AccountObject-2', []),
    ('AddressObjectType', 'stix111.cybox.objects.address_object.Address', 'address_object', 'http://cybox.mitre.org/objects#AddressObject-2', []),
    ('APIObjectType', 'stix111.cybox.objects.api_object.API', 'api_object', 'http://cybox.mitre.org/objects#APIObject-2', []),
    ('ArchiveFileObjectType', 'stix111.cybox.objects.archive_file_object.ArchiveFile', 'archive_file_object', 'http://cybox.mitre.org/objects#ArchiveFileObject-1', ['FileObjectType']),
    ('ArtifactObjectType', 'stix111.cybox.objects.artifact_object.Artifact', 'artifact_object', 'http://cybox.mitre.org/objects#ArtifactObject-2', []),
    ('ARPCacheObjectType', 'stix111.cybox.objects.arp_cache_object.ARPCache', 'arp_cache_object', 'http://cybox.mitre.org/objects#ARPCacheObject-1', []),
    ('ASObjectType', 'stix111.cybox.objects.as_object.AS', 'as_object', 'http://cybox.mitre.org/objects#ASObject-1', []),
    ('CodeObjectType', 'stix111.cybox.objects.code_object.Code', 'code_object', 'http://cybox.mitre.org/objects#CodeObject-2', []),
    ('CustomObjectType', 'stix111.cybox.objects.custom_object.Custom', 'custom_object', 'http://cybox.mitre.org/objects#CustomObject-1', []),
    ('DeviceObjectType', 'stix111.cybox.objects.device_object.Device', 'device_object', 'http://cybox.mitre.org/objects#DeviceObject-2', []),
    ('DiskObjectType', 'stix111.cybox.objects.disk_object.Disk', 'disk_object', 'http://cybox.mitre.org/objects#DiskObject-2', ['DiskPartitionObjectType']),
    ('DiskPartitionObjectType', 'stix111.cybox.objects.disk_partition_object.DiskPartition', 'disk_partition_object', 'http://cybox.mitre.org/objects#DiskPartitionObject-2', []),
    ('DNSCacheObjectType', 'stix111.cybox.objects.dns_cache_object.DNSCache', 'dns_cache_object', 'http://cybox.mitre.org/objects#DNSCacheObject-2', ['DNSRecordObjectType', 'AddressObjectType', 'URIObjectType']),
    ('DNSQueryObjectType', 'stix111.cybox.objects.dns_query_object.DNSQuery', 'dns_query_object', 'http://cybox.mitre.org/objects#DNSQueryObject-2', ['DNSRecordObjectType', 'URIObjectType', 'AddressObjectType']),
    ('DNSRecordObjectType', 'stix111.cybox.objects.dns_record_object.DNSRecord', 'dns_record_object', 'http://cybox.mitre.org/objects#DNSRecordObject-2', ['URIObjectType', 'AddressObjectType']),
    ('DomainNameObjectType', 'stix111.cybox.objects.domain_name_object.DomainName', 'domain_name_object', 'http://cybox.mitre.org/objects#DomainNameObject-1', []),
    ('EmailMessageObjectType', 'stix111.cybox.objects.email_message_object.EmailMessage', 'email_message_object', 'http://cybox.mitre.org/objects#EmailMessageObject-2', ['FileObjectType', 'AddressObjectType', 'URIObjectType']),
    ('FileObjectType', 'stix111.cybox.objects.file_object.File', 'file_object', 'http://cybox.mitre.org/objects#FileObject-2', []),
    ('GUIDialogboxObjectType', 'stix111.cybox.objects.gui_dialogbox_object.GUIDialogbox', 'gui_dialogbox_object', 'http://cybox.mitre.org/objects#GUIDialogboxObject-2', ['GUIObjectType']),
    ('GUIObjectType', 'stix111.cybox.objects.gui_object.GUI', 'gui_object', 'http://cybox.mitre.org/objects#GUIObject-2', []),
    ('GUIWindowObjectType', 'stix111.cybox.objects.gui_window_object.GUIWindow', 'gui_window_object', 'http://cybox.mitre.org/objects#GUIWindowObject-2', ['GUIObjectType']),
    ('HostnameObjectType', 'stix111.cybox.objects.hostname_object.Hostname', 'hostname_object', 'http://cybox.mitre.org/objects#HostnameObject-1', []),
    ('HTTPSessionObjectType', 'stix111.cybox.objects.http_session_object.HTTPSession', 'http_session_object', 'http://cybox.mitre.org/objects#HTTPSessionObject-2', ['AddressObjectType', 'PortObjectType', 'URIObjectType']),
    ('ImageFileObjectType', 'stix111.cybox.objects.image_file_object.ImageFile', 'image_file_object', 'http://cybox.mitre.org/objects#ImageFileObject-1', ['FileObjectType']),
    ('LibraryObjectType', 'stix111.cybox.objects.library_object.Library', 'library_object', 'http://cybox.mitre.org/objects#LibraryObject-2', []),
    ('LinkObjectType', 'stix111.cybox.objects.link_object.Link', 'link_object', 'http://cybox.mitre.org/objects#LinkObject-1', ['URIObjectType']),
    ('LinuxPackageObjectType', 'stix111.cybox.objects.linux_package_object.LinuxPackage', 'linux_package_object', 'http://cybox.mitre.org/objects#LinuxPackageObject-2', []),
    ('MemoryObjectType', 'stix111.cybox.objects.memory_object.Memory', 'memory_object', 'http://cybox.mitre.org/objects#MemoryObject-2', []),
    ('MutexObjectType', 'stix111.cybox.objects.mutex_object.Mutex', 'mutex_object', 'http://cybox.mitre.org/objects#MutexObject-2', []),
    ('NetRouteObjectType', 'stix111.cybox.objects.network_route_object.NetRoute', 'network_route_object', 'http://cybox.mitre.org/objects#NetworkRouteObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('NetworkConnectionObjectType', 'stix111.cybox.objects.network_connection_object.NetworkConnection', 'network_connection_object', 'http://cybox.mitre.org/objects#NetworkConnectionObject-2', ['SocketAddressObjectType', 'HTTPSessionObjectType', 'DNSQueryObjectType', 'DNSRecordObjectType', 'URIObjectType']),
    ('NetworkFlowObjectType', None, 'network_flow_object', 'http://cybox.mitre.org/objects#NetworkFlowObject-2', ['NetworkPacketType', 'AddressObjectType', 'SocketAddressObjectType']),
    ('NetworkPacketObjectType', 'stix111.cybox.objects.network_packet_object.NetworkPacket', 'network_packet_object', 'http://cybox.mitre.org/objects#PacketObject-2', ['AddressObjectType', 'PortObjectType']),
    ('NetworkRouteEntryObjectType', 'stix111.cybox.objects.network_route_entry_object.NetworkRouteEntry', 'network_route_entry_object', 'http://cybox.mitre.org/objects#NetworkRouteEntryObject-2', ['AddressObjectType']),
    ('NetworkSocketObjectType', 'stix111.cybox.objects.network_socket_object.NetworkSocket', 'network_socket_object', 'http://cybox.mitre.org/objects#NetworkSocketObject-2', ['SocketAddressObjectType']),
    ('NetworkSubnetObjectType', 'stix111.cybox.objects.network_subnet_object.NetworkSubnet', 'network_subnet_object', 'http://cybox.mitre.org/objects#NetworkSubnetObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('PDFFileObjectType', 'stix111.cybox.objects.pdf_file_object.PDFFile', 'pdf_file_object', 'http://cybox.mitre.org/objects#PDFFileObject-1', ['FileObjectType']),
    ('PipeObjectType', 'stix111.cybox.objects.pipe_object.Pipe', 'pipe_object', 'http://cybox.mitre.org/objects#PipeObject-2', []),
    ('PortObjectType', 'stix111.cybox.objects.port_object.Port', 'port_object', 'http://cybox.mitre.org/objects#PortObject-2', []),
    ('ProcessObjectType', 'stix111.cybox.objects.process_object.Process', 'process_object', 'http://cybox.mitre.org/objects#ProcessObject-2', ['NetworkConnectionObjectType', 'PortObjectType']),
    ('ProductObjectType', 'stix111.cybox.objects.product_object.Product', 'product_object', 'http://cybox.mitre.org/objects#ProductObject-2', []),
    ('SemaphoreObjectType', 'stix111.cybox.objects.semaphore_object.Semaphore', 'semaphore_object', 'http://cybox.mitre.org/objects#SemaphoreObject-2', []),
    ('SMSMessageObjectType', 'stix111.cybox.objects.sms_message_object.SMSMessage', 'sms_message_object', 'http://cybox.mitre.org/objects#SMSMessageObject-1', []),
    ('SocketAddressObjectType', 'stix111.cybox.objects.socket_address_object.SocketAddress', 'socket_address_object', 'http://cybox.mitre.org/objects#SocketAddressObject-1', ['AddressObjectType', 'PortObjectType']),
    ('SystemObjectType', 'stix111.cybox.objects.system_object.System', 'system_object', 'http://cybox.mitre.org/objects#SystemObject-2', ['AddressObjectType']),
    ('UnixFileObjectType', None, 'unix_file_object', 'http://cybox.mitre.org/objects#UnixFileObject-2', ['FileObjectType']),
    ('UnixNetworkRouteEntryObjectType', None, 'unix_network_route_entry_object', 'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('UnixPipeObjectType', None, 'unix_pipe_object', 'http://cybox.mitre.org/objects#UnixPipeObject', ['PipeObjectType']),
    ('UnixProcessObjectType', None, 'unix_process_object', 'http://cybox.mitre.org/objects#UnixProcessObject-2', ['ProcessObjectType', 'AddressObjectType', 'PortObjectType']),
    ('UnixUserAccountObjectType', 'stix111.cybox.objects.unix_user_account_object.UnixUserAccount', 'unix_user_account_object', 'http://cybox.mitre.org/objects#UnixUserAccountObject-2', ['UserAccountObjectType', 'AccountObjectType']),
    ('UnixVolumeObjectType', None, 'unix_volume_object', 'http://cybox.mitre.org/objects#UnixVolumeObject-2', ['VolumeObjectType']),
    ('URIObjectType', 'stix111.cybox.objects.uri_object.URI', 'uri_object', 'http://cybox.mitre.org/objects#URIObject-2', []),
    ('URLHistoryObjectType', None, 'url_history_object', 'http://cybox.mitre.org/objects#URLHistoryObject-1', ['URIObjectType','HostnameObjectType']),
    ('UserAccountObjectType', 'stix111.cybox.objects.user_account_object.UserAccount', 'user_account_object', 'http://cybox.mitre.org/objects#UserAccountObject-2', ['AccountObjectType']),
    ('VolumeObjectType', 'stix111.cybox.objects.volume_object.Volume', 'volume_object', 'http://cybox.mitre.org/objects#VolumeObject-2', []),
    ('WhoisObjectType', 'stix111.cybox.objects.whois_object.WhoisEntry', 'whois_object', 'http://cybox.mitre.org/objects#WhoisObject-2', ['URIObjectType', 'AddressObjectType']),
    ('WindowsComputerAccountObjectType', 'stix111.cybox.objects.win_computer_account_object.WinComputerAccount', 'win_computer_account_object', 'http://cybox.mitre.org/objects#WinComputerAccountObject-2', ['AccountObjectType', 'PortObjectType']),
    ('WindowsCriticalSectionObjectType', 'stix111.cybox.objects.win_critical_section_object.WinCriticalSection', 'win_critical_section_object', 'http://cybox.mitre.org/objects#WinCriticalSectionObject-2', []),
    ('WindowsDriverObjectType', 'stix111.cybox.objects.win_driver_object.WinDriver', 'win_driver_object', 'http://cybox.mitre.org/objects#WinDriverObject-3', []),
    ('WindowsEventLogObjectType', 'stix111.cybox.objects.win_event_log_object.WinEventLog', 'win_event_log_object', 'http://cybox.mitre.org/objects#WinEventLogObject-2', []),
    ('WindowsEventObjectType', 'stix111.cybox.objects.win_event_object.WinEvent', 'win_event_object', 'http://cybox.mitre.org/objects#WinEventObject-2', ['WindowsHandleObjectType']),
    ('WindowsExecutableFileObjectType', 'stix111.cybox.objects.win_executable_file_object.WinExecutableFile', 'win_executable_file_object', 'http://cybox.mitre.org/objects#WinExecutableFileObject-2', ['WindowsFileObjectType', 'FileObjectType', 'WinComputerAccountObjectType', 'AccountObjectType', 'PortObjectType']),
    ('WindowsFileObjectType', 'stix111.cybox.objects.win_file_object.WinFile', 'win_file_object', 'http://cybox.mitre.org/objects#WinFileObject-2', ['FileObjectType', 'WinComputerAccountObjectType', 'AccountObjectType', 'PortObjectType']),
    ('WindowsFilemappingObjectType', 'stix111.cybox.objects.win_filemapping_object.WinFilemapping', 'win_filemapping_object', 'http://cybox.mitre.org/objects#WinFilemappingObject-1', ['WindowsHandleObjectType']),
    ('WindowsHandleObjectType', 'stix111.cybox.objects.win_handle_object.WinHandle', 'win_handle_object', 'http://cybox.mitre.org/objects#WinHandleObject-2', []),
    ('WindowsHookObjectType', 'stix111.cybox.objects.win_hook_object.WinHook', 'windows_hook_object', 'http://cybox.mitre.org/objects#WinHookObject-1', ['WindowsHandleObjectType','LibraryObjectType']),
    ('WindowsKernelHookObjectType', 'stix111.cybox.objects.win_kernel_hook_object.WinKernelHook', 'win_kernel_hook_object', 'http://cybox.mitre.org/objects#WinKernelHookObject-2', []),
    ('WindowsKernelObjectType', 'stix111.cybox.objects.win_kernel_object.WinKernel', 'win_kernel_object', 'http://cybox.mitre.org/objects#WinKernelObject-2', []),
    ('WindowsMailslotObjectType', 'stix111.cybox.objects.win_mailslot_object.WinMailslot', 'win_mailslot_object', 'http://cybox.mitre.org/objects#WinMailslotObject-2', ['WindowsHandleObjectType']),
    ('WindowsMemoryPageRegionObjectType', 'stix111.cybox.objects.win_memory_page_region_object.WinMemoryPageRegion', 'win_memory_page_region_object', 'http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2', ['MemoryObjectType']),
    ('WindowsMutexObjectType', 'stix111.cybox.objects.win_mutex_object.WinMutex', 'win_mutex_object', 'http://cybox.mitre.org/objects#WinMutexObject-2', ['WindowsHandleObjectType', 'MutexObjectType']),
    ('WindowsNetworkRouteEntryObjectType', 'stix111.cybox.objects.win_network_route_entry_object.WinNetworkRouteEntry', 'win_network_route_entry_object', 'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('WindowsNetworkShareObjectType', 'stix111.cybox.objects.win_network_share_object.WinNetworkShare', 'win_network_share_object', 'http://cybox.mitre.org/objects#WinNetworkShareObject-2', []),
    ('WindowsPipeObjectType', 'stix111.cybox.objects.win_pipe_object.WinPipe', 'win_pipe_object', 'http://cybox.mitre.org/objects#WinPipeObject-2', ['PipeObjectType']),
    ('WindowsPrefetchObjectType', 'stix111.cybox.objects.win_prefetch_object.WinPrefetch', 'win_prefetch_object', 'http://cybox.mitre.org/objects#WinPrefetchObject-2', ['WindowsVolumeObjectType', 'VolumeObjectType', 'DeviceObjectType']),
    ('WindowsProcessObjectType', 'stix111.cybox.objects.win_process_object.WinProcess', 'win_process_object', 'http://cybox.mitre.org/objects#WinProcessObject-2', ['ProcessObjectType', 'WindowsHandleObjectType', 'MemoryObjectType', 'AddressObjectType', 'PortObjectType']),
    ('WindowsRegistryKeyObjectType', 'stix111.cybox.objects.win_registry_key_object.WinRegistryKey', 'win_registry_key_object', 'http://cybox.mitre.org/objects#WinRegistryKeyObject-2', ['WindowsHandleObjectType']),
    ('WindowsSemaphoreObjectType', 'stix111.cybox.objects.win_semaphore_object.WinSemaphore', 'win_semaphore_object', 'http://cybox.mitre.org/objects#WinSemaphoreObject-2', ['WindowsHandleObjectType', 'SemaphoreObjectType']),
    ('WindowsServiceObjectType', 'stix111.cybox.objects.win_service_object.WinService', 'win_service_object', 'http://cybox.mitre.org/objects#WinServiceObject-2', ['WindowsProcessObjectType', 'WindowsHandleObjectType', 'MemoryObjectType', 'AddressObjectType', 'PortObjectType']),
    ('WindowsSystemObjectType', 'stix111.cybox.objects.win_system_object.WinSystem', 'win_system_object', 'http://cybox.mitre.org/objects#WinSystemObject-2', ['WindowsHandleObjectType', 'SystemObjectType', 'AddressObjectType']),
    ('WindowsSystemRestoreObjectType', 'stix111.cybox.objects.win_system_restore_object.WinSystemRestore', 'win_system_restore_object', 'http://cybox.mitre.org/objects#WinSystemRestoreObject-2', []),
    ('WindowsTaskObjectType', 'stix111.cybox.objects.win_task_object.WinTask', 'win_task_object', 'http://cybox.mitre.org/objects#WinTaskObject-2', ['EmailMessageObjectType', 'FileObjectType', 'AddressObjectType', 'URIObjectType']),
    ('WindowsThreadObjectType', 'stix111.cybox.objects.win_thread_object.WinThread', 'win_thread_object', 'http://cybox.mitre.org/objects#WinThreadObject-2', ['WindowsHandleObjectType']),
    ('WindowsUserAccountObjectType', 'stix111.cybox.objects.win_user_object.WinUser', 'win_user_account_object', 'http://cybox.mitre.org/objects#WinUserAccountObject-2', ['UserAccountObjectType', 'AccountObjectType']),
    ('WindowsVolumeObjectType', 'stix111.cybox.objects.win_volume_object.WinVolume', 'win_volume_object', 'http://cybox.mitre.org/objects#WinVolumeObject-2', ['VolumeObjectType']),
    ('WindowsWaitableTimerObjectType', 'stix111.cybox.objects.win_waitable_timer_object.WinWaitableTimer', 'win_waitable_timer_object', 'http://cybox.mitre.org/objects#WinWaitableTimerObject-2', ['WindowsHandleObjectType']),
    ('X509CertificateObjectType', 'stix111.cybox.objects.x509_certificate_object.X509Certificate', 'x509_certificate_object', 'http://cybox.mitre.org/objects#X509CertificateObject-2', []),
]


_OBJ_META = _ObjectMetadata(OBJ_LIST)
