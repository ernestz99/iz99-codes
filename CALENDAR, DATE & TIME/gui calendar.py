from tkinter import *
from datetime import *
import calendar

win=Tk()
win.title("Date,Time&Calendar")
#win.geometry("650x200")
win.config(bg="White")

def comm():
    win4=Tk()
    win4.title("Comment")
    win4.geometry("400x400")
    win4.config(bg="White")
    Label(win4, text="Enter your name ⬇ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").pack()
    a= Entry(win4, bg="Light grey", fg="Black",font=("Arial", 8))
    a.pack()
    Label(win4, text="Enter your e-mail ⬇ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").pack()
    b = Entry(win4, bg="Light grey", fg="Black",font=("Arial", 8))
    b.pack()
    Label(win4, text="Comment ⬇", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").pack()
    Text(win4,font=("Arial", 10), height=10, width=50, bg="Light grey", fg="Black").pack()
    Button(win4, text="submit", font=("Franklin Gothic Demi", 12), bg="Green",fg="White").pack()
    win4.mainloop()

def DT():
    win3=Tk()
    win3.title("Date & Time")
    win3.geometry("500x250")
    win3.config(bg="white")

    def checkT():
        now= datetime.now()
        x = now.strftime("%H: %M: %S")
        x1 = Label (win3, text= x, font=("Franklin Gothic Demi", 14), bg="White", fg="Black")
        x1.grid(row=5, column=1, padx=20)

    def check():
        today = date.today()
        c = today.year
        c1 = today.month
        c2 = today.day
        d = Label (win3,text= (c2,'-',c1,'-',c), font=("Franklin Gothic Demi", 14), bg="White", fg="Black")
        d.grid(row=4, column=1, padx=20)

    a = Label (win3, text="❏ Welcome to the Date & Time Application", font=("Franklin Gothic Demi", 14), bg="White", fg="Green").grid(row=0, column=1)
    a1 = Label (win3, text="Date ➠ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").grid(row=2, column=0)
    a2 = Label (win3, text="Time ➠ ", font=("Franklin Gothic Demi", 12), bg="White", fg="Black").grid(row=3, column=0)
    b = Button (win3, text="check date ✔️", font=("Franklin Gothic Demi", 12), bg="Green", fg="White",command= check).grid(row=2, column=1)
    b1 = Button (win3, text="check time ✔️", font=("Franklin Gothic Demi", 12), bg="Green", fg="White",command= checkT).grid(row=3, column=1)
    b2 = Button(win3, text="Exit ❎", font=("Comic Sans MS", 10), background="Dark Red", foreground="White", command=win3.destroy).grid(row=7, column=1)

def month():
    win2=Tk()
    win2.title("Calendar Month")
    win2.geometry("600x400")
    win2.config(bg="white")
    
    def view():
        g = int (c.get())
        h = int (e.get())
        i = Label(win2, text= calendar.month(g,h,w=2,l=1), font="consolas 10 bold", justify= LEFT, bg="White", fg="Black")
        i.grid(row=7, column=1, padx=20)

    a = Label (win2, text="❏ Welcome to the Calendar Application", font=("Franklin Gothic Demi", 14), bg="White", fg="Green").grid(row=0, column=1)
    b = Label (win2, text="CREATE YOUR CALENDAR ", font=("Franklin Gothic Demi", 10), bg="White", fg="Black").grid(row=1, column=1)
    b = Label (win2, text="Please Enter a Year ➠  ", font=("Franklin Gothic Demi", 14), bg="White", fg="Black").grid(row=2, column=0)
    c = Entry (win2,bg="Grey",fg="White", font=12, width=20)
    c.grid(row=2, column=1)
    d = Label (win2, text="Please Enter a Month ➠  ", font=("Franklin Gothic Demi", 14), bg="White", fg="Black").grid(row=3, column=0)
    e = Entry (win2,bg="Grey",fg="White", font=12, width=20)
    e.grid(row=3, column=1)
    f = Button(win2, text="✅", font=("Comic Sans MS", 14), bg="Dark Green", fg="White",width= 8, command=view).grid(row=4, column=1)
    f1 = Button(win2, text="❎", font=("Comic Sans MS", 14), background="Dark Red", foreground="White",width= 8, command=win2.destroy).grid(row=8, column=1)

    win2.mainloop()

def exi():
    win.destroy()
def view():
    def exi2():
        new.destroy()
    new=Tk()
    new.geometry("600x650")
    new.title("Calendar Year")
    new.config(bg="White")

    z= int(c.get())
    calend= calendar.calendar(z)
    f = Label (new, text= calend ,font="Consolas 10 bold", justify= LEFT, bg="White", fg="Black")
    f.grid(row=1, column=2, padx=20)
    e = Button(new, text="❎", font=("Comic Sans MS", 14), bg="Dark Red", fg="White",width=5, command=exi2)
    e.grid(row=2,column=2)

    new.mainloop()

menubar = Menu (win)

file= Menu(menubar, tearoff=0)
menubar.add_cascade(label= "🔓 Menu",font=("cambria bold", 12), menu= file)
file.add_command(label="➲ View a calendar month",font=("cambria", 10), command= month)
file.add_command(label="➲ Check date & time",font=("cambria", 10), command= DT)
file.add_separator()

sub_menu = Menu(file, tearoff=0)
file.add_cascade(label= "📌 More...",font=("cambria", 10), menu= sub_menu)
sub_menu.add_command(label="😎 Reaction",font=("cambria", 10), command= None)
sub_menu.add_command(label="✉ Comment",font=("cambria", 10), command= comm)
file.add_separator()
file.add_command(label="❎Exit",font=("cambria", 10), command=win.destroy)

hel = Menu(menubar,tearoff=0)
menubar.add_cascade(label= "🔧 Tools",font=("cambria bold", 12), menu= hel)
hel.add_command(label="Tk Help",font=("cambria", 10), command= None)
hel.add_command(label="Demo",font=("cambria", 10), command= None)
hel.add_separator()
hel.add_command(label="✨ More",font=("cambria", 10), command= None)

win.config(menu= menubar)

a = Label (win, text="DATE, TIME & CALENDAR ⏳ ", font=("Franklin Gothic Demi", 16), width= 25, bg="White", fg="Black").grid(row=0, column=1)
a2 = Button (win, text=" 🔐  ", font=16, width= 5, bg="White", fg="Black").grid(row=1, column=1)
b1 = Label (win, text="❏ Welcome to the Calendar Application", font=("Franklin Gothic Demi", 14), bg="White", fg="Green").grid(row=2, column=1)
b = Label (win, text="CREATE YOUR CALENDAR ", font=("Franklin Gothic Demi", 10), bg="White", fg="Black").grid(row=3, column=1)
b = Label (win, text="Please Enter a Year ➠   ", font=("Franklin Gothic Demi", 14), bg="White", fg="Black").grid(row=4, column=0)
c = Entry (win,bg="Grey",fg="White", font=12, width=20)
c.grid(row=4, column=1)
d = Button(win, text="✅", font=("Comic Sans MS", 14), bg="Dark Green", fg="White",width= 8, command=view).grid(row=4, column=2)

win.mainloop()