# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cluster.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ptt_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cluster.proto',
  package='ptt.cluster',
  serialized_pb=_b('\n\rcluster.proto\x12\x0bptt.cluster\x1a\tptt.proto\"/\n\x0bQueryServer\x12\x0f\n\x07version\x18\x01 \x02(\t\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\"?\n\x0eQueryServerAck\x12\x1c\n\x07servers\x18\x01 \x02(\x0b\x32\x0b.ptt.Server\x12\x0f\n\x07\x63ontext\x18\x02 \x01(\t\"2\n\x0cNotifyServer\x12\x11\n\tcompanyid\x18\x01 \x02(\t\x12\x0f\n\x07peponum\x18\x02 \x02(\x05\"!\n\x0fNotifyServerAck\x12\x0e\n\x06result\x18\x01 \x02(\x05')
  ,
  dependencies=[ptt_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_QUERYSERVER = _descriptor.Descriptor(
  name='QueryServer',
  full_name='ptt.cluster.QueryServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='ptt.cluster.QueryServer.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='ptt.cluster.QueryServer.context', index=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=88,
)


_QUERYSERVERACK = _descriptor.Descriptor(
  name='QueryServerAck',
  full_name='ptt.cluster.QueryServerAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='servers', full_name='ptt.cluster.QueryServerAck.servers', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context', full_name='ptt.cluster.QueryServerAck.context', index=1,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=153,
)


_NOTIFYSERVER = _descriptor.Descriptor(
  name='NotifyServer',
  full_name='ptt.cluster.NotifyServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='companyid', full_name='ptt.cluster.NotifyServer.companyid', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peponum', full_name='ptt.cluster.NotifyServer.peponum', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=155,
  serialized_end=205,
)


_NOTIFYSERVERACK = _descriptor.Descriptor(
  name='NotifyServerAck',
  full_name='ptt.cluster.NotifyServerAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ptt.cluster.NotifyServerAck.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=207,
  serialized_end=240,
)

_QUERYSERVERACK.fields_by_name['servers'].message_type = ptt_pb2._SERVER
DESCRIPTOR.message_types_by_name['QueryServer'] = _QUERYSERVER
DESCRIPTOR.message_types_by_name['QueryServerAck'] = _QUERYSERVERACK
DESCRIPTOR.message_types_by_name['NotifyServer'] = _NOTIFYSERVER
DESCRIPTOR.message_types_by_name['NotifyServerAck'] = _NOTIFYSERVERACK

QueryServer = _reflection.GeneratedProtocolMessageType('QueryServer', (_message.Message,), dict(
  DESCRIPTOR = _QUERYSERVER,
  __module__ = 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:ptt.cluster.QueryServer)
  ))
_sym_db.RegisterMessage(QueryServer)

QueryServerAck = _reflection.GeneratedProtocolMessageType('QueryServerAck', (_message.Message,), dict(
  DESCRIPTOR = _QUERYSERVERACK,
  __module__ = 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:ptt.cluster.QueryServerAck)
  ))
_sym_db.RegisterMessage(QueryServerAck)

NotifyServer = _reflection.GeneratedProtocolMessageType('NotifyServer', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSERVER,
  __module__ = 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:ptt.cluster.NotifyServer)
  ))
_sym_db.RegisterMessage(NotifyServer)

NotifyServerAck = _reflection.GeneratedProtocolMessageType('NotifyServerAck', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFYSERVERACK,
  __module__ = 'cluster_pb2'
  # @@protoc_insertion_point(class_scope:ptt.cluster.NotifyServerAck)
  ))
_sym_db.RegisterMessage(NotifyServerAck)


# @@protoc_insertion_point(module_scope)
