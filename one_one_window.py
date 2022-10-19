from tkinter import *
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
import grpc
from threading import Thread
# import ChatClient
import src.utils as utils

# GUI

YAML_CONFIG_PATH = 'config.yaml'


def get_server_config_from_file():
    YAML_CONFIG_PATH = 'config.yaml'
    yaml_config = utils.read_yaml_config(YAML_CONFIG_PATH)
    return utils.get_server_config_from_yaml(yaml_config)


def subscribe_messages(username, txt):
    print("Entered subscribe message thread")
    server_host, server_port = get_server_config_from_file()
    with grpc.insecure_channel(str(server_host)+':'+str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        responses = stub.subscribeMessages(chat_pb2.ChatUserConnected(userId=username, username=username))
        for response in responses:
            print("Message received from {}: {}".format(response.username, response.message))
            send = response.username + " -> " + response.message
            txt.insert(END, "\n" + send)
            # user = e.get().lower()
            # e.delete(0, END)


def send(e, txt, username, recipient):
    message = e.get()
    send = "You -> " + message
    txt.insert(END, "\n" + send)
    user = e.get().lower()
    e.delete(0, END)
    print("Sending message: " + message)
    server_host, server_port = get_server_config_from_file()
    with grpc.insecure_channel(str(server_host)+':'+str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.sendMessage(chat_pb2.ChatMessage(
            userId=username,
            username=username,
            message=message,
            recipient=recipient))
        print("Registration response : " + response.response)


# class One_one(ChatClient):
def one_one_chat(username, recipient):
    print("Username in one_one_chat: "+username)
    root = Tk()
    root.title("Chat with "+recipient)

    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text=recipient, font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
    btn = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                 command=lambda: send(e, txt, username, recipient)).grid(row=2, column=1)
    Thread(target=subscribe_messages, args=(username,txt,)).start()
    # subscribe_messages(username)

    root.mainloop()