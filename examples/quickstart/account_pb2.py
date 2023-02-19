# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='account.proto',
  package='account',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\raccount.proto\x12\x07\x61\x63\x63ount\x1a\x1bgoogle/protobuf/empty.proto\"C\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06groups\x18\x04 \x03(\x05\"\x11\n\x0fUserListRequest\"!\n\x13UserRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x88\x02\n\x0eUserController\x12\x33\n\x04List\x12\x18.account.UserListRequest\x1a\r.account.User\"\x00\x30\x01\x12(\n\x06\x43reate\x12\r.account.User\x1a\r.account.User\"\x00\x12\x39\n\x08Retrieve\x12\x1c.account.UserRetrieveRequest\x1a\r.account.User\"\x00\x12(\n\x06Update\x12\r.account.User\x1a\r.account.User\"\x00\x12\x32\n\x07\x44\x65stroy\x12\r.account.User\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='account.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='account.User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='account.User.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='account.User.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='groups', full_name='account.User.groups', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=122,
)


_USERLISTREQUEST = _descriptor.Descriptor(
  name='UserListRequest',
  full_name='account.UserListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=141,
)


_USERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='UserRetrieveRequest',
  full_name='account.UserRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='account.UserRetrieveRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=176,
)

DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserListRequest'] = _USERLISTREQUEST
DESCRIPTOR.message_types_by_name['UserRetrieveRequest'] = _USERRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.User)
  })
_sym_db.RegisterMessage(User)

UserListRequest = _reflection.GeneratedProtocolMessageType('UserListRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERLISTREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.UserListRequest)
  })
_sym_db.RegisterMessage(UserListRequest)

UserRetrieveRequest = _reflection.GeneratedProtocolMessageType('UserRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERRETRIEVEREQUEST,
  '__module__' : 'account_pb2'
  # @@protoc_insertion_point(class_scope:account.UserRetrieveRequest)
  })
_sym_db.RegisterMessage(UserRetrieveRequest)



_USERCONTROLLER = _descriptor.ServiceDescriptor(
  name='UserController',
  full_name='account.UserController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=179,
  serialized_end=443,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='account.UserController.List',
    index=0,
    containing_service=None,
    input_type=_USERLISTREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='account.UserController.Create',
    index=1,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='account.UserController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_USERRETRIEVEREQUEST,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='account.UserController.Update',
    index=3,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='account.UserController.Destroy',
    index=4,
    containing_service=None,
    input_type=_USER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERCONTROLLER)

DESCRIPTOR.services_by_name['UserController'] = _USERCONTROLLER

# @@protoc_insertion_point(module_scope)
