# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RegionUpdate.proto

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
  name='RegionUpdate.proto',
  package='PSXAPI.Response68',
  syntax='proto2',
  serialized_pb=_b('\n\x12RegionUpdate.proto\x12\x11PSXAPI.Response68\"N\n\x0cRegionUpdate\x12\x13\n\x08RegionID\x18\x01 \x01(\x05:\x01\x30\x12\x10\n\x05\x43oins\x18\x02 \x01(\r:\x01\x30\x12\x17\n\x0c\x42\x61ttlePoints\x18\x03 \x01(\r:\x01\x30')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REGIONUPDATE = _descriptor.Descriptor(
  name='RegionUpdate',
  full_name='PSXAPI.Response68.RegionUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='RegionID', full_name='PSXAPI.Response68.RegionUpdate.RegionID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Coins', full_name='PSXAPI.Response68.RegionUpdate.Coins', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='BattlePoints', full_name='PSXAPI.Response68.RegionUpdate.BattlePoints', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=41,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['RegionUpdate'] = _REGIONUPDATE

RegionUpdate = _reflection.GeneratedProtocolMessageType('RegionUpdate', (_message.Message,), dict(
  DESCRIPTOR = _REGIONUPDATE,
  __module__ = 'RegionUpdate_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response68.RegionUpdate)
  ))
_sym_db.RegisterMessage(RegionUpdate)


# @@protoc_insertion_point(module_scope)