from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def forget_p():
    win.destroy()
    import forget_password
    

def login():
    username =usernameE.get().lower()
    password =passE.get()
    if username == "" or password == "" or username=="Username" or password=="Password":
        MessageBox.showerror("ERROR ❎", "All fields are required")
    else:
        con = mysql.connect (host= "localhost", user="win", password="", database="login details")
        mycursor = con.cursor()
        mycursor.execute("select * from login where username='"+username +"' and password='"+password+"' ")
        row = mycursor.fetchone()
        if row==None:
            MessageBox.showerror("ERROR ❎", "Invalid username or password")
        elif username == 'admin' or password == 'admin123 ':
            MessageBox.showinfo("WELCOME 🌐", "Welcome Admin")
            win.destroy()
            import admin_page
        else:
            MessageBox.showinfo("WELCOME 🌐", "Login Successful")
            win.destroy()
            import homepage

def sign_up():
    win.destroy()
    import signup_page

def hide():
    closeye.config(file='EXAM RESULT DATABASE/closeye.png')
    passE.config(show='*')
    eyeB.config(command=show)

def show():
    closeye.config(file='EXAM RESULT DATABASE/openeye.png')
    passE.config(show='') 
    eyeB.config(command=hide)

def user_enter(event):
    if usernameE.get()== 'Username':
        usernameE.delete(0, END)

def pass_enter(event):
    if passE.get()== 'Password':
        passE.delete(0, END)

win=Tk()
win.geometry("990x660")
win.resizable(0,0)
win.title("Login Page")

bgImage=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/bg.jpg')

bgLabel=Label(win, image=bgImage)
bgLabel.place (x=0,y=0)

heading=Label(win, text="USER LOGIN 🔒", font=("Cambria",20, "bold"), bg="White", fg="firebrick1")
heading.place(x=618, y=120)

usernameE=Entry(win, width=25,font=("Cambria",11, "bold"), bd=0, fg="firebrick1")
usernameE.place(x=578, y=200)
usernameE.insert(0,"Username")
usernameE.bind('<FocusIn>', user_enter)
usernameF=Frame(win, width=250, height=2, bg="firebrick1").place(x=578, y=222,)

passE=Entry(win, width=25,font=("Cambria",11, "bold"), bd=0, fg="firebrick1")
passE.place(x=578, y=260)
passE.insert(0,"Password")
passE.bind('<FocusIn>', pass_enter)
passF=Frame(win, width=250, height=2, bg="firebrick1").place(x=578, y=282,)
closeye=PhotoImage(file='EXAM RESULT DATABASE/closeye.png')
eyeB=Button(win, image=closeye, bd=0, bg="White", activebackground="White",cursor="hand2", command=show)
eyeB.place(x=800, y=250)
passE.config(show='*')


forgetB=Button(win, text='Forget Password?', font=("Cambria",11, "bold"), bd=0, bg="White", 
                activebackground="White", activeforeground="firebrick1",
                fg="firebrick1", cursor="hand2", command=forget_p)
forgetB.place(x=700, y=295)

loginB=Button(win, text="Login", font=("Candara", 17, "bold"), fg="White", bg="firebrick1",
                activebackground="firebrick1", activeforeground="White", cursor="hand2",
                bd=0, width=20, command=login)
loginB.place(x=575, y=350)

orL=Label(win, text="----------------------- OR -----------------------", font=("Candara", 15, "bold"), 
            fg="firebrick1", bg="White")
orL.place(x=575, y=410)

fb=PhotoImage(file='EXAM RESULT DATABASE/facebook.png')
fbL=Label(win, image=fb, bg="white")
fbL.place(x=640, y=440)

google=PhotoImage(file='EXAM RESULT DATABASE/google.png')
gL=Label(win, image=google, bg="white")
gL.place(x=700, y=440)

twitter=PhotoImage(file='EXAM RESULT DATABASE/twitter.png')
tL=Label(win, image=twitter, bg="white")
tL.place(x=760, y=440)

sigL=Label(win, text="Don't have an account?", font=("Candara", 11, "bold"), 
            fg="firebrick1", bg="White")
sigL.place(x=580, y=490)

newAB=Button(win, text="Sign Up", font=("Candara", 11, "bold underline"), fg="blue", bg="white",
                activebackground="white", activeforeground="blue", cursor="hand2",
                bd=0, command=sign_up)
newAB.place(x=755, y=490)

win.mainloop()

