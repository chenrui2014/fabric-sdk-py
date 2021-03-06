# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/chaincode_event.proto

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
  name='hfc/protos/peer/chaincode_event.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n%hfc/protos/peer/chaincode_event.proto\x12\x06protos\"Z\n\x0e\x43haincodeEvent\x12\x14\n\x0c\x63haincode_id\x18\x01 \x01(\t\x12\r\n\x05tx_id\x18\x02 \x01(\t\x12\x12\n\nevent_name\x18\x03 \x01(\t\x12\x0f\n\x07payload\x18\x04 \x01(\x0c\x42\x66\n\"org.hyperledger.fabric.protos.peerB\x15\x43haincodeEventPackageZ)github.com/hyperledger/fabric/protos/peerb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHAINCODEEVENT = _descriptor.Descriptor(
  name='ChaincodeEvent',
  full_name='protos.ChaincodeEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_id', full_name='protos.ChaincodeEvent.chaincode_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='protos.ChaincodeEvent.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event_name', full_name='protos.ChaincodeEvent.event_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='protos.ChaincodeEvent.payload', index=3,
      number=4, type=12, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['ChaincodeEvent'] = _CHAINCODEEVENT

ChaincodeEvent = _reflection.GeneratedProtocolMessageType('ChaincodeEvent', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEEVENT,
  __module__ = 'hfc.protos.peer.chaincode_event_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeEvent)
  ))
_sym_db.RegisterMessage(ChaincodeEvent)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\"org.hyperledger.fabric.protos.peerB\025ChaincodeEventPackageZ)github.com/hyperledger/fabric/protos/peer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
