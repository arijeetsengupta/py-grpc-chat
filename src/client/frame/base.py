import tkinter as tk


class BaseChatFrame(tk.Frame):

    def __init__(self, master, grpc_client):
        super(BaseChatFrame, self).__init__(master)
        self._grpc_client = grpc_client
