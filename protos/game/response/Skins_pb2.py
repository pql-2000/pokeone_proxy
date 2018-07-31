# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Skins.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Skins.proto',
  package='PSXAPI_Response12425156163',
  syntax='proto2',
  serialized_pb=_b('\n\x0bSkins.proto\x12\x1aPSXAPI_Response12425156163\"\x99\x01\n\x04Skin\x12?\n\x06\x41\x63tion\x18\x01 \x01(\x0e\x32&.PSXAPI_Response12425156163.SkinAction:\x07__None0\x12;\n\x04Type\x18\x02 \x01(\x0e\x32$.PSXAPI_Response12425156163.SkinType:\x07__None1\x12\x13\n\x08SpriteID\x18\x03 \x01(\x05:\x01\x30\"6\n\x05Skins\x12-\n\x03\x41ll\x18\x01 \x03(\x0b\x32 .PSXAPI_Response12425156163.Skin*\"\n\nSkinAction\x12\x0b\n\x07__None0\x10\x00\x12\x07\n\x03\x41\x64\x64\x10\x01*J\n\x08SkinType\x12\x0b\n\x07__None1\x10\x00\x12\n\n\x06\x43lothe\x10\x01\x12\x07\n\x03Hat\x10\x02\x12\t\n\x05Mount\x10\x03\x12\x08\n\x04Surf\x10\x04\x12\x07\n\x03\x46ly\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_SKINACTION = _descriptor.EnumDescriptor(
  name='SkinAction',
  full_name='PSXAPI_Response12425156163.SkinAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Add', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=255,
  serialized_end=289,
)
_sym_db.RegisterEnumDescriptor(_SKINACTION)

SkinAction = enum_type_wrapper.EnumTypeWrapper(_SKINACTION)
_SKINTYPE = _descriptor.EnumDescriptor(
  name='SkinType',
  full_name='PSXAPI_Response12425156163.SkinType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Clothe', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Hat', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mount', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Surf', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Fly', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=291,
  serialized_end=365,
)
_sym_db.RegisterEnumDescriptor(_SKINTYPE)

SkinType = enum_type_wrapper.EnumTypeWrapper(_SKINTYPE)
__None0 = 0
Add = 1
__None1 = 0
Clothe = 1
Hat = 2
Mount = 3
Surf = 4
Fly = 5



_SKIN = _descriptor.Descriptor(
  name='Skin',
  full_name='PSXAPI_Response12425156163.Skin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI_Response12425156163.Skin.Action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Type', full_name='PSXAPI_Response12425156163.Skin.Type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpriteID', full_name='PSXAPI_Response12425156163.Skin.SpriteID', index=2,
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
  serialized_start=44,
  serialized_end=197,
)


_SKINS = _descriptor.Descriptor(
  name='Skins',
  full_name='PSXAPI_Response12425156163.Skins',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='All', full_name='PSXAPI_Response12425156163.Skins.All', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=199,
  serialized_end=253,
)

_SKIN.fields_by_name['Action'].enum_type = _SKINACTION
_SKIN.fields_by_name['Type'].enum_type = _SKINTYPE
_SKINS.fields_by_name['All'].message_type = _SKIN
DESCRIPTOR.message_types_by_name['Skin'] = _SKIN
DESCRIPTOR.message_types_by_name['Skins'] = _SKINS
DESCRIPTOR.enum_types_by_name['SkinAction'] = _SKINACTION
DESCRIPTOR.enum_types_by_name['SkinType'] = _SKINTYPE

Skin = _reflection.GeneratedProtocolMessageType('Skin', (_message.Message,), dict(
  DESCRIPTOR = _SKIN,
  __module__ = 'Skins_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI_Response12425156163.Skin)
  ))
_sym_db.RegisterMessage(Skin)

Skins = _reflection.GeneratedProtocolMessageType('Skins', (_message.Message,), dict(
  DESCRIPTOR = _SKINS,
  __module__ = 'Skins_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI_Response12425156163.Skins)
  ))
_sym_db.RegisterMessage(Skins)


# @@protoc_insertion_point(module_scope)