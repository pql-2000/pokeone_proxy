# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Evs.proto

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


import bcl_pb2 as bcl__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Evs.proto',
  package='PSXAPI.Request19',
  syntax='proto2',
  serialized_pb=_b('\n\tEvs.proto\x12\x10PSXAPI.Request19\x1a\tbcl.proto\"\xbc\x01\n\x03\x45vs\x12\x1a\n\x07Pokemon\x18\x01 \x01(\x0b\x32\t.bcl.Guid\x12\x34\n\x06\x41\x63tion\x18\x02 \x01(\x0e\x32\x1b.PSXAPI.Request19.EvsAction:\x07Request\x12\r\n\x02Hp\x18\x03 \x01(\x05:\x01\x30\x12\x0e\n\x03\x41tk\x18\x04 \x01(\x05:\x01\x30\x12\x0e\n\x03\x44\x65\x66\x18\x05 \x01(\x05:\x01\x30\x12\x10\n\x05Speed\x18\x06 \x01(\x05:\x01\x30\x12\x10\n\x05SpAtk\x18\x07 \x01(\x05:\x01\x30\x12\x10\n\x05SpDef\x18\x08 \x01(\x05:\x01\x30*.\n\tEvsAction\x12\x0b\n\x07Request\x10\x00\x12\t\n\x05Skill\x10\x01\x12\t\n\x05Reset\x10\x02')
  ,
  dependencies=[bcl__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EVSACTION = _descriptor.EnumDescriptor(
  name='EvsAction',
  full_name='PSXAPI.Request19.EvsAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Request', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Skill', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Reset', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=233,
  serialized_end=279,
)
_sym_db.RegisterEnumDescriptor(_EVSACTION)

EvsAction = enum_type_wrapper.EnumTypeWrapper(_EVSACTION)
Request = 0
Skill = 1
Reset = 2



_EVS = _descriptor.Descriptor(
  name='Evs',
  full_name='PSXAPI.Request19.Evs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Pokemon', full_name='PSXAPI.Request19.Evs.Pokemon', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Request19.Evs.Action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hp', full_name='PSXAPI.Request19.Evs.Hp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Atk', full_name='PSXAPI.Request19.Evs.Atk', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Def', full_name='PSXAPI.Request19.Evs.Def', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Speed', full_name='PSXAPI.Request19.Evs.Speed', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpAtk', full_name='PSXAPI.Request19.Evs.SpAtk', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='SpDef', full_name='PSXAPI.Request19.Evs.SpDef', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=43,
  serialized_end=231,
)

_EVS.fields_by_name['Pokemon'].message_type = bcl__pb2._GUID
_EVS.fields_by_name['Action'].enum_type = _EVSACTION
DESCRIPTOR.message_types_by_name['Evs'] = _EVS
DESCRIPTOR.enum_types_by_name['EvsAction'] = _EVSACTION

Evs = _reflection.GeneratedProtocolMessageType('Evs', (_message.Message,), dict(
  DESCRIPTOR = _EVS,
  __module__ = 'Evs_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request19.Evs)
  ))
_sym_db.RegisterMessage(Evs)


# @@protoc_insertion_point(module_scope)