import tkinter as tk
import src.utils as utils
import src.server.chat_pb2 as chat_pb2
import src.server.chat_pb2_grpc as chat_pb2_grpc
from group_chat_window import group_chat_window
import grpc
import tkinter as tk


def get_member_groups(username):
    server_host, server_port = utils.get_server_config_from_json()
    with grpc.insecure_channel(str(server_host) + ':' + str(server_port)) as channel:
        stub = chat_pb2_grpc.ChatStub(channel)
        response = stub.getMemberGroups(chat_pb2.ChatUser(username=username))
    groups = response.response.split(',')
    print(groups)
    return groups


def display_groups(username):
    member_groups = get_member_groups(username)
    # create a root window.
    top = tk.Tk()
    top.title("Select Group")

    # create listbox object
    listbox = tk.Listbox(top, height=10,
                         width=15,
                         activestyle='dotbox',
                         selectmode=tk.SINGLE)

    # Define the size of the window.
    top.geometry("300x250")

    # Define a label for the list.
    label = tk.Label(top, text="Your Groups")

    # insert elements by their
    # index and names.
    for idx, group in enumerate(member_groups):
        listbox.insert(idx, group)

    # pack the widgets
    label.pack()
    listbox.pack()

    def items_selected(event):
        # get all selected indices
        selected_indices = listbox.curselection()
        # get selected items
        group_name = ",".join([listbox.get(i) for i in selected_indices])
        print("Group selected: "+group_name)
        group_chat_window(username, group_name)
        # showinfo(title='Information', message=msg)

    listbox.bind('<<ListboxSelect>>', items_selected)

    # Display until User
    # exits themselves.
    top.mainloop()
