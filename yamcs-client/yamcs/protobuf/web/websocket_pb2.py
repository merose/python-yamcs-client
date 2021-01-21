# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yamcs/protobuf/web/websocket.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yamcs.protobuf import yamcs_pb2 as yamcs_dot_protobuf_dot_yamcs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='yamcs/protobuf/web/websocket.proto',
  package='yamcs.protobuf.web',
  syntax='proto2',
  serialized_options=_b('\n\022org.yamcs.protobufB\010WebProtoP\001'),
  serialized_pb=_b('\n\"yamcs/protobuf/web/websocket.proto\x12\x12yamcs.protobuf.web\x1a\x1ayamcs/protobuf/yamcs.proto\"\xac\x01\n\x1cParameterSubscriptionRequest\x12)\n\x02id\x18\x01 \x03(\x0b\x32\x1d.yamcs.protobuf.NamedObjectId\x12\x16\n\x0e\x61\x62ortOnInvalid\x18\x02 \x01(\x08\x12\x1a\n\x12updateOnExpiration\x18\x03 \x01(\x08\x12\x15\n\rsendFromCache\x18\x04 \x01(\x08\x12\x16\n\x0esubscriptionId\x18\x05 \x01(\x05\"g\n\x1dParameterSubscriptionResponse\x12.\n\x07invalid\x18\x02 \x03(\x0b\x32\x1d.yamcs.protobuf.NamedObjectId\x12\x16\n\x0esubscriptionId\x18\x03 \x01(\x05\x42 \n\x12org.yamcs.protobufB\x08WebProtoP\x01')
  ,
  dependencies=[yamcs_dot_protobuf_dot_yamcs__pb2.DESCRIPTOR,])




_PARAMETERSUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='ParameterSubscriptionRequest',
  full_name='yamcs.protobuf.web.ParameterSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='yamcs.protobuf.web.ParameterSubscriptionRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abortOnInvalid', full_name='yamcs.protobuf.web.ParameterSubscriptionRequest.abortOnInvalid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updateOnExpiration', full_name='yamcs.protobuf.web.ParameterSubscriptionRequest.updateOnExpiration', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sendFromCache', full_name='yamcs.protobuf.web.ParameterSubscriptionRequest.sendFromCache', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptionId', full_name='yamcs.protobuf.web.ParameterSubscriptionRequest.subscriptionId', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=259,
)


_PARAMETERSUBSCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='ParameterSubscriptionResponse',
  full_name='yamcs.protobuf.web.ParameterSubscriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invalid', full_name='yamcs.protobuf.web.ParameterSubscriptionResponse.invalid', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptionId', full_name='yamcs.protobuf.web.ParameterSubscriptionResponse.subscriptionId', index=1,
      number=3, type=5, cpp_type=1, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=364,
)

_PARAMETERSUBSCRIPTIONREQUEST.fields_by_name['id'].message_type = yamcs_dot_protobuf_dot_yamcs__pb2._NAMEDOBJECTID
_PARAMETERSUBSCRIPTIONRESPONSE.fields_by_name['invalid'].message_type = yamcs_dot_protobuf_dot_yamcs__pb2._NAMEDOBJECTID
DESCRIPTOR.message_types_by_name['ParameterSubscriptionRequest'] = _PARAMETERSUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['ParameterSubscriptionResponse'] = _PARAMETERSUBSCRIPTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParameterSubscriptionRequest = _reflection.GeneratedProtocolMessageType('ParameterSubscriptionRequest', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERSUBSCRIPTIONREQUEST,
  __module__ = 'yamcs.protobuf.web.websocket_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.ParameterSubscriptionRequest)
  ))
_sym_db.RegisterMessage(ParameterSubscriptionRequest)

ParameterSubscriptionResponse = _reflection.GeneratedProtocolMessageType('ParameterSubscriptionResponse', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERSUBSCRIPTIONRESPONSE,
  __module__ = 'yamcs.protobuf.web.websocket_pb2'
  # @@protoc_insertion_point(class_scope:yamcs.protobuf.web.ParameterSubscriptionResponse)
  ))
_sym_db.RegisterMessage(ParameterSubscriptionResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
