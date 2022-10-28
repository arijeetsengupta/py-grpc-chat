import tkinter as tk
from src.client.frame.base import BaseChatFrame
# from src.client.frame.one_one_window import one_one_chat
from one_one_window import one_one_chat
from tkinter.messagebox import showinfo

selected_users = []

class ChecklistBox(tk.Frame):
    def __init__(self, parent, users, **kwargs):
        global selected_users
        tk.Frame.__init__(self, parent, **kwargs)

        for x in range(len(users)):
            l = tk.Checkbutton(self, text=users[x], variable=users[x],command=lambda x=users[x]:selected_users.append(x))
            l.pack(anchor = 'w')
        #tk.Button(self,text="Ok",command=lambda: [print(selected_users)]).pack()


    def getCheckedItems(self):
        global selected_users
        return selected_users


