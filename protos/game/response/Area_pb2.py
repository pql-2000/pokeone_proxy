# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Area.proto

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
  name='Area.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nArea.proto\"D\n\x04\x41rea\x12\x0b\n\x03Map\x18\x01 \x01(\t\x12\x10\n\x08\x41reaName\x18\x02 \x01(\t\x12\x1d\n\x07Pokemon\x18\x03 \x03(\x0b\x32\x0c.AreaPokemon\"\xc2\x01\n\x0b\x41reaPokemon\x12\x14\n\tPokemonID\x18\x01 \x01(\x05:\x01\x30\x12\x16\n\x07\x46ishing\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x12\n\x03\x44\x61y\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x14\n\x05Night\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07Morning\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07\x45vening\x18\x06 \x01(\x08:\x05\x66\x61lse\x12+\n\x07Pokedex\x18\x07 \x01(\x0e\x32\x12.PokedexEntryState:\x06__None*5\n\x11PokedexEntryState\x12\n\n\x06__None\x10\x00\x12\x08\n\x04Seen\x10\x01\x12\n\n\x06\x43\x61ught\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_POKEDEXENTRYSTATE = _descriptor.EnumDescriptor(
  name='PokedexEntryState',
  full_name='PokedexEntryState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Seen', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Caught', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=281,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_POKEDEXENTRYSTATE)

PokedexEntryState = enum_type_wrapper.EnumTypeWrapper(_POKEDEXENTRYSTATE)
__None = 0
Seen = 1
Caught = 2



_AREA = _descriptor.Descriptor(
  name='Area',
  full_name='Area',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Map', full_name='Area.Map', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='AreaName', full_name='Area.AreaName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='Area.Pokemon', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=14,
  serialized_end=82,
)


_AREAPOKEMON = _descriptor.Descriptor(
  name='AreaPokemon',
  full_name='AreaPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PokemonID', full_name='AreaPokemon.PokemonID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Fishing', full_name='AreaPokemon.Fishing', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Day', full_name='AreaPokemon.Day', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Night', full_name='AreaPokemon.Night', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Morning', full_name='AreaPokemon.Morning', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Evening', full_name='AreaPokemon.Evening', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Pokedex', full_name='AreaPokemon.Pokedex', index=6,
      number=7, type=14, cpp_type=8, label=1,
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
  serialized_start=85,
  serialized_end=279,
)

_AREA.fields_by_name['Pokemon'].message_type = _AREAPOKEMON
_AREAPOKEMON.fields_by_name['Pokedex'].enum_type = _POKEDEXENTRYSTATE
DESCRIPTOR.message_types_by_name['Area'] = _AREA
DESCRIPTOR.message_types_by_name['AreaPokemon'] = _AREAPOKEMON
DESCRIPTOR.enum_types_by_name['PokedexEntryState'] = _POKEDEXENTRYSTATE

Area = _reflection.GeneratedProtocolMessageType('Area', (_message.Message,), dict(
  DESCRIPTOR = _AREA,
  __module__ = 'Area_pb2'
  # @@protoc_insertion_point(class_scope:Area)
  ))
_sym_db.RegisterMessage(Area)

AreaPokemon = _reflection.GeneratedProtocolMessageType('AreaPokemon', (_message.Message,), dict(
  DESCRIPTOR = _AREAPOKEMON,
  __module__ = 'Area_pb2'
  # @@protoc_insertion_point(class_scope:AreaPokemon)
  ))
_sym_db.RegisterMessage(AreaPokemon)


# @@protoc_insertion_point(module_scope)