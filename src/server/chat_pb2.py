# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/server/chat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15src/server/chat.proto\"Q\n\x12\x43reateGroupRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x15\n\rgroup_members\x18\x03 \x01(\t\"\x07\n\x05\x45mpty\"\x1c\n\x08\x43hatUser\x12\x10\n\x08username\x18\x01 \x01(\t\"%\n\x11\x43hatUserConnected\x12\x10\n\x08username\x18\x01 \x01(\t\"7\n\x0e\x43hatActiveUser\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x13\n\x0b\x63urrentHash\x18\x02 \x01(\t\",\n\x12\x43hatUserDisconnect\x12\x16\n\x0eisDisconnected\x18\x01 \x01(\x08\"\x88\x01\n\x0b\x43hatMessage\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x11\n\trecipient\x18\x03 \x01(\t\x12\x14\n\x0cis_broadcast\x18\x04 \x01(\x08\x12\x19\n\x11is_group_chat_msg\x18\x05 \x01(\x08\x12\x12\n\ngroup_name\x18\x06 \x01(\t\"+\n\x05\x43reds\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\"\n\x0eServerResponse\x12\x10\n\x08response\x18\x01 \x01(\t2\xdf\x03\n\x04\x43hat\x12(\n\x07\x63onnect\x12\t.ChatUser\x1a\x12.ChatUserConnected\x12\x34\n\ndisconnect\x12\x12.ChatUserConnected\x1a\x12.ChatUserConnected\x12,\n\x0bsendMessage\x12\x0c.ChatMessage\x1a\x0f.ServerResponse\x12\x37\n\x11subscribeMessages\x12\x12.ChatUserConnected\x1a\x0c.ChatMessage0\x01\x12=\n\x14subscribeActiveUsers\x12\x12.ChatUserConnected\x1a\x0f.ChatActiveUser0\x01\x12#\n\x08register\x12\x06.Creds\x1a\x0f.ServerResponse\x12 \n\x05login\x12\x06.Creds\x1a\x0f.ServerResponse\x12&\n\x0bgetAllUsers\x12\x06.Empty\x1a\x0f.ServerResponse\x12\x33\n\x0b\x63reateGroup\x12\x13.CreateGroupRequest\x1a\x0f.ServerResponse\x12-\n\x0fgetMemberGroups\x12\t.ChatUser\x1a\x0f.ServerResponseb\x06proto3')



_CREATEGROUPREQUEST = DESCRIPTOR.message_types_by_name['CreateGroupRequest']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_CHATUSER = DESCRIPTOR.message_types_by_name['ChatUser']
_CHATUSERCONNECTED = DESCRIPTOR.message_types_by_name['ChatUserConnected']
_CHATACTIVEUSER = DESCRIPTOR.message_types_by_name['ChatActiveUser']
_CHATUSERDISCONNECT = DESCRIPTOR.message_types_by_name['ChatUserDisconnect']
_CHATMESSAGE = DESCRIPTOR.message_types_by_name['ChatMessage']
_CREDS = DESCRIPTOR.message_types_by_name['Creds']
_SERVERRESPONSE = DESCRIPTOR.message_types_by_name['ServerResponse']
CreateGroupRequest = _reflection.GeneratedProtocolMessageType('CreateGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGROUPREQUEST,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:CreateGroupRequest)
  })
_sym_db.RegisterMessage(CreateGroupRequest)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

ChatUser = _reflection.GeneratedProtocolMessageType('ChatUser', (_message.Message,), {
  'DESCRIPTOR' : _CHATUSER,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatUser)
  })
_sym_db.RegisterMessage(ChatUser)

ChatUserConnected = _reflection.GeneratedProtocolMessageType('ChatUserConnected', (_message.Message,), {
  'DESCRIPTOR' : _CHATUSERCONNECTED,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatUserConnected)
  })
_sym_db.RegisterMessage(ChatUserConnected)

ChatActiveUser = _reflection.GeneratedProtocolMessageType('ChatActiveUser', (_message.Message,), {
  'DESCRIPTOR' : _CHATACTIVEUSER,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatActiveUser)
  })
_sym_db.RegisterMessage(ChatActiveUser)

ChatUserDisconnect = _reflection.GeneratedProtocolMessageType('ChatUserDisconnect', (_message.Message,), {
  'DESCRIPTOR' : _CHATUSERDISCONNECT,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatUserDisconnect)
  })
_sym_db.RegisterMessage(ChatUserDisconnect)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)

Creds = _reflection.GeneratedProtocolMessageType('Creds', (_message.Message,), {
  'DESCRIPTOR' : _CREDS,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:Creds)
  })
_sym_db.RegisterMessage(Creds)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVERRESPONSE,
  '__module__' : 'src.server.chat_pb2'
  # @@protoc_insertion_point(class_scope:ServerResponse)
  })
_sym_db.RegisterMessage(ServerResponse)

_CHAT = DESCRIPTOR.services_by_name['Chat']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEGROUPREQUEST._serialized_start=25
  _CREATEGROUPREQUEST._serialized_end=106
  _EMPTY._serialized_start=108
  _EMPTY._serialized_end=115
  _CHATUSER._serialized_start=117
  _CHATUSER._serialized_end=145
  _CHATUSERCONNECTED._serialized_start=147
  _CHATUSERCONNECTED._serialized_end=184
  _CHATACTIVEUSER._serialized_start=186
  _CHATACTIVEUSER._serialized_end=241
  _CHATUSERDISCONNECT._serialized_start=243
  _CHATUSERDISCONNECT._serialized_end=287
  _CHATMESSAGE._serialized_start=290
  _CHATMESSAGE._serialized_end=426
  _CREDS._serialized_start=428
  _CREDS._serialized_end=471
  _SERVERRESPONSE._serialized_start=473
  _SERVERRESPONSE._serialized_end=507
  _CHAT._serialized_start=510
  _CHAT._serialized_end=989
# @@protoc_insertion_point(module_scope)
