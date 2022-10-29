from tkinter import *
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
import grpc
from threading import Thread
import src.utils as utils


def subscribe_messages(username, recipient, txt):
    print("In one-one subscribe message for {}...".format(username))
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        responses = stub.subscribeMessages(chat_pb2.ChatUserConnected(username=username))
        for response in responses:
            if not response.is_broadcast and ((
                    response.recipient == username and response.username == recipient) or (
                    response.recipient == recipient and response.username == username)
            ):
                send = response.username + " -> " + response.message
                txt.insert(END, "\n" + send)


def send(e, txt, username, recipient):
    message = e.get()
    # send = "You -> " + message
    # txt.insert(END, "\n" + send)
    user = e.get().lower()
    e.delete(0, END)
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.sendMessage(chat_pb2.ChatMessage(
            username=username,
            message=message,
            recipient=recipient,
            is_broadcast=0))


def one_one_chat(username, recipient):
    root = Tk()
    root.title("Chat with " + recipient)

    BG_GRAY = "#DDE0E2"
    BG_COLOR = "#FFFFFF"
    TEXT_COLOR = "#444546"

    # Send function
    lable1 = Label(
        root, bg=BG_COLOR, fg=TEXT_COLOR, text=username+"->"+recipient, pady=10, width=20, height=1).grid(
        row=0, column=1)
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    e = Entry(root, bg="#FFFFFF", fg=TEXT_COLOR, width=55)
    e.grid(row=2, column=0)
    btn = Button(root, text="Send", bg=BG_GRAY,
                 command=lambda: send(e, txt, username, recipient)).grid(row=2, column=1)
    Thread(target=subscribe_messages, args=(username, recipient, txt,)).start()

    root.mainloop()
