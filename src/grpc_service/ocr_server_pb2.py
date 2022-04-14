# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ocr_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10ocr_server.proto\"\x15\n\x05Image\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x10\n\x02Id\x12\n\n\x02id\x18\x01 \x01(\t\"\x14\n\x04Text\x12\x0c\n\x04text\x18\x01 \x01(\t2^\n\tOCRServer\x12\x1b\n\tImageSync\x12\x05.Text\x1a\x05.Text\"\x00\x12\x1b\n\nStoreImage\x12\x06.Image\x1a\x03.Id\"\x00\x12\x17\n\x07GetText\x12\x03.Id\x1a\x05.Text\"\x00\x62\x06proto3')



_IMAGE = DESCRIPTOR.message_types_by_name['Image']
_ID = DESCRIPTOR.message_types_by_name['Id']
_TEXT = DESCRIPTOR.message_types_by_name['Text']
Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'ocr_server_pb2'
  # @@protoc_insertion_point(class_scope:Image)
  })
_sym_db.RegisterMessage(Image)

Id = _reflection.GeneratedProtocolMessageType('Id', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'ocr_server_pb2'
  # @@protoc_insertion_point(class_scope:Id)
  })
_sym_db.RegisterMessage(Id)

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), {
  'DESCRIPTOR' : _TEXT,
  '__module__' : 'ocr_server_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  })
_sym_db.RegisterMessage(Text)

_OCRSERVER = DESCRIPTOR.services_by_name['OCRServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGE._serialized_start=20
  _IMAGE._serialized_end=41
  _ID._serialized_start=43
  _ID._serialized_end=59
  _TEXT._serialized_start=61
  _TEXT._serialized_end=81
  _OCRSERVER._serialized_start=83
  _OCRSERVER._serialized_end=177
# @@protoc_insertion_point(module_scope)