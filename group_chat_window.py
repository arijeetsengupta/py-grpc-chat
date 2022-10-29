# Program to make a simple
# login screen


import tkinter as tk

from src.client.frame.checklist import ChecklistBox


def group_chat_window():

    group_module_root=tk.Tk()

    # setting the windows size
    group_module_root.geometry("600x400")

    # declaring string variable
    # for storing name and password
    group_name=tk.StringVar()
    users = ["Ipshita","Arijeet","Rukhsar"]
    # def submit():

    #     name=group_name.get()
    #     print("The name is : " + name)

        
    name_label = tk.Label(group_module_root, text = 'Group Name', font=('calibre',10, 'bold'))
    name_entry = tk.Entry(group_module_root,textvariable = group_name, font=('calibre',10,'normal'))
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)

    users_lable = tk.Label(group_module_root, text="Users").grid(row=1)
    global users_list
    users_list = ChecklistBox(group_module_root,users,bd=21,height=25,width=20)
    users_list.grid(row=2)

    def start_group_chat():
        group_members = users_list.getCheckedItems()
        grp_name = group_name.get()
        print(group_members)
        print(" and Group "+grp_name)
        # add group name to users and add group to group list and close window

    sub_btn=tk.Button(group_module_root,text = 'Create Group', command = start_group_chat)
    sub_btn.grid(row=2,column=1)

    group_module_root.mainloop()
