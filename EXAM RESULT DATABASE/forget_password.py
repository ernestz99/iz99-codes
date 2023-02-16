from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def submit():
    username=usernameE.get()
    password=passE.get()
    confirmP=confE.get()

    if username=="" or password=="" or confirmP=="":
        MessageBox.showerror("ERROR ❎", "All fields are required")
    elif password != confirmP:
        MessageBox.showerror("ERROR ❎", "Your new password did not match")
    else:
        con = mysql.connect (host= "localhost", user="win", password="", database="login details")
        mycursor = con.cursor()
        mycursor.execute("select * from login where username='"+username +"'")
        row = mycursor.fetchone()
        if row==None:
            MessageBox.showerror("ERROR ❎", "Username never exist")
        elif len(password) < 6 or len(password) >15:
            MessageBox.showerror("ERROR ❎", "Your new password must be 6 - 15 characters long")
        else:
            mycursor.execute("UPDATE LOGIN SET PASSWORD='"+ password +"' WHERE USERNAME='"+username+"' ")
            mycursor.execute("commit")
            con.close()
            MessageBox.showinfo("SUCCESS ✅", "Password is reset")
            win.destroy()
            import login_page
            
win=Tk()
win.title('Forget Password Page')
win.resizable(0,0)
bg=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/background.jpg')

bgL=Label(win, image=bg).grid ()

heading=Label(win, text="RESET PASSWORD 🔂", font=("Verdana",16, "bold"), bg="White", fg="magenta2")
heading.place(x=480, y=60)

userL=Label(win, text='Username', font=("Verdana", 12), fg="magenta2", bg="White").place(x=470, y=130)
usernameE=Entry(win, width=25,font=("Verdana",10, "bold"), bd=0, fg="magenta2")
usernameE.place(x=470, y=160)
usernameF=Frame(win, width=250, height=2, bg="orchid1").place(x=470, y=180)

passL=Label(win, text='Password', font=("Verdana", 12), fg="magenta2", bg="White").place(x=470, y=210)
passE=Entry(win, width=25,font=("Verdana",10, "bold"), bd=0, fg="magenta2")
passE.place(x=470, y=240)
passF=Frame(win, width=250, height=2, bg="orchid1").place(x=470, y=260)

confL=Label(win, text='Confirm Password', font=("Verdana", 12), fg="magenta2", bg="White").place(x=470, y=290)
confE=Entry(win, width=25,font=("Verdana",10, "bold"), bd=0, fg="magenta2")
confE.place(x=470, y=320)
confF=Frame(win, width=250, height=2, bg="orchid1").place(x=470, y=340)

subB=Button(win, text="Submit", font=("Candara", 14, "bold"), fg="White", bg="magenta2",
                activebackground="magenta2", activeforeground="White", cursor="hand2",
                bd=0, width=25, command=submit)
subB.place(x=470, y=390)


win.mainloop()