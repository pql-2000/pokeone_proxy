# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Style.proto

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
  name='Style.proto',
  package='PSXAPI.Response78',
  syntax='proto2',
  serialized_pb=_b('\n\x0bStyle.proto\x12\x11PSXAPI.Response78\"\x81\x01\n\x05Style\x12/\n\x06Gender\x18\x01 \x01(\x0e\x32\x19.PSXAPI.Response78.Gender:\x04Male\x12\x0f\n\x04Skin\x18\x02 \x01(\x05:\x01\x30\x12\x0f\n\x04\x45yes\x18\x03 \x01(\x05:\x01\x30\x12\x0f\n\x04Hair\x18\x04 \x01(\x05:\x01\x30\x12\x14\n\tHairColor\x18\x05 \x01(\x05:\x01\x30*\x1e\n\x06Gender\x12\x08\n\x04Male\x10\x00\x12\n\n\x06\x46\x65male\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='PSXAPI.Response78.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Male', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Female', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=166,
  serialized_end=196,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

Gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
Male = 0
Female = 1



_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='PSXAPI.Response78.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Gender', full_name='PSXAPI.Response78.Style.Gender', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Skin', full_name='PSXAPI.Response78.Style.Skin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Eyes', full_name='PSXAPI.Response78.Style.Eyes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hair', full_name='PSXAPI.Response78.Style.Hair', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HairColor', full_name='PSXAPI.Response78.Style.HairColor', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_end=164,
)

_STYLE.fields_by_name['Gender'].enum_type = _GENDER
DESCRIPTOR.message_types_by_name['Style'] = _STYLE
DESCRIPTOR.enum_types_by_name['Gender'] = _GENDER

Style = _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), dict(
  DESCRIPTOR = _STYLE,
  __module__ = 'Style_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response78.Style)
  ))
_sym_db.RegisterMessage(Style)


# @@protoc_insertion_point(module_scope)