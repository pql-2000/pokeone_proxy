# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Stats.proto

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
  name='Stats.proto',
  package='PSXAPI.Response77',
  syntax='proto2',
  serialized_pb=_b('\n\x0bStats.proto\x12\x11PSXAPI.Response77\"*\n\x05\x45quip\x12\x11\n\x06\x43lothe\x18\x01 \x01(\x05:\x01\x30\x12\x0e\n\x03Hat\x18\x02 \x01(\x05:\x01\x30\"\xb5\x04\n\x05Stats\x12\x10\n\x08Username\x18\x01 \x01(\t\x12\x35\n\x06Result\x18\x02 \x01(\x0e\x32\x1e.PSXAPI.Response77.StatsResult:\x05\x45rror\x12\x0e\n\x06\x42\x61\x64ges\x18\x03 \x03(\x05\x12&\n\x04\x44\x61ta\x18\x04 \x01(\x0b\x32\x18.PSXAPI.Response77.Stats\x12\x14\n\x0cLevelRegions\x18\x05 \x03(\x05\x12\x0e\n\x06Levels\x18\x06 \x03(\r\x12\x11\n\x06Region\x18\x07 \x01(\x05:\x01\x30\x12\x11\n\tGuildName\x18\x08 \x01(\t\x12\x18\n\rGuildEmblemId\x18\t \x01(\r:\x01\x30\x12\x19\n\nGuildAdmin\x18\n \x01(\x08:\x05\x66\x61lse\x12\'\n\x05Style\x18\x0b \x01(\x0b\x32\x18.PSXAPI.Response77.Style\x12\'\n\x05\x45quip\x18\x0c \x01(\x0b\x32\x18.PSXAPI.Response77.Equip\x12:\n\nMemberRank\x18\r \x01(\x0e\x32\x1d.PSXAPI.Response77.MemberRank:\x07__None0\x12\x38\n\tStaffRank\x18\x0e \x01(\x0e\x32\x1c.PSXAPI.Response77.StaffRank:\x07__None1\x12\x11\n\x06\x46ollow\x18\x0f \x01(\x05:\x01\x30\x12\x1c\n\x11\x46ollowPersonality\x18\x10 \x01(\x05:\x01\x30\x12\x1a\n\x0b\x46ollowShiny\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\x15\n\x06Online\x18\x12 \x01(\x08:\x05\x66\x61lse\"\x81\x01\n\x05Style\x12/\n\x06Gender\x18\x01 \x01(\x0e\x32\x19.PSXAPI.Response77.Gender:\x04Male\x12\x0f\n\x04Skin\x18\x02 \x01(\x05:\x01\x30\x12\x0f\n\x04\x45yes\x18\x03 \x01(\x05:\x01\x30\x12\x0f\n\x04Hair\x18\x04 \x01(\x05:\x01\x30\x12\x14\n\tHairColor\x18\x05 \x01(\x05:\x01\x30*\x1e\n\x06Gender\x12\x08\n\x04Male\x10\x00\x12\n\n\x06\x46\x65male\x10\x01*%\n\nMemberRank\x12\x0b\n\x07__None0\x10\x00\x12\n\n\x06Member\x10\x01*I\n\tStaffRank\x12\x0b\n\x07__None1\x10\x00\x12\r\n\tDeveloper\x10\x01\x12\x11\n\rGameModerator\x10\x02\x12\r\n\tModerator\x10\x03*9\n\x0bStatsResult\x12\t\n\x05\x45rror\x10\x00\x12\x08\n\x04Self\x10\x01\x12\x08\n\x04User\x10\x02\x12\x0b\n\x07Private\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='PSXAPI.Response77.Gender',
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
  serialized_start=778,
  serialized_end=808,
)
_sym_db.RegisterEnumDescriptor(_GENDER)

Gender = enum_type_wrapper.EnumTypeWrapper(_GENDER)
_MEMBERRANK = _descriptor.EnumDescriptor(
  name='MemberRank',
  full_name='PSXAPI.Response77.MemberRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Member', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=810,
  serialized_end=847,
)
_sym_db.RegisterEnumDescriptor(_MEMBERRANK)

MemberRank = enum_type_wrapper.EnumTypeWrapper(_MEMBERRANK)
_STAFFRANK = _descriptor.EnumDescriptor(
  name='StaffRank',
  full_name='PSXAPI.Response77.StaffRank',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='__None1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Developer', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GameModerator', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Moderator', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=849,
  serialized_end=922,
)
_sym_db.RegisterEnumDescriptor(_STAFFRANK)

StaffRank = enum_type_wrapper.EnumTypeWrapper(_STAFFRANK)
_STATSRESULT = _descriptor.EnumDescriptor(
  name='StatsResult',
  full_name='PSXAPI.Response77.StatsResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Error', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Self', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='User', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Private', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=924,
  serialized_end=981,
)
_sym_db.RegisterEnumDescriptor(_STATSRESULT)

StatsResult = enum_type_wrapper.EnumTypeWrapper(_STATSRESULT)
Male = 0
Female = 1
__None0 = 0
Member = 1
__None1 = 0
Developer = 1
GameModerator = 2
Moderator = 3
Error = 0
Self = 1
User = 2
Private = 3



_EQUIP = _descriptor.Descriptor(
  name='Equip',
  full_name='PSXAPI.Response77.Equip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Clothe', full_name='PSXAPI.Response77.Equip.Clothe', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hat', full_name='PSXAPI.Response77.Equip.Hat', index=1,
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
  serialized_start=34,
  serialized_end=76,
)


_STATS = _descriptor.Descriptor(
  name='Stats',
  full_name='PSXAPI.Response77.Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Username', full_name='PSXAPI.Response77.Stats.Username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Result', full_name='PSXAPI.Response77.Stats.Result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Badges', full_name='PSXAPI.Response77.Stats.Badges', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data', full_name='PSXAPI.Response77.Stats.Data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LevelRegions', full_name='PSXAPI.Response77.Stats.LevelRegions', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Levels', full_name='PSXAPI.Response77.Stats.Levels', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Region', full_name='PSXAPI.Response77.Stats.Region', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuildName', full_name='PSXAPI.Response77.Stats.GuildName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuildEmblemId', full_name='PSXAPI.Response77.Stats.GuildEmblemId', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GuildAdmin', full_name='PSXAPI.Response77.Stats.GuildAdmin', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Style', full_name='PSXAPI.Response77.Stats.Style', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Equip', full_name='PSXAPI.Response77.Stats.Equip', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MemberRank', full_name='PSXAPI.Response77.Stats.MemberRank', index=12,
      number=13, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StaffRank', full_name='PSXAPI.Response77.Stats.StaffRank', index=13,
      number=14, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Follow', full_name='PSXAPI.Response77.Stats.Follow', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FollowPersonality', full_name='PSXAPI.Response77.Stats.FollowPersonality', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FollowShiny', full_name='PSXAPI.Response77.Stats.FollowShiny', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Online', full_name='PSXAPI.Response77.Stats.Online', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
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
  serialized_start=79,
  serialized_end=644,
)


_STYLE = _descriptor.Descriptor(
  name='Style',
  full_name='PSXAPI.Response77.Style',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Gender', full_name='PSXAPI.Response77.Style.Gender', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Skin', full_name='PSXAPI.Response77.Style.Skin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Eyes', full_name='PSXAPI.Response77.Style.Eyes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Hair', full_name='PSXAPI.Response77.Style.Hair', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HairColor', full_name='PSXAPI.Response77.Style.HairColor', index=4,
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
  serialized_start=647,
  serialized_end=776,
)

_STATS.fields_by_name['Result'].enum_type = _STATSRESULT
_STATS.fields_by_name['Data'].message_type = _STATS
_STATS.fields_by_name['Style'].message_type = _STYLE
_STATS.fields_by_name['Equip'].message_type = _EQUIP
_STATS.fields_by_name['MemberRank'].enum_type = _MEMBERRANK
_STATS.fields_by_name['StaffRank'].enum_type = _STAFFRANK
_STYLE.fields_by_name['Gender'].enum_type = _GENDER
DESCRIPTOR.message_types_by_name['Equip'] = _EQUIP
DESCRIPTOR.message_types_by_name['Stats'] = _STATS
DESCRIPTOR.message_types_by_name['Style'] = _STYLE
DESCRIPTOR.enum_types_by_name['Gender'] = _GENDER
DESCRIPTOR.enum_types_by_name['MemberRank'] = _MEMBERRANK
DESCRIPTOR.enum_types_by_name['StaffRank'] = _STAFFRANK
DESCRIPTOR.enum_types_by_name['StatsResult'] = _STATSRESULT

Equip = _reflection.GeneratedProtocolMessageType('Equip', (_message.Message,), dict(
  DESCRIPTOR = _EQUIP,
  __module__ = 'Stats_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response77.Equip)
  ))
_sym_db.RegisterMessage(Equip)

Stats = _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), dict(
  DESCRIPTOR = _STATS,
  __module__ = 'Stats_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response77.Stats)
  ))
_sym_db.RegisterMessage(Stats)

Style = _reflection.GeneratedProtocolMessageType('Style', (_message.Message,), dict(
  DESCRIPTOR = _STYLE,
  __module__ = 'Stats_pb2'
  # @@protoc_insertion_point(class_scope:PSXAPI.Response77.Style)
  ))
_sym_db.RegisterMessage(Style)


# @@protoc_insertion_point(module_scope)