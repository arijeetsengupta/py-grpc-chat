import grpc
import src.utils as utils
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
from tkinter import *
from threading import Thread
import logging


def get_all_users():
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host)+':'+str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.getAllUsers(chat_pb2.Empty())
    users = response.response.split(',')
    # print(users)
    for user in users:
        print(user)


def create_group(username, group_name, group_members):
    server_host, server_port = utils.get_server_config_from_json()
    group_members = ','.join(group_members)
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.createGroup(chat_pb2.CreateGroupRequest(username=username,
                                                                group_name=group_name,
                                                                group_members=group_members))
    logging.info("Group creation response from server: {}".format(response.response))


def subscribe_messages(username, group_name, txt):
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        responses = stub.subscribeMessages(chat_pb2.ChatUserConnected(username=username))
        for response in responses:
            if response.is_group_chat_msg and response.group_name == group_name:
                send = response.username + " -> " + response.message
                txt.insert(END, "\n" + send)
                logging.info("Received message {} in group {} from {}".format(
                    response.message, response.group_name,response.username))


def send(e, txt, username, group_name):
    message = e.get()
    user = e.get().lower()
    e.delete(0, END)
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.sendMessage(chat_pb2.ChatMessage(
            username=username,
            message=message,
            is_broadcast=False,
            is_group_chat_msg=True,
            group_name=group_name))
    logging.info("{} sent message [{}] to group {} ".format(username, message, group_name))


def group_chat(username, group_name):
    logging.info("Entered flow for group chat.")
    root = Tk()
    root.title("Group chat: " + group_name)

    BG_GRAY = "#DDE0E2"
    BG_COLOR = "#FFFFFF"
    TEXT_COLOR = "#444546"

    # Send function
    lable1 = Label(
        root, bg=BG_COLOR, fg=TEXT_COLOR, text=username+"->"+group_name, pady=10, width=20, height=1).grid(
        row=0, column=1)
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    e = Entry(root, bg="#FFFFFF", fg=TEXT_COLOR, width=55)
    e.grid(row=2, column=0)
    btn = Button(root, text="Send", bg=BG_GRAY,
                 command=lambda: send(e, txt, username, group_name)).grid(row=2, column=1)
    Thread(target=subscribe_messages, args=(username, group_name, txt,)).start()

    root.mainloop()
