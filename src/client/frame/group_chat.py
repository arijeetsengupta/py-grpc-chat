import tkinter as tk
import src.utils as utils
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
import grpc


def get_member_groups(username):
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host)+':'+str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.getMemberGroups(chat_pb2.ChatUser(username=username))
    groups = response.response.split(',')
    print(groups)
    return groups


def display_groups(username):
    get_member_groups(username)