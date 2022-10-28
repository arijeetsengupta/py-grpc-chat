import tkinter as tk
from src.client.frame.base import BaseChatFrame
# from src.client.frame.one_one_window import one_one_chat
from one_one_window import one_one_chat
from tkinter.messagebox import showinfo

from src.client.frame.checklist import ChecklistBox
#from checklist import ChecklistBox

def group_chat_module(username, groupname):
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
    group_list.pack()

    create_group_button = tk.Button(root, text="Create new Group", bg=BG_GRAY,
                 command=lambda: create_group_module(username))
    create_group_button.pack()

    root.mainloop()




def create_group_module(username):
    root=tk.Tk()
 
    # setting the windows size
    root.geometry("600x400")
    
    # declaring string variable
    # for storing name and password
    name_var=tk.StringVar()
    # passw_var=tk.StringVar()
    
    
    # defining a function that will
    # get the name and password and
    # print them on the screen
    def submit():
    
        name=name_var.get()
        # password=passw_var.get()
        
        print("The name is : " + name)
        # print("The password is : " + password)
        
        name_var.set("")
        # passw_var.set("")
        
        
    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    
    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    
    # creating a label for password
    # passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    
    # creating a entry for password
    # passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    
    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0,column=0)
    name_entry.grid(row=0,column=1)
    # passw_label.grid(row=1,column=0)
    # passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    
    # performing an infinite loop
    # for the window to display
    root.mainloop()
    # create_grp_module = tk.Tk()
    # create_grp_module.title("Create new Group")

    # group_name = tk.StringVar()

    
    # def print_group_name():
    #     g = group_name.get()
    #     print("Printing group name: "+g)

    # tk.Label(create_grp_module, text="Enter Group Name").pack()
    # group_name_entry = tk.Entry(create_grp_module, textvariable=group_name)
    # group_name_entry.pack()

    # group_name_button = tk.Button(create_grp_module, text= "Create Group", command=print_group_name)
    # group_name_button.pack()

    # create_grp_module.mainloop()
    
    # user_label = tk.Label(root,text='users')
    # user_label.pack()

    # #users = get_all_users()
    # users = ["Ipshita","Arijeet","Rukhsar"]
    # global users_list
    # users_list = ChecklistBox(root,users,bd=21,height=25,width=20)
    # users_list.pack()

    # # create_group_button = tk.Button(root, text= "Create Group", command=lambda: start_group_chat(group_name))
    # create_group_button = tk.Button(root, text= "Create Group", command=start_group_chat)
    # create_group_button.pack()

def select_users_in_group():
    selusers = tk.Tk()
    user_label = tk.Label(selusers,text='users')
    user_label.pack()

    #users = get_all_users()
    users = ["Ipshita","Arijeet","Rukhsar"]
    global users_list
    users_list = ChecklistBox(selusers,users,bd=21,height=25,width=20)
    users_list.pack()

    # create_group_button = tk.Button(root, text= "Create Group", command=lambda: start_group_chat(group_name))
    #create_group_button = tk.Button(selusers, text= "Create Group", command=start_group_chat)
    #create_group_button.pack()
    
    
# def start_group_chat():
#     global group_name
#     grp_name = group_name.get()
#     print("Group name:" + grp_name)
#     group_members = users_list.getCheckedItems()
#     print(group_members)



