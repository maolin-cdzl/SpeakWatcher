# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: net.proto

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
  name='net.proto',
  package='ptt.net',
  serialized_pb=_b('\n\tnet.proto\x12\x07ptt.net\";\n\tHeartBeat\x12\x14\n\ttimestamp\x18\x01 \x01(\r:\x01\x30\x12\x0b\n\x03gid\x18\x02 \x01(\r\x12\x0b\n\x03uid\x18\x03 \x01(\r\"6\n\x04Ping\x12\x14\n\ttimestamp\x18\x01 \x01(\r:\x01\x30\x12\x0b\n\x03gid\x18\x02 \x01(\r\x12\x0b\n\x03uid\x18\x03 \x01(\r\"6\n\x04Pong\x12\x14\n\ttimestamp\x18\x01 \x01(\r:\x01\x30\x12\x0b\n\x03gid\x18\x02 \x01(\r\x12\x0b\n\x03uid\x18\x03 \x01(\rB\x1d\n\x1b\x63om.shanlitech.ptt.protocol')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HEARTBEAT = _descriptor.Descriptor(
  name='HeartBeat',
  full_name='ptt.net.HeartBeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ptt.net.HeartBeat.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.net.HeartBeat.gid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='ptt.net.HeartBeat.uid', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=81,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='ptt.net.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ptt.net.Ping.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.net.Ping.gid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='ptt.net.Ping.uid', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=137,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='ptt.net.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ptt.net.Pong.timestamp', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='ptt.net.Pong.gid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='ptt.net.Pong.uid', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=193,
)

DESCRIPTOR.message_types_by_name['HeartBeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG

HeartBeat = _reflection.GeneratedProtocolMessageType('HeartBeat', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEAT,
  __module__ = 'net_pb2'
  # @@protoc_insertion_point(class_scope:ptt.net.HeartBeat)
  ))
_sym_db.RegisterMessage(HeartBeat)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'net_pb2'
  # @@protoc_insertion_point(class_scope:ptt.net.Ping)
  ))
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), dict(
  DESCRIPTOR = _PONG,
  __module__ = 'net_pb2'
  # @@protoc_insertion_point(class_scope:ptt.net.Pong)
  ))
_sym_db.RegisterMessage(Pong)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033com.shanlitech.ptt.protocol'))
# @@protoc_insertion_point(module_scope)
