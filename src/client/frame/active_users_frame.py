import tkinter as tk
from src.client.frame.base import BaseChatFrame
# from src.client.frame.one_one_window import one_one_chat
from one_one_window import one_one_chat
from tkinter.messagebox import showinfo


class ActiveUsersFrame(tk.Frame):

    __ACTIVE_USER_LIST_WIDTH = 21
    __ACTIVE_USER_LIST_HEIGHT = 18
    __ACTIVE_USER_BORDER_SIZE = 0

    def __init__(self, master, username):
        super(ActiveUsersFrame, self).__init__(master)
        self.username = username
        self.__setup_widgets()

    def __setup_widgets(self):
        self.__active_user_label = tk.Label(self, text='Active Users')
        self.__active_user_label.pack()

        self.__active_users_list = tk.Listbox(self,
                                              bd=self.__ACTIVE_USER_BORDER_SIZE,
                                              height=self.__ACTIVE_USER_LIST_HEIGHT,
                                              width=self.__ACTIVE_USER_LIST_WIDTH,
                                              selectmode=tk.SINGLE)
        self.__active_users_list.pack()

        def items_selected(event):
            # get all selected indices
            selected_indices = self.__active_users_list.curselection()
            # get selected items
            recipient = ",".join([self.__active_users_list.get(i) for i in selected_indices])
            msg = f'You selected: {recipient}'
            print(self.username)
            one_one_chat(self.username, recipient)
            # showinfo(title='Information', message=msg)

        self.__active_users_list.bind('<<ListboxSelect>>', items_selected)

    def clear_active_user_list(self):
        messages_start_index = 0
        messsages_end_index = self.__active_users_list.size()
        self.__active_users_list.delete(messages_start_index, messsages_end_index)

    def add_active_user(self, username):
        messages_start_index = self.__active_users_list.size() + 1
        self.__active_users_list.insert(messages_start_index, username)
