from tkinter import *
from PIL import ImageTk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def clear():
    emailE.delete(0, END)
    userE.delete(0, END)
    passE.delete(0, END)
    conE.delete(0, END)
    check.set(0)

def signup():
    email=emailE.get()
    username=userE.get().lower()
    password=passE.get()
    confirmP=conE.get()
    checkB=check.get()

    if email=="" or username=="" or password==""or confirmP=="":
        MessageBox.showerror("ERROR ❎", "All fields are required")
    elif password != confirmP:
        MessageBox.showerror("ERROR ❎", "Your password did not match")
    elif checkB==0:
        MessageBox.showerror("ERROR ❎", "Accept Terms & Condtions to proceed")
    else:
        con = mysql.connect (host= "localhost", user="win", password="", database="login details")
        mycursor = con.cursor()
        mycursor.execute("select * from login where username='"+username +"'")
        row = mycursor.fetchone()
        mycursor.execute("select * from login where email='"+email +"'")
        rows = mycursor.fetchone()
        if rows !=None:
            MessageBox.showerror("ERROR ❎", "Email is already registered")
        elif row !=None:
            MessageBox.showerror("ERROR ❎", "Sorry, that username is taken")
        elif len(password) < 6 or len(password) >15:
            MessageBox.showerror("ERROR ❎", "Your password must be 6 - 15 characters long")
        else:
            mycursor.execute("INSERT INTO LOGIN (EMAIL, USERNAME, PASSWORD) VALUES ('"+ email +"', '"+ username +"', '"+ password +" ')")
            mycursor.execute("commit")
            con.close()
            clear()
            MessageBox.showinfo("SUCCESS ✅", "Registration Successfully")
            win.destroy()
            import login_page

def login_page():
    win.destroy()
    import login_page


win=Tk()
win.title('Sign Up Page')
win.resizable(0,0)
bg=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/images.bg.jpg')

bgL=Label(win, image=bg).grid ()

bgF=Frame(win, bg='white')
bgF.place(x=554, y=100)

heading=Label(bgF, text="CREATE AN ACCOUNT 🔓", font=("Cambria",18, "bold"), bg="White", fg="firebrick1")
heading.grid(row=0, column=0, padx=10, pady=10)
emailL=Label(bgF, text='Email', font=("Candara", 11, "bold"), fg="firebrick1", bg="White")
emailL.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))
emailE=Entry(bgF, width=30,font=("Candara",11, "bold"), bd=0, bg="firebrick1", fg="white")
emailE.grid(row=2, column=0, sticky='w', padx=25)

userL=Label(bgF, text='Username', font=("Candara", 11, "bold"), fg="firebrick1", bg="White")
userL.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))
userE=Entry(bgF, width=30,font=("Candara",11, "bold"), bd=0, bg="firebrick1", fg="white")
userE.grid(row=4, column=0, sticky='w', padx=25)

passL=Label(bgF, text='Password', font=("Candara", 11, "bold"), fg="firebrick1", bg="White")
passL.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))
passE=Entry(bgF, width=30,font=("Candara",11, "bold"), bd=0, bg="firebrick1", fg="white")
passE.grid(row=6, column=0, sticky='w', padx=25)

conL=Label(bgF, text='Confirm Password', font=("Candara", 11, "bold"), fg="firebrick1", bg="White")
conL.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))
conE=Entry(bgF, width=30,font=("Candara",11, "bold"), bd=0, bg="firebrick1", fg="white")
conE.grid(row=8, column=0, sticky='w', padx=25)
check= IntVar()
tc=Checkbutton(bgF, text='I agree to the Terms & Condition', font=("Candara", 10, "bold"),
                fg="firebrick1", bg="White", activeforeground="firebrick1", activebackground="White", cursor='hand2', variable=check)
tc.grid(row=9, column=0,sticky='w', padx=15, pady=10)

signB=Button(bgF, text="Sign Up", font=("Candara", 15, "bold"), fg="White", bg="firebrick1",
                activebackground="firebrick1", activeforeground="White", cursor="hand2",
                bd=0, width=20, command=signup)
signB.grid(row=10, column=0, padx=15, pady=10)

sigL=Label(bgF, text="Aleady have an account?", font=("Candara", 10, "bold"), 
            fg="firebrick1", bg="White")
sigL.grid(row=11, column=0, sticky='w', pady=30, padx=15)

newAB=Button(bgF, text="Log in", font=("Candara", 10, "bold underline"), fg="blue", bg="white",
                activebackground="white", activeforeground="blue", cursor="hand2",
                bd=0, command=login_page)
newAB.place(x=165, y=402)

win.mainloop()

