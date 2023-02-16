from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
from PIL import ImageTk

def num_enter(event):
    if bgE.get()== "    Examination number":
        bgE.delete(0, END)

def submit():
    exam_num = bgE.get()
    if(exam_num == "" or exam_num == "    Examination number"):
        MessageBox.showerror("ERROR ❎", "Enter your examination number ")
    else:
        con = mysql.connect (host= "localhost", user="win", password="", database="exam result")
        cursor = con.cursor()
        cursor.execute("select * from data where exam_num='"+exam_num +"' ")
        row = cursor.fetchone()
        if row==None:
            MessageBox.showerror("ERROR ❎", "Invalid examination number. Please check!")
        else:
            def update(data):
                for i in data:
                    trv.insert('', 'end', values=i)
            con = mysql.connect (host= "localhost", user="win", password="", database="exam result")
            cursor = con.cursor()
            cursor.execute("SELECT id, exam_num,gender FROM data WHERE exam_num='"+exam_num +"' ")
            data = cursor.fetchall()

            def show(info):
                for i in info:
                    trv1.insert('', 'end', values=i)
            cursor.execute("SELECT java, python, dart, html, php FROM data WHERE exam_num='"+exam_num +"' ")
            info = cursor.fetchall()

            def check():
                cursor.execute("SELECT java, python, dart, html, php FROM data WHERE exam_num='"+exam_num +"' ")
                total = cursor.fetchall() 
                score = sum(map(sum,total))
                per = (score / 500 * 100)
                
                lbl2 = Label(wrapper3, text=f"Total Scored: {score}", bd=0, 
                                background='white', font=('Bahnschrift SemiLight', 18, 'bold'))
                lbl2.place(x=390,y=250)
                lbl3 = Label(wrapper3, text="Total Marks: 500", bd=0, 
                                background='white', font=('Bahnschrift SemiLight', 18, 'bold'))
                lbl3.place(x=390,y=300)

                lbl4 = Label(wrapper3, text=f"Percentage: {per}%", bd=0, 
                                background='white', font=('Bahnschrift SemiLight', 18, 'bold'))
                lbl4.place(x=390,y=350)

            def login():
                root.destroy()
                import login_page
            
            def home():
                root.destroy()
                import homepage

            win.destroy()
            root=Tk()
            root.title('Student Page')
            root.config(bg='white')
            root.geometry('1000x850')
            root.resizable(0,0)
            style = ttk.Style()
            style.theme_use ('clam')
            style.configure('Treeview.Heading', font=('',10, 'bold'))

            title = Label (root, text='STUDENT DASHBOARD', font=('',18,'bold'), bg='white').pack(fill='both', padx=20, pady=5)

            wrapper1 = LabelFrame (root, text='Welcome', font='bold',bg='white', height=150)
            wrapper1.pack(fill='both', padx=20, pady=10)

            wrapper2 = LabelFrame (root, text='Your Data',bg='white', font='bold', height=150)
            wrapper2.pack(fill='both', padx=20, pady=10)

            wrapper3 = LabelFrame (root, text='Your Result',bg='white', font='bold')
            wrapper3.pack(fill='both', expand='yes', padx=20, pady=10)

            #wrapper1
            w1Image=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/images/logo.png')
            lbl = Label(wrapper1, image=w1Image, bd=0, bg='white')
            lbl.grid(row=0, column=0, padx=20, pady=3)

            cursor.execute("select name from data where exam_num='"+exam_num +"'")
            rows = cursor.fetchall()

            ent=Entry(wrapper1, bd=0, font=('Copperplate Gothic Bold', 20), width=20)
            ent.grid(row=0, column=1, padx=5, pady=3)
            
            for row in rows:
                ent.insert (0, row [0])
                ent.config(state=DISABLED, disabledbackground='white', disabledforeground='black')

            
            #wrapper2
            trv= ttk.Treeview(wrapper2, columns=(1,2,3), show='headings', height='3')
            trv.pack()
            trv.place(x=80,y=20)
            trv.column(1,anchor=CENTER, stretch=NO, width=250, minwidth=250)
            trv.column(2,anchor=CENTER, stretch=NO, width=250, minwidth=250)
            trv.column(3,anchor=CENTER, stretch=NO, width=250, minwidth=250)

            trv.heading(1, text='Student ID')
            trv.heading(2, text='Exam number')
            trv.heading(3, text='Gender')
            update(data)


            #wrapper3
            trv1= ttk.Treeview(wrapper3, columns=(1,2,3,4,5), show='headings', height='3')
            trv1.pack(side=LEFT)
            trv1.place(x=50,y=20)
            trv1.column(1,anchor=CENTER, stretch=NO, width=200, minwidth=200)
            trv1.column(2,anchor=CENTER, stretch=NO, width=150, minwidth=150)
            trv1.column(3,anchor=CENTER, stretch=NO, width=150, minwidth=150)
            trv1.column(4,anchor=CENTER, stretch=NO, width=150, minwidth=150)
            trv1.column(5,anchor=CENTER, stretch=NO, width=150, minwidth=150)

            trv1.heading(1, text='Java')
            trv1.heading(2, text='Python')
            trv1.heading(3, text='Dart')
            trv1.heading(4, text='HTML')
            trv1.heading(5, text='PHP')
            show(info)

            w3Image=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/images/bulb.png')
            lbl1 = Label(wrapper3, image=w3Image, bd=0, background='white')
            lbl1.place(x=460,y=120)
            btn = Button(wrapper3, text='Calculate Total Score & Percentage', font=('bold'), command=check, bd=1, bg='dodgerblue', 
                        fg='white', activebackground='dodgerblue', activeforeground='white')
            btn.place(x=360,y=190)

            log=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/images/log.png')
            but2 = Button(wrapper3, image=log, bd=0, background='white', activebackground='white', command=home)
            but2.place(x=20,y=430)

            exi=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/images/exit.png')
            but3 = Button(wrapper3, image=exi, bd=0, background='white', activebackground='white', command=login)
            but3.place(x=900,y=430)




            root.mainloop()

win = Tk()
win.geometry("900x610")
win.title("Homepage")
win.geometry("1280x700")
win.config(bg="White")
win.resizable(0,0)
bgImage=ImageTk.PhotoImage(file='EXAM RESULT DATABASE/images/pic1.jpg')
bgL=Label(win, image=bgImage).grid()

icon=PhotoImage(file="EXAM RESULT DATABASE/images/student.png")
bgI=Label(win, image=icon,bd=0,bg='white').place(x=605, y=200)
bgE=Entry(win, bd=0, bg='white', fg='purple', font=('verdana', 12, 'bold'), width=20)
bgE.place(x=561, y=360)
bgE.insert(0,"    Examination number")
bgE.bind('<FocusIn>', num_enter)
bgF=Frame(win, width=235, height=2, bg="purple").place(x=558, y=380)

send=PhotoImage(file="EXAM RESULT DATABASE/images/submit1.png")

bgB=Button(win,image=send,bd=0,bg='white', 
                activebackground='white', cursor='hand2', command=submit)
bgB.place(x=615, y=390)

Label(win, text='The',fg='purple', font=('verdana', 12, 'bold'), bg='white').place(x=580, y=670)
Label(win, text='Sky',fg='white', font=('verdana', 12, 'bold'), bg='purple').place(x=620, y=670)
Label(win, text='is Your Limit....',fg='purple', font=('verdana', 12, 'bold'), bg='white').place(x=660, y=670)

win.mainloop()