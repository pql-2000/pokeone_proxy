# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Ignore.proto

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
  name='Ignore.proto',
  package='PSXAPI.Response36',
  syntax='proto2',
  serialized_pb=_b('\n\x0cIgnore.proto\x12\x11PSXAPI.Response36\"g\n\x06Ignore\x12\'\n\x04List\x18\x01 \x03(\x0b\x32\x19.PSXAPI.Response36.Ignore\x12\x34\n\x06\x41\x63tion\x18\x02 \x01(\x0e\x32\x1f.PSXAPI.Response36.IgnoreAction:\x03\x41ll*,\n\x0cIgnoreAction\x12\x07\n\x03\x41ll\x10\x00\x12\x07\n\x03\x41\x64\x64\x10\x01\x12\n\n\x06Remove\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_IGNOREACTION = _descriptor.EnumDescriptor(
  name='IgnoreAction',
  full_name='PSXAPI.Response36.IgnoreAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='All', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Add', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Remove', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=184,
)
_sym_db.RegisterEnumDescriptor(_IGNOREACTION)

IgnoreAction = enum_type_wrapper.EnumTypeWrapper(_IGNOREACTION)
All = 0
Add = 1
Remove = 2



_IGNORE = _descriptor.Descriptor(
  name='Ignore',
  full_name='PSXAPI.Response36.Ignore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='List', full_name='PSXAPI.Response36.Ignore.List', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Action', full_name='PSXAPI.Response36.Ignore.Action', index=1,
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
  serialized_start=35,
  serialized_end=138,
)

_IGNORE.fields_by_name['List'].message_type = _IGNORE
_IGNORE.fields_by_name['Action'].enum_type = _IGNOREACTION
DESCRIPTOR.message_types_by_name['Ignore'] = _IGNORE
DESCRIPTOR.enum_types_by_name['IgnoreAction'] = _IGNOREACTION

Ignore = _reflection.GeneratedProtocolMessageType('Ignore', (_message.Message,), dict(
  DESCRIPTOR = _IGNORE,
  __module__ = 'Ignore_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response36.Ignore)
  ))
_sym_db.RegisterMessage(Ignore)


# @@protoc_insertion_point(module_scope)