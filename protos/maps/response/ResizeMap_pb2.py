# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ResizeMap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ResizeMap.proto',
  package='MAPAPI.Response33',
  syntax='proto2',
  serialized_pb=_b('\n\x0fResizeMap.proto\x12\x11MAPAPI.Response33\"0\n\tResizeMap\x12\x10\n\x05width\x18\x01 \x01(\x05:\x01\x30\x12\x11\n\x06height\x18\x02 \x01(\x05:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESIZEMAP = _descriptor.Descriptor(
  name='ResizeMap',
  full_name='MAPAPI.Response33.ResizeMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='MAPAPI.Response33.ResizeMap.width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='MAPAPI.Response33.ResizeMap.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['ResizeMap'] = _RESIZEMAP

ResizeMap = _reflection.GeneratedProtocolMessageType('ResizeMap', (_message.Message,), dict(
  DESCRIPTOR = _RESIZEMAP,
  __module__ = 'ResizeMap_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response33.ResizeMap)
  ))
_sym_db.RegisterMessage(ResizeMap)


# @@protoc_insertion_point(module_scope)