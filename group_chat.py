import tkinter as tk
from src.client.frame.checklist import ChecklistBox
#from checklist import ChecklistBox
from group_chat_window import group_chat_window

users_list = []

def group_chat_module(username):
    root = tk.Tk()
    root.title("Group Chat")

    BG_GRAY = "#DDE0E2"
    
    user_label = tk.Label(root,text='Groups')
    user_label.pack()

    #groups = get_all_groups
    groups = ["Group1","Group2","Group3"]

    group_list = tk.Listbox(root,height=18, width=20,selectmode=tk.SINGLE)
    index = 1
    for group in groups:
        group_list.insert(index,group)
        index+=1
    group_list.grid(row=0, column=0)
    group_list.pack()

    create_group_button = tk.Button(root, text="Create new Group", bg=BG_GRAY,
                 command=group_chat_window)
    create_group_button.grid(row=0, column=1)
    create_group_button.pack()

    

    root.mainloop()


def create_group_module(username):
    create_grp_module = tk.Tk()
    create_grp_module.title("Create new Group")

    global group_name
    group_name = tk.StringVar()
    
    group_name_lable = tk.Label(create_grp_module, text="Enter Group Name")
    group_name_lable.pack()
    group_name_entry = tk.Entry(create_grp_module, textvariable=group_name)
    group_name_entry.pack()

    # group_name_button = tk.Button(create_grp_module, text= "Create Group", command=print_group_name)
    # group_name_button.pack()

    # create_grp_module.mainloop()
    
    user_label = tk.Label(create_grp_module,text='users')
    user_label.pack()

    #users = get_all_users()
    users = ["Ipshita","Arijeet","Rukhsar"]
    global users_list
    users_list = ChecklistBox(create_grp_module,users,bd=21,height=25,width=20)
    users_list.pack()

    # create_group_button = tk.Button(root, text= "Create Group", command=lambda: start_group_chat(group_name))
    create_group_button = tk.Button(create_grp_module, text= "Create Group", command=start_group_chat)
    create_group_button.pack()

def start_group_chat():
    group_members = users_list.getCheckedItems()
    grp_name = group_name.get()
    print(group_members)
    print(" and Group "+grp_name)
    # add group name to users and add group to group list and close window




