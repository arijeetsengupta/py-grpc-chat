import tkinter as tk


class ChatMessagesFrame(tk.Frame):
    __CHAT_MESSAGE_HEIGHT = 20

    def __init__(self, master):
        super(ChatMessagesFrame, self).__init__(master)
        self.__setup_chat_messages_widget()

    def __setup_chat_messages_widget(self):
        self.__chat_messages = tk.Listbox(self, height=self.__CHAT_MESSAGE_HEIGHT)
        self.__chat_messages.pack(fill=tk.BOTH)

    def add_message(self, username, message):
        next_item_index = self.__chat_messages.size() + 1
        self.__chat_messages.insert(next_item_index, '[{:10}] - {}'.format(username, message))

    def clear_chat_messages(self):
        messages_start_index = 0
        messsages_end_index = self.__chat_messages.size()
        self.__chat_messages.delete(messages_start_index, messsages_end_index)
