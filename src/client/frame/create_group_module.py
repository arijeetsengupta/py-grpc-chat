import tkinter as tk
from src.client.frame.base import BaseChatFrame
from one_one_window import one_one_chat
from tkinter.messagebox import showinfo
from tkinter import *
import src.utils as utils
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
import grpc

from src.client.frame.checklist import ChecklistBox
import logging


def get_all_users():
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host)+':'+str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.getAllUsers(chat_pb2.Empty())
    users = response.response.split(',')
    return users


def create_group_backend(username, group_name, group_members):
    server_host, server_port = utils.get_server_config_from_json()
    group_members = ','.join(group_members)
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.createGroup(chat_pb2.CreateGroupRequest(username=username,
                                                                group_name=group_name,
                                                                group_members=group_members))
    logging.info("Group creation response from server: {}".format(response.response))
    return response.response


def create_group(username):
    frame = tk.Tk()
    frame.title("Enter New Group Name")
    frame.geometry('400x200')

    def select_users_in_group():
        group_name = inputtxt.get(1.0, "end-1c")
        selusers = tk.Tk()
        selusers.title("Chat Group:"+group_name)
        user_label = tk.Label(selusers, text='Add Users')
        user_label.pack()
        users = get_all_users()
        users.remove(username)
        users_list = ChecklistBox(selusers, users, bd=21, height=25, width=20)
        users_list.pack()

        def start_group_chat():
            group_members = users_list.getCheckedItems()
            group_members.append(username)
            group_create_backend_response = create_group_backend(username, group_name, group_members)
            selusers.destroy()
            frame.destroy()
            tk.messagebox.showinfo("Response", group_create_backend_response)

        create_group_button = tk.Button(
            selusers, text="Create Group", command=start_group_chat)

        create_group_button.pack()
    # TextBox Creation
    inputtxt = tk.Text(frame,
                       height=5,
                       width=20)

    inputtxt.pack()
    # Button Creation
    printButton = tk.Button(frame,
                            text="Continue",
                            command=select_users_in_group)
    printButton.pack()
    # Label Creation
    lbl = tk.Label(frame, text="")
    lbl.pack()
    frame.mainloop()
