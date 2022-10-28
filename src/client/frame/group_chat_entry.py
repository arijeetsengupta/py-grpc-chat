import tkinter as tk
from src.client.frame.base import BaseChatFrame
from one_one_window import one_one_chat
from tkinter.messagebox import showinfo
from tkinter import *

from src.client.frame.checklist import ChecklistBox
from src.client.frame.create_group_module import create_group
from src.client.frame.group_chat import display_groups


def group_chat_module(username):

    parent = tk.Tk()
    frame = tk.Frame(parent)
    frame.pack()

    text_disp = tk.Button(frame,
                          text="Create New Group",
                          command=lambda: create_group(username)
                          )

    text_disp.pack(side=tk.LEFT)

    exit_button = tk.Button(frame,
                            text="Join Group",
                            command=lambda: display_groups(username))
    exit_button.pack(side=tk.RIGHT)

    parent.mainloop()