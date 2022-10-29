import tkinter as tk
from turtle import width
from src.client.frame.base import BaseChatFrame
from one_one_window import one_one_chat
from tkinter.messagebox import showinfo
from tkinter import *

from src.client.frame.checklist import ChecklistBox
from src.client.frame.create_group_module import create_group
from src.client.frame.group_chat import display_groups


def group_chat_module(username):

    parent = tk.Tk()
    parent.geometry('300x150')
    frame = tk.Frame(parent)
    frame.pack()

    def create_group_module():
        parent.destroy()
        create_group(username)
    
    def display_group_module():
        parent.destroy()  
        display_groups(username)

    text_disp = tk.Button(frame,
                          text="Create New Group",
                          command=lambda: create_group_module()
                          )

    text_disp.pack(side=tk.LEFT, pady= 5, padx= 10)

    exit_button = tk.Button(frame,
                            text="Join Group",
                            command=lambda: display_group_module())
    exit_button.pack(side=tk.RIGHT, pady= 5, padx= 10)

    parent.mainloop()



