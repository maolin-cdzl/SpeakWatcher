# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: push.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ptt_pb2 as ptt__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='push.proto',
  package='ptt.push',
  syntax='proto2',
  serialized_pb=_b('\n\npush.proto\x12\x08ptt.push\x1a\tptt.proto\",\n\x0cReconfigured\x12\x1c\n\x04\x63onf\x18\x01 \x01(\x0b\x32\x0e.ptt.Configure\"(\n\x0cUsersChanged\x12\x18\n\x05users\x18\x01 \x03(\x0b\x32\t.ptt.User\"L\n\x10GroupListChanged\x12!\n\rupdate_groups\x18\x01 \x03(\x0b\x32\n.ptt.Group\x12\x15\n\trm_groups\x18\x02 \x03(\rB\x02\x10\x01\"\xd9\x01\n\x0eMembersChanged\x12\x37\n\x07\x63hanges\x18\x01 \x03(\x0b\x32&.ptt.push.MembersChanged.MemberChanged\x1a\x8d\x01\n\rMemberChanged\x12\x0b\n\x03gid\x18\x01 \x02(\r\x12\x1a\n\x0ejoined_members\x18\x02 \x03(\rB\x02\x10\x01\x12\x18\n\x0cleft_members\x18\x03 \x03(\rB\x02\x10\x01\x12!\n\x0eupdate_members\x18\x04 \x03(\x0b\x32\t.ptt.User\x12\x16\n\nrm_members\x18\x05 \x03(\rB\x02\x10\x01\"}\n\x10\x43ontactshipAsked\x12\x34\n\x08requests\x18\x01 \x03(\x0b\x32\".ptt.push.ContactshipAsked.Request\x1a\x33\n\x07Request\x12\x0b\n\x03uid\x18\x01 \x02(\r\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05uname\x18\x03 \x01(\t\"N\n\x0f\x43ontactsChanged\x12\"\n\x0fupdate_contacts\x18\x01 \x03(\x0b\x32\t.ptt.User\x12\x17\n\x0brm_contacts\x18\x02 \x03(\rB\x02\x10\x01\"(\n\x0cMemberGetMic\x12\x0b\n\x03gid\x18\x01 \x02(\r\x12\x0b\n\x03uid\x18\x02 \x02(\r\")\n\rMemberLostMic\x12\x0b\n\x03gid\x18\x01 \x02(\r\x12\x0b\n\x03uid\x18\x02 \x02(\r\"&\n\x07LostMic\x12\x0b\n\x03gid\x18\x01 \x02(\r\x12\x0e\n\x06reason\x18\x02 \x01(\t\"u\n\x0c\x43urrentGroup\x12\x0b\n\x03gid\x18\x01 \x02(\r\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\r\n\x02ip\x18\x03 \x01(\r:\x01\x30\x12\x0f\n\x04port\x18\x04 \x01(\r:\x01\x30\x12\r\n\x05gname\x18\x05 \x01(\t\x12\x19\n\x05group\x18\x06 \x01(\x0b\x32\n.ptt.Group\"\x19\n\x07Kickout\x12\x0e\n\x06reason\x18\x01 \x01(\t\"2\n\x0cNewWorksheet\x12\"\n\nworksheets\x18\x01 \x03(\x0b\x32\x0e.ptt.Worksheet\"I\n\x0f\x43ustomBroadcast\x12\x17\n\x04\x66rom\x18\x01 \x01(\x0b\x32\t.ptt.User\x12\x10\n\x08msg_name\x18\x02 \x02(\t\x12\x0b\n\x03msg\x18\x03 \x01(\x0c\"\x1f\n\x0b\x43hangeRoles\x12\x10\n\x05roles\x18\x01 \x02(\r:\x01\x30\x42\x1d\n\x1b\x63om.shanlitech.ptt.protocol')
  ,
  dependencies=[ptt__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RECONFIGURED = _descriptor.Descriptor(
  name='Reconfigured',
  full_name='ptt.push.Reconfigured',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conf', full_name='ptt.push.Reconfigured.conf', index=0,
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
  serialized_start=35,
  serialized_end=79,
)


_USERSCHANGED = _descriptor.Descriptor(
  name='UsersChanged',
  full_name='ptt.push.UsersChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='users', full_name='ptt.push.UsersChanged.users', index=0,
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
  serialized_start=81,
  serialized_end=121,
)


_GROUPLISTCHANGED = _descriptor.Descriptor(
  name='GroupListChanged',
  full_name='ptt.push.GroupListChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_groups', full_name='ptt.push.GroupListChanged.update_groups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rm_groups', full_name='ptt.push.GroupListChanged.rm_groups', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=123,
  serialized_end=199,
)


_MEMBERSCHANGED_MEMBERCHANGED = _descriptor.Descriptor(
  name='MemberChanged',
  full_name='ptt.push.MembersChanged.MemberChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.push.MembersChanged.MemberChanged.gid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='joined_members', full_name='ptt.push.MembersChanged.MemberChanged.joined_members', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='left_members', full_name='ptt.push.MembersChanged.MemberChanged.left_members', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='update_members', full_name='ptt.push.MembersChanged.MemberChanged.update_members', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rm_members', full_name='ptt.push.MembersChanged.MemberChanged.rm_members', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=278,
  serialized_end=419,
)

_MEMBERSCHANGED = _descriptor.Descriptor(
  name='MembersChanged',
  full_name='ptt.push.MembersChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='changes', full_name='ptt.push.MembersChanged.changes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MEMBERSCHANGED_MEMBERCHANGED, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=419,
)


_CONTACTSHIPASKED_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='ptt.push.ContactshipAsked.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='ptt.push.ContactshipAsked.Request.uid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='text', full_name='ptt.push.ContactshipAsked.Request.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uname', full_name='ptt.push.ContactshipAsked.Request.uname', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=495,
  serialized_end=546,
)

_CONTACTSHIPASKED = _descriptor.Descriptor(
  name='ContactshipAsked',
  full_name='ptt.push.ContactshipAsked',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requests', full_name='ptt.push.ContactshipAsked.requests', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTACTSHIPASKED_REQUEST, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=546,
)


_CONTACTSCHANGED = _descriptor.Descriptor(
  name='ContactsChanged',
  full_name='ptt.push.ContactsChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_contacts', full_name='ptt.push.ContactsChanged.update_contacts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rm_contacts', full_name='ptt.push.ContactsChanged.rm_contacts', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
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
  serialized_start=548,
  serialized_end=626,
)


_MEMBERGETMIC = _descriptor.Descriptor(
  name='MemberGetMic',
  full_name='ptt.push.MemberGetMic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.push.MemberGetMic.gid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='ptt.push.MemberGetMic.uid', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=628,
  serialized_end=668,
)


_MEMBERLOSTMIC = _descriptor.Descriptor(
  name='MemberLostMic',
  full_name='ptt.push.MemberLostMic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.push.MemberLostMic.gid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='ptt.push.MemberLostMic.uid', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=670,
  serialized_end=711,
)


_LOSTMIC = _descriptor.Descriptor(
  name='LostMic',
  full_name='ptt.push.LostMic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.push.LostMic.gid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ptt.push.LostMic.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=713,
  serialized_end=751,
)


_CURRENTGROUP = _descriptor.Descriptor(
  name='CurrentGroup',
  full_name='ptt.push.CurrentGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.push.CurrentGroup.gid', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reason', full_name='ptt.push.CurrentGroup.reason', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='ptt.push.CurrentGroup.ip', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='ptt.push.CurrentGroup.port', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gname', full_name='ptt.push.CurrentGroup.gname', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='ptt.push.CurrentGroup.group', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=753,
  serialized_end=870,
)


_KICKOUT = _descriptor.Descriptor(
  name='Kickout',
  full_name='ptt.push.Kickout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='ptt.push.Kickout.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=872,
  serialized_end=897,
)


_NEWWORKSHEET = _descriptor.Descriptor(
  name='NewWorksheet',
  full_name='ptt.push.NewWorksheet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='worksheets', full_name='ptt.push.NewWorksheet.worksheets', index=0,
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
  serialized_start=899,
  serialized_end=949,
)


_CUSTOMBROADCAST = _descriptor.Descriptor(
  name='CustomBroadcast',
  full_name='ptt.push.CustomBroadcast',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from', full_name='ptt.push.CustomBroadcast.from', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_name', full_name='ptt.push.CustomBroadcast.msg_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ptt.push.CustomBroadcast.msg', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=951,
  serialized_end=1024,
)


_CHANGEROLES = _descriptor.Descriptor(
  name='ChangeRoles',
  full_name='ptt.push.ChangeRoles',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='ptt.push.ChangeRoles.roles', index=0,
      number=1, type=13, cpp_type=3, label=2,
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
  serialized_start=1026,
  serialized_end=1057,
)

_RECONFIGURED.fields_by_name['conf'].message_type = ptt__pb2._CONFIGURE
_USERSCHANGED.fields_by_name['users'].message_type = ptt__pb2._USER
_GROUPLISTCHANGED.fields_by_name['update_groups'].message_type = ptt__pb2._GROUP
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['update_members'].message_type = ptt__pb2._USER
_MEMBERSCHANGED_MEMBERCHANGED.containing_type = _MEMBERSCHANGED
_MEMBERSCHANGED.fields_by_name['changes'].message_type = _MEMBERSCHANGED_MEMBERCHANGED
_CONTACTSHIPASKED_REQUEST.containing_type = _CONTACTSHIPASKED
_CONTACTSHIPASKED.fields_by_name['requests'].message_type = _CONTACTSHIPASKED_REQUEST
_CONTACTSCHANGED.fields_by_name['update_contacts'].message_type = ptt__pb2._USER
_CURRENTGROUP.fields_by_name['group'].message_type = ptt__pb2._GROUP
_NEWWORKSHEET.fields_by_name['worksheets'].message_type = ptt__pb2._WORKSHEET
_CUSTOMBROADCAST.fields_by_name['from'].message_type = ptt__pb2._USER
DESCRIPTOR.message_types_by_name['Reconfigured'] = _RECONFIGURED
DESCRIPTOR.message_types_by_name['UsersChanged'] = _USERSCHANGED
DESCRIPTOR.message_types_by_name['GroupListChanged'] = _GROUPLISTCHANGED
DESCRIPTOR.message_types_by_name['MembersChanged'] = _MEMBERSCHANGED
DESCRIPTOR.message_types_by_name['ContactshipAsked'] = _CONTACTSHIPASKED
DESCRIPTOR.message_types_by_name['ContactsChanged'] = _CONTACTSCHANGED
DESCRIPTOR.message_types_by_name['MemberGetMic'] = _MEMBERGETMIC
DESCRIPTOR.message_types_by_name['MemberLostMic'] = _MEMBERLOSTMIC
DESCRIPTOR.message_types_by_name['LostMic'] = _LOSTMIC
DESCRIPTOR.message_types_by_name['CurrentGroup'] = _CURRENTGROUP
DESCRIPTOR.message_types_by_name['Kickout'] = _KICKOUT
DESCRIPTOR.message_types_by_name['NewWorksheet'] = _NEWWORKSHEET
DESCRIPTOR.message_types_by_name['CustomBroadcast'] = _CUSTOMBROADCAST
DESCRIPTOR.message_types_by_name['ChangeRoles'] = _CHANGEROLES

Reconfigured = _reflection.GeneratedProtocolMessageType('Reconfigured', (_message.Message,), dict(
  DESCRIPTOR = _RECONFIGURED,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.Reconfigured)
  ))
_sym_db.RegisterMessage(Reconfigured)

UsersChanged = _reflection.GeneratedProtocolMessageType('UsersChanged', (_message.Message,), dict(
  DESCRIPTOR = _USERSCHANGED,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.UsersChanged)
  ))
_sym_db.RegisterMessage(UsersChanged)

GroupListChanged = _reflection.GeneratedProtocolMessageType('GroupListChanged', (_message.Message,), dict(
  DESCRIPTOR = _GROUPLISTCHANGED,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.GroupListChanged)
  ))
_sym_db.RegisterMessage(GroupListChanged)

MembersChanged = _reflection.GeneratedProtocolMessageType('MembersChanged', (_message.Message,), dict(

  MemberChanged = _reflection.GeneratedProtocolMessageType('MemberChanged', (_message.Message,), dict(
    DESCRIPTOR = _MEMBERSCHANGED_MEMBERCHANGED,
    __module__ = 'push_pb2'
    # @@protoc_insertion_point(class_scope:ptt.push.MembersChanged.MemberChanged)
    ))
  ,
  DESCRIPTOR = _MEMBERSCHANGED,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.MembersChanged)
  ))
_sym_db.RegisterMessage(MembersChanged)
_sym_db.RegisterMessage(MembersChanged.MemberChanged)

ContactshipAsked = _reflection.GeneratedProtocolMessageType('ContactshipAsked', (_message.Message,), dict(

  Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR = _CONTACTSHIPASKED_REQUEST,
    __module__ = 'push_pb2'
    # @@protoc_insertion_point(class_scope:ptt.push.ContactshipAsked.Request)
    ))
  ,
  DESCRIPTOR = _CONTACTSHIPASKED,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.ContactshipAsked)
  ))
_sym_db.RegisterMessage(ContactshipAsked)
_sym_db.RegisterMessage(ContactshipAsked.Request)

ContactsChanged = _reflection.GeneratedProtocolMessageType('ContactsChanged', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTSCHANGED,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.ContactsChanged)
  ))
_sym_db.RegisterMessage(ContactsChanged)

MemberGetMic = _reflection.GeneratedProtocolMessageType('MemberGetMic', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERGETMIC,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.MemberGetMic)
  ))
_sym_db.RegisterMessage(MemberGetMic)

MemberLostMic = _reflection.GeneratedProtocolMessageType('MemberLostMic', (_message.Message,), dict(
  DESCRIPTOR = _MEMBERLOSTMIC,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.MemberLostMic)
  ))
_sym_db.RegisterMessage(MemberLostMic)

LostMic = _reflection.GeneratedProtocolMessageType('LostMic', (_message.Message,), dict(
  DESCRIPTOR = _LOSTMIC,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.LostMic)
  ))
_sym_db.RegisterMessage(LostMic)

CurrentGroup = _reflection.GeneratedProtocolMessageType('CurrentGroup', (_message.Message,), dict(
  DESCRIPTOR = _CURRENTGROUP,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.CurrentGroup)
  ))
_sym_db.RegisterMessage(CurrentGroup)

Kickout = _reflection.GeneratedProtocolMessageType('Kickout', (_message.Message,), dict(
  DESCRIPTOR = _KICKOUT,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.Kickout)
  ))
_sym_db.RegisterMessage(Kickout)

NewWorksheet = _reflection.GeneratedProtocolMessageType('NewWorksheet', (_message.Message,), dict(
  DESCRIPTOR = _NEWWORKSHEET,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.NewWorksheet)
  ))
_sym_db.RegisterMessage(NewWorksheet)

CustomBroadcast = _reflection.GeneratedProtocolMessageType('CustomBroadcast', (_message.Message,), dict(
  DESCRIPTOR = _CUSTOMBROADCAST,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.CustomBroadcast)
  ))
_sym_db.RegisterMessage(CustomBroadcast)

ChangeRoles = _reflection.GeneratedProtocolMessageType('ChangeRoles', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEROLES,
  __module__ = 'push_pb2'
  # @@protoc_insertion_point(class_scope:ptt.push.ChangeRoles)
  ))
_sym_db.RegisterMessage(ChangeRoles)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.shanlitech.ptt.protocol'))
_GROUPLISTCHANGED.fields_by_name['rm_groups'].has_options = True
_GROUPLISTCHANGED.fields_by_name['rm_groups']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['joined_members'].has_options = True
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['joined_members']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['left_members'].has_options = True
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['left_members']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['rm_members'].has_options = True
_MEMBERSCHANGED_MEMBERCHANGED.fields_by_name['rm_members']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_CONTACTSCHANGED.fields_by_name['rm_contacts'].has_options = True
_CONTACTSCHANGED.fields_by_name['rm_contacts']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)