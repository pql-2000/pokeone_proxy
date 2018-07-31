# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FlyEnter.proto

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
  name='FlyEnter.proto',
  package='PSXAPI.Request20',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x46lyEnter.proto\x12\x10PSXAPI.Request20\"3\n\x08\x46lyEnter\x12\'\n\x04Move\x18\x01 \x01(\x0b\x32\x19.PSXAPI.Request20.FlyMove\"\x80\x01\n\x07\x46lyMove\x12\x0f\n\x04PosX\x18\x01 \x01(\x02:\x01\x30\x12\x0f\n\x04PosY\x18\x02 \x01(\x02:\x01\x30\x12\x0f\n\x04PosZ\x18\x03 \x01(\x02:\x01\x30\x12\x0f\n\x04RotX\x18\x04 \x01(\x02:\x01\x30\x12\x0f\n\x04RotY\x18\x05 \x01(\x02:\x01\x30\x12\x0f\n\x04RotZ\x18\x06 \x01(\x02:\x01\x30\x12\x0f\n\x04RotW\x18\x07 \x01(\x02:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FLYENTER = _descriptor.Descriptor(
  name='FlyEnter',
  full_name='PSXAPI.Request20.FlyEnter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Move', full_name='PSXAPI.Request20.FlyEnter.Move', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=36,
  serialized_end=87,
)


_FLYMOVE = _descriptor.Descriptor(
  name='FlyMove',
  full_name='PSXAPI.Request20.FlyMove',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='PosX', full_name='PSXAPI.Request20.FlyMove.PosX', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosY', full_name='PSXAPI.Request20.FlyMove.PosY', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PosZ', full_name='PSXAPI.Request20.FlyMove.PosZ', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotX', full_name='PSXAPI.Request20.FlyMove.RotX', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotY', full_name='PSXAPI.Request20.FlyMove.RotY', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotZ', full_name='PSXAPI.Request20.FlyMove.RotZ', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='RotW', full_name='PSXAPI.Request20.FlyMove.RotW', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
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
  serialized_start=90,
  serialized_end=218,
)

_FLYENTER.fields_by_name['Move'].message_type = _FLYMOVE
DESCRIPTOR.message_types_by_name['FlyEnter'] = _FLYENTER
DESCRIPTOR.message_types_by_name['FlyMove'] = _FLYMOVE

FlyEnter = _reflection.GeneratedProtocolMessageType('FlyEnter', (_message.Message,), dict(
  DESCRIPTOR = _FLYENTER,
  __module__ = 'FlyEnter_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request20.FlyEnter)
  ))
_sym_db.RegisterMessage(FlyEnter)

FlyMove = _reflection.GeneratedProtocolMessageType('FlyMove', (_message.Message,), dict(
  DESCRIPTOR = _FLYMOVE,
  __module__ = 'FlyEnter_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Request20.FlyMove)
  ))
_sym_db.RegisterMessage(FlyMove)


# @@protoc_insertion_point(module_scope)