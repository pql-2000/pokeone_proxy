# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HeightTile.proto

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
  name='HeightTile.proto',
  package='MAPAPI.Response12',
  syntax='proto2',
  serialized_pb=_b('\n\x10HeightTile.proto\x12\x11MAPAPI.Response12\"C\n\x12HeightChangeStruct\x12\x0c\n\x01X\x18\x01 \x01(\x05:\x01\x30\x12\x0c\n\x01Y\x18\x02 \x01(\x05:\x01\x30\x12\x11\n\x06Height\x18\x03 \x01(\x05:\x01\x30\"U\n\nHeightTile\x12\x11\n\x06Height\x18\x01 \x01(\x05:\x01\x30\x12\x34\n\x05Tiles\x18\x02 \x03(\x0b\x32%.MAPAPI.Response12.HeightChangeStruct')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HEIGHTCHANGESTRUCT = _descriptor.Descriptor(
  name='HeightChangeStruct',
  full_name='MAPAPI.Response12.HeightChangeStruct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='X', full_name='MAPAPI.Response12.HeightChangeStruct.X', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Y', full_name='MAPAPI.Response12.HeightChangeStruct.Y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Height', full_name='MAPAPI.Response12.HeightChangeStruct.Height', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=39,
  serialized_end=106,
)


_HEIGHTTILE = _descriptor.Descriptor(
  name='HeightTile',
  full_name='MAPAPI.Response12.HeightTile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Height', full_name='MAPAPI.Response12.HeightTile.Height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Tiles', full_name='MAPAPI.Response12.HeightTile.Tiles', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=108,
  serialized_end=193,
)

_HEIGHTTILE.fields_by_name['Tiles'].message_type = _HEIGHTCHANGESTRUCT
DESCRIPTOR.message_types_by_name['HeightChangeStruct'] = _HEIGHTCHANGESTRUCT
DESCRIPTOR.message_types_by_name['HeightTile'] = _HEIGHTTILE

HeightChangeStruct = _reflection.GeneratedProtocolMessageType('HeightChangeStruct', (_message.Message,), dict(
  DESCRIPTOR = _HEIGHTCHANGESTRUCT,
  __module__ = 'HeightTile_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response12.HeightChangeStruct)
  ))
_sym_db.RegisterMessage(HeightChangeStruct)

HeightTile = _reflection.GeneratedProtocolMessageType('HeightTile', (_message.Message,), dict(
  DESCRIPTOR = _HEIGHTTILE,
  __module__ = 'HeightTile_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response12.HeightTile)
  ))
_sym_db.RegisterMessage(HeightTile)


# @@protoc_insertion_point(module_scope)