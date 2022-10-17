from tkinter import *
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
import grpc
from threading import Thread
# import ChatClient

# GUI


def subscribe_messages(username):
    print("Entered subscribe message thread")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        responses = stub.subscribeMessages(chat_pb2.ChatUserConnected(userId=username, username=username))
        for response in responses:
            print("Message received from {}: {}".format(response.username, response.message))


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
    def send():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)
        user = e.get().lower()
        e.delete(0, END)

    lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text=recipient, font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)
    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
    send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                  command=send).grid(row=2, column=1)
    # threading.Thread(target=self.__listen_for_messages, daemon=True).start()

    Thread(target=subscribe_messages, args=(username,)).start()
    # subscribe_messages(username)

    root.mainloop()