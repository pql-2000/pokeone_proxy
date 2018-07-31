# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ZoneItem.proto

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
  name='ZoneItem.proto',
  package='MAPAPI.Response41',
  syntax='proto2',
  serialized_pb=_b('\n\x0eZoneItem.proto\x12\x11MAPAPI.Response41\"T\n\x08ZoneItem\x12\x11\n\x06ItemID\x18\x01 \x01(\x05:\x01\x30\x12\x35\n\nItemRarity\x18\x02 \x01(\x0e\x32\x19.MAPAPI.Response41.Rarity:\x06\x43ommon*Q\n\x06Rarity\x12\n\n\x06\x43ommon\x10\x00\x12\x0c\n\x08Uncommon\x10\x01\x12\x08\n\x04Rare\x10\x02\x12\x08\n\x04\x45pic\x10\x03\x12\x0c\n\x08Mythical\x10\x04\x12\x0b\n\x07Special\x10\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RARITY = _descriptor.EnumDescriptor(
  name='Rarity',
  full_name='MAPAPI.Response41.Rarity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Common', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Uncommon', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Rare', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Epic', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Mythical', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Special', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=123,
  serialized_end=204,
)
_sym_db.RegisterEnumDescriptor(_RARITY)

Rarity = enum_type_wrapper.EnumTypeWrapper(_RARITY)
Common = 0
Uncommon = 1
Rare = 2
Epic = 3
Mythical = 4
Special = 5



_ZONEITEM = _descriptor.Descriptor(
  name='ZoneItem',
  full_name='MAPAPI.Response41.ZoneItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ItemID', full_name='MAPAPI.Response41.ZoneItem.ItemID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ItemRarity', full_name='MAPAPI.Response41.ZoneItem.ItemRarity', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=37,
  serialized_end=121,
)

_ZONEITEM.fields_by_name['ItemRarity'].enum_type = _RARITY
DESCRIPTOR.message_types_by_name['ZoneItem'] = _ZONEITEM
DESCRIPTOR.enum_types_by_name['Rarity'] = _RARITY

ZoneItem = _reflection.GeneratedProtocolMessageType('ZoneItem', (_message.Message,), dict(
  DESCRIPTOR = _ZONEITEM,
  __module__ = 'ZoneItem_pb2'
  # @@protoc_insertion_point(class_scope:MAPAPI.Response41.ZoneItem)
  ))
_sym_db.RegisterMessage(ZoneItem)


# @@protoc_insertion_point(module_scope)