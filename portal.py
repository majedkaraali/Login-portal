

import os
from tkinter import *
from handledata import *
import threading
import time

root=Tk()
root.geometry('600x555')
root.config(bg="#9BCD9B")
root.title("Login")

started_console=False

log_page=LabelFrame(root,text="Login",width=330,height=220,padx=5,pady=5,bg="#9BCD9B")
log_page.pack()
reg_page=LabelFrame(root,text="Register",width=420,height=240,padx=5,pady=5,bg="#9BCD9B")


user_label=Label(log_page,text='UserName',bg="#9BCD9B")
user_label.place(x=10,y=10)
pass_label=Label(log_page,text='Password',bg="#9BCD9B")
pass_label.place(x=10,y=40)

usernamef=Entry(log_page,width=26)
usernamef.place(x=80,y=10)
passwordf=Entry(log_page,width=26)
passwordf.place(x=80,y=40)



or_ryg=Label(log_page,text="New here ? ",bg="#9BCD9B")
or_ryg.place(x=50,y=142)



def heompage():
    time.sleep(2)
    log_page.destroy()
    reg_page.destroy()
    root.config(bg='white')
    welcome=Label(root,text="Welcome "+f_name,bg='white',fg='blue',font=('BLOD',28))
    welcome.pack()
    

def login():
    global f_name
    username=usernamef.get()
    password=passwordf.get()
    f_name=username
    login_user(username,password)
    color='red'
    from handledata import acess,tx

    if acess==True:
        color='green'
        threading.Thread(target=heompage).start()
        
    console=Label(log_page,text=tx+" "*10,fg=color,bg="#9BCD9B")
    console.place(x=110,y=75) 
    if color=='green':
        console.config(fg='green')






def send():
    username=new_username.get()
    conf=conf_password.get()
    password=new_password.get()

    global started_console,console

    tx=''
    color='red'

    if len(username)==0:
        tx="Please enter username"
    elif len(username)<4:
        tx="Username must be at least 4 charecters"
    elif len(password)<8:
        tx="Password must be at least 8 charecters"
    elif conf !=password:
        tx="Passwords not  match"
    else:
        add_user(username,password)
        from handledata import state
        if state==True:
            tx="Account Created Sucsessfuly"
            color='green'
            new_username.delete(0,END)
            new_password.delete(0,END)
            conf_password.delete(0,END)
        elif state==False:
            tx="Username already exists"


   # console
    if started_console==True:
        console.destroy()
    console=Label(reg_page,text=tx,fg=color,bg="#9BCD9B")
    console.place(x=133,y=125)
    started_console=True
   
    
    if color=='green':
        console.config(fg='green')





def new_register():
    reg_page.pack()
    global new_password,conf_password,new_username
    new_user_label=Label(reg_page,text='Enter new Username',bg="#9BCD9B")
    new_user_label.place(x=10,y=10)
    new_pass_label=Label(reg_page,text='Enter new Password',bg="#9BCD9B")
    new_pass_label.place(x=10,y=40)
    conform_pass_label=Label(reg_page,text='Conform Password',bg="#9BCD9B")
    conform_pass_label.place(x=10,y=70)

    new_username=Entry(reg_page,width=26)
    new_username.place(x=140,y=10)
    new_password=Entry(reg_page,width=26)
    new_password.place(x=140,y=40)
    conf_password=Entry(reg_page,width=26)
    conf_password.place(x=140,y=70)
   
    submet=Button(reg_page,text='Submet',font=('BLOD',8),command=send)
    submet.place(x=80,y=125)



register=Button(log_page,text='Register',font=('BLOD',8),command=new_register)
register.place(x=135,y=142)

login_button=Button(log_page,text='Login',font=('BLOD',8),command=login)
login_button.place(x=140,y=100)

file_size = os.path.getsize('database.db')
print("File Size is :", file_size, "bytes")


root.mainloop()