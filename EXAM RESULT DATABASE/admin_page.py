from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

mydb = mysql.connect (host= "localhost", user="win", password="", database="exam result")
cursor = mydb.cursor()

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=i)
cursor.execute("SELECT id, name, exam_num,gender FROM data")
rows = cursor.fetchall()


def show(info):
    trv1.delete(*trv1.get_children())
    for i in info:
        trv1.insert('', 'end', values=i)
cursor.execute("SELECT name, java, python, dart, html, php FROM data")
info = cursor.fetchall()

def search():
    q2 = q.get()
    cursor.execute("SELECT id, name, exam_num, gender FROM data WHERE name='"+q2+"' OR id='"+q2+"'")
    rows = cursor.fetchall()
    update(rows)

def clear():
    cursor.execute("SELECT id, name, exam_num, gender FROM data")
    rows = cursor.fetchall()
    update(rows)

def clear1():
    cursor.execute("SELECT name, java, python, dart, html, php FROM data")
    info = cursor.fetchall()
    show(info)

def getrow(event):
    rowid = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t1.set(item['values'] [0])
    t2.set(item['values'] [1])
    t3.set(item['values'] [2])
    t4.set(item['values'] [3])

def update_stud():
    iD = t1.get()
    name = t2.get().capitalize()
    exam_num = t3.get()
    gender = t4.get().upper()
    java = t5.get()
    python = t6.get()
    dart = t7.get()
    html = t8.get()
    php = t9.get()
    if (iD=="" or name=="" or exam_num=="" or gender=="" or java=="" or python=="" or dart=="" or html=="" or php==""):
        MessageBox.showerror("ERROR ❌", "All fields are required")
    else:
        if MessageBox.askyesno('Please Confrim', 'Are you sure you want to edit this Student Data?'):
            cursor.execute(" Update data set name='"+ name +"', exam_num='"+ exam_num +"', gender='"+ gender+"', java='"+ java+"', python='"+ python+"', dart='"+ dart+"', html='"+ html+"', php='"+ php+"' where id='"+iD+"' ")
            cursor.execute("commit")
            clear()
            clear1()
            MessageBox.showinfo("Edit Status", "Student data successfully edited")
            ent.delete(0, 'end')
            ent1.delete(0, 'end')
            ent2.delete(0, 'end')
            ent3.delete(0, 'end')
            ent4.delete(0, 'end')
            ent5.delete(0, 'end')
            ent6.delete(0, 'end')
            ent7.delete(0, 'end')
            ent8.delete(0, 'end')
        else:
            return True

def add():
    iD = t1.get()
    name = t2.get().capitalize()
    exam_num = t3.get()
    gender = t4.get().upper()
    java = t5.get()
    python = t6.get()
    dart = t7.get()
    html = t8.get()
    php = t9.get()
    if (iD=="" or name=="" or exam_num=="" or gender=="" or java=="" or python=="" or dart=="" or html=="" or php==""):
        MessageBox.showerror("ERROR ❌", "All fields are required")
    else:
        cursor.execute("Insert into data values ('"+ iD +"','"+ name +"', '"+ exam_num+"','"+ gender+"', '"+ java+"', '"+ python+"','"+ dart+"', '"+ html+"', '"+ php+"')")
        cursor.execute("commit")
        clear()
        clear1()
        MessageBox.showinfo("Add Status", "Student data successfully added")
        ent.delete(0, 'end')
        ent1.delete(0, 'end')
        ent2.delete(0, 'end')
        ent3.delete(0, 'end')
        ent4.delete(0, 'end')
        ent5.delete(0, 'end')
        ent6.delete(0, 'end')
        ent7.delete(0, 'end')
        ent8.delete(0, 'end')

def dele():
    student_id = t1.get()
    if(student_id == ""):
        MessageBox.showerror("Delete Status", "Enter sudent ID to delete")
    else:
        if MessageBox.askyesno('Confrim Delete?', 'Are you sure you want to delete this Student Data?'):
            cursor.execute("delete from data where id='"+student_id+"' ")
            cursor.execute("commit")
            clear()
            clear1()
            MessageBox.showinfo("Delete Status", "Student data successfully deleted")
        else:
            return True

def exi():
    root.destroy()
    import login_page

root=Tk()
root.title('Admin Page')
root.geometry('1000x850')
root.resizable(0,0)
style = ttk.Style()
style.theme_use ('clam')

q = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()
t8 = StringVar()
t9 = StringVar()

title = Label (root, text='ADMIN DASHBOARD', font=('',18,'bold')).pack(fill='both', padx=20, pady=5)
wrapper1 = LabelFrame (root, text='Admin Tools', font='bold')
wrapper1.pack(fill='both', padx=20, pady=2)

wrapper2 = LabelFrame (root, text='Search', font='bold', height=150)
wrapper2.pack(fill='both', padx=20, pady=10)

wrapper3 = LabelFrame (root, text='Student Data', font='bold')
wrapper3.pack(fill='both', expand='yes', padx=20, pady=10)

wrapper4 = LabelFrame (root, text='Student Results', font='bold')
wrapper4.pack(fill='both', expand='yes', padx=20, pady=10)

#wrapper1
lbl = Label(wrapper1, text='Student ID')
lbl.grid(row=0, column=0, padx=5, pady=3)
ent =Entry (wrapper1, textvariable=t1, bd=2)
ent.grid(row=0, column=1,sticky='W', padx=2, pady=3)

lbl1 = Label(wrapper1, text='Student Name')
lbl1.grid(row=0, column=2, padx=5, pady=3)
ent1 =Entry (wrapper1, textvariable=t2, bd=2)
ent1.grid(row=0, column=3, padx=5, pady=3)

lbl2 = Label(wrapper1, text='Exam Number')
lbl2.grid(row=0, column=4, padx=5, pady=3)
ent2 =Entry (wrapper1, textvariable=t3, bd=2)
ent2.grid(row=0, column=5, padx=5, pady=3)

lbl3 = Label(wrapper1, text='Gender')
lbl3.grid(row=0, column=6, padx=5, pady=3)
ent3 =Entry (wrapper1, textvariable=t4, bd=2)
ent3.grid(row=0, column=7, padx=5, pady=3)

title1 = Label (wrapper1, text='ENTER SCORES ✍️', font=('',8,'bold')).grid(row=1, column=0, padx=10, pady=10)

lbl4 = Label(wrapper1, text='Java')
lbl4.grid(row=2, column=0, padx=5, pady=3)
ent4 =Entry (wrapper1, textvariable=t5, width=10, bd=2)
ent4.grid(row=2, column=1,sticky='W', pady=3)

lbl5 = Label(wrapper1, text='Python')
lbl5.grid(row=3, column=0, pady=3)
ent5 =Entry (wrapper1, textvariable=t6, width=10, bd=2)
ent5.grid(row=3, column=1,sticky='W', pady=3)

lbl6 = Label(wrapper1, text='Dart')
lbl6.grid(row=4, column=0, padx=5, pady=3)
ent6 =Entry (wrapper1, textvariable=t7, width=10, bd=2)
ent6.grid(row=4, column=1,sticky='W', pady=3)

lbl7 = Label(wrapper1, text='HTML')
lbl7.grid(row=5, column=0, padx=5, pady=3)
ent7 =Entry (wrapper1, textvariable=t8, width=10, bd=2)
ent7.grid(row=5, column=1,sticky='W', pady=3)

lbl8 = Label(wrapper1, text='PHP')
lbl8.grid(row=6, column=0, padx=5, pady=3)
ent8 =Entry (wrapper1, textvariable=t9, width=10, bd=2)
ent8.grid(row=6, column=1,sticky='W', pady=3)

btn = Button(wrapper1, text='Edit', command=update_stud, width=10).grid(row=7, column=1, padx=5, pady=10)
btn1 = Button(wrapper1, text='Add New', width=10, command=add).grid(row=7, column=0, padx=5, pady=10)
btn2 = Button(wrapper1, text='Delete', width=10, command=dele).grid(row=7, column=2, padx=5, pady=10)
btn3 = Button(wrapper1, text='Log out', width=15, command=exi, bd=1, activebackground='red', activeforeground='white')
btn3.grid(row=7, column=7, padx=5, pady=10)

#wrapper2
sl = Label(wrapper2, text='ID/Name').pack(side=LEFT, padx=10)
se = Entry(wrapper2, textvariable=q, bd=2)
se.pack(side=LEFT, padx=6)
but = Button(wrapper2, text='Search', command= search).pack(side=LEFT, padx=6)
but1 = Button(wrapper2, text='Clear', command= clear).pack(side=LEFT, padx=6)

#wrapper3
trv= ttk.Treeview(wrapper3, columns=(1,2,3,4), show='headings', height='8')
trv.pack(side=LEFT)
trv.place(x=0,y=0)
trv.column(1,anchor=CENTER, stretch=NO, width=250, minwidth=250)
trv.column(2,anchor=CENTER, stretch=NO, width=250, minwidth=250)
trv.column(3,anchor=CENTER, stretch=NO, width=250, minwidth=250)
trv.column(4,anchor=CENTER, stretch=NO, width=200, minwidth=200)

trv.heading(1, text='Student ID')
trv.heading(2, text='Student Name')
trv.heading(3, text='Exam number')
trv.heading(4, text='Gender')
trv.bind('<Double 1>', getrow)
update(rows)

#wrapper4
trv1= ttk.Treeview(wrapper4, columns=(1,2,3,4,5,6), show='headings', height='8')
trv1.pack(side=LEFT)
trv1.place(x=0,y=0)
trv1.column(1,anchor=CENTER, stretch=NO, width=200, minwidth=200)
trv1.column(2,anchor=CENTER, stretch=NO, width=150, minwidth=150)
trv1.column(3,anchor=CENTER, stretch=NO, width=150, minwidth=150)
trv1.column(4,anchor=CENTER, stretch=NO, width=150, minwidth=150)
trv1.column(5,anchor=CENTER, stretch=NO, width=150, minwidth=150)
trv1.column(6,anchor=CENTER, stretch=NO, width=150, minwidth=150)

trv1.heading(1, text='Student Name')
trv1.heading(2, text='Java')
trv1.heading(3, text='Python')
trv1.heading(4, text='Dart')
trv1.heading(5, text='HTML')
trv1.heading(6, text='PHP')
show(info)

root.mainloop()