# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hrm.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hrm.proto',
  package='hrm',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\thrm.proto\x12\x03hrm\x1a\x1egoogle/protobuf/wrappers.proto\"1\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x81\x01\n\x1aPersonPartialUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05\x65mail\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue2S\n\x10PersonController\x12?\n\rPartialUpdate\x12\x1f.hrm.PersonPartialUpdateRequest\x1a\x0b.hrm.Person\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='hrm.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hrm.Person.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hrm.Person.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='hrm.Person.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=50,
  serialized_end=99,
)


_PERSONPARTIALUPDATEREQUEST = _descriptor.Descriptor(
  name='PersonPartialUpdateRequest',
  full_name='hrm.PersonPartialUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='hrm.PersonPartialUpdateRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='hrm.PersonPartialUpdateRequest.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='hrm.PersonPartialUpdateRequest.email', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=102,
  serialized_end=231,
)

_PERSONPARTIALUPDATEREQUEST.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_PERSONPARTIALUPDATEREQUEST.fields_by_name['email'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['PersonPartialUpdateRequest'] = _PERSONPARTIALUPDATEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'hrm_pb2'
  # @@protoc_insertion_point(class_scope:hrm.Person)
  })
_sym_db.RegisterMessage(Person)

PersonPartialUpdateRequest = _reflection.GeneratedProtocolMessageType('PersonPartialUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _PERSONPARTIALUPDATEREQUEST,
  '__module__' : 'hrm_pb2'
  # @@protoc_insertion_point(class_scope:hrm.PersonPartialUpdateRequest)
  })
_sym_db.RegisterMessage(PersonPartialUpdateRequest)



_PERSONCONTROLLER = _descriptor.ServiceDescriptor(
  name='PersonController',
  full_name='hrm.PersonController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=233,
  serialized_end=316,
  methods=[
  _descriptor.MethodDescriptor(
    name='PartialUpdate',
    full_name='hrm.PersonController.PartialUpdate',
    index=0,
    containing_service=None,
    input_type=_PERSONPARTIALUPDATEREQUEST,
    output_type=_PERSON,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSONCONTROLLER)

DESCRIPTOR.services_by_name['PersonController'] = _PERSONCONTROLLER

# @@protoc_insertion_point(module_scope)
