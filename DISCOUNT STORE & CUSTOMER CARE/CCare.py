from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import ImageTk
import pyttsx3 #pip install pyttsx3 module

def call_us():
    def talk():
        def tc():
            cal.pack_forget()
            pyttsx3.speak ("Hi there! I'm Zee.......Thanks for getting in touch. How can i help you?")
        def exi():
            talk_win.destroy()
            import CCare
        call_win.destroy()
        talk_win = Tk()
        talk_win.config(background='white')
        talk_win.overrideredirect(True)
        screen_width = talk_win.winfo_screenwidth()
        screen_height = talk_win.winfo_screenheight()
        window_width = 500
        window_height = 250
        x_coord = (screen_width/2) - (window_width/2)
        y_coord = (screen_height/2) - (window_height/2)
        talk_win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

        call2 = ImageTk.PhotoImage(file='DISCOUNT STORE & CUSTOMER CARE/call2.png')
        Label(talk_win, image=call2, bg='white').pack(pady=30)
        cal= Button(talk_win, text='Call',bd=0, bg='deep sky blue',activebackground='deep sky blue', 
                        font='bold',fg='white', activeforeground='white',width=15, command=tc)
        cal.pack()
        Button(talk_win, text='Hang Up',bd=0, bg='orange red',activebackground='orange red', 
                        font='bold',fg='white', activeforeground='white',width=15, command=exi).pack()
       
        talk_win.mainloop()

    def main():
        call_win.destroy()
        import CCare
    win.destroy()
    call_win = Tk()
    call_win.config(background='white')
    call_win.overrideredirect(True)
    screen_width = call_win.winfo_screenwidth()
    screen_height = call_win.winfo_screenheight()
    window_width = 500
    window_height = 400
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    call_win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

    grp = ImageTk.PhotoImage(file='DISCOUNT STORE & CUSTOMER CARE/grp.png')
    Label(call_win, image=grp, bg='white').pack(pady=20)
    Label(call_win, text="Hi, Let's help you today.",font=('cambria',12,'bold'),bg='white').pack(pady=15)
    Label(call_win, text="Phones lines are available between 8:00 AM and 5:00 PM on weekdays.",
                    font=('cambria',10),bg='white').pack()
    Label(call_win, text="Tap on the number to call ",font=('cambria',10),bg='white').pack()
    back = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/back.png")
    Button(call_win, text='091000CALL247MiNiSTORE',bg='white', activebackground='white',font='bold',command=talk).pack(pady=25)
    Button(call_win, text='',font=('cambria',12,'bold'),image=back, compound='left', 
                        bg='white', bd=0, activebackground='white', command=main).pack()
    call_win.mainloop()

def mail_us():
    def main():
        mail_win.destroy()
        import CCare
    win.destroy()
    mail_win = Tk()
    mail_win.config(background='white')
    mail_win.overrideredirect(True)
    screen_width = mail_win.winfo_screenwidth()
    screen_height = mail_win.winfo_screenheight()
    window_width = 500
    window_height = 400
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    mail_win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

    grp = ImageTk.PhotoImage(file='DISCOUNT STORE & CUSTOMER CARE/grp.png')
    Label(mail_win, image=grp, bg='white').pack(pady=20)
    Label(mail_win, text="Hi, Let's help you today.",font=('cambria',12,'bold'),bg='white').pack(pady=15)
    Label(mail_win, text="Send us a mail through the Store mail below ",font=('cambria',10),bg='white').pack()
    back = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/back.png")
    Label(mail_win, text='ministores247@gmail.com',bg='white', activebackground='white',font='bold').pack(pady=25)
    back = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/back.png")
    Button(mail_win, text='',font=('cambria',12,'bold'),image=back, compound='left', 
                        bg='white', bd=0, activebackground='white', command=main).pack()
    mail_win.mainloop()

def faqq():
    def main():
        faqq_win.destroy()
        import CCare

    win.destroy()
    faqq_win = Tk()
    faqq_win.config(background='white')
    faqq_win.overrideredirect(True)
    screen_width = faqq_win.winfo_screenwidth()
    screen_height = faqq_win.winfo_screenheight()
    window_width = 500
    window_height = 300
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    faqq_win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

    ff = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/faq2.png")
    back = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/back.png")

    Label(faqq_win, image = ff,bd=0,bg='white').pack(pady=15)
    Label(faqq_win, text='FREQUENTLY ASKED QUESTIONS',bd=0, font=('cambria',18,'bold'),bg='white', justify=LEFT).pack(pady=10)
    Button(faqq_win, text='⚫ HOW DO YOU PLACE ORDER?  ➕',bd=0, font=('cambria',12,'bold'),bg='white').place(x=20, y=150)
    Button(faqq_win, text='⚫ WHAT PAYMENT TYPES DO YOU ACCEPT?  ➕',bd=0, 
                    font=('cambria',12,'bold'),bg='white', justify=LEFT).place(x=20, y=200)
    Button(faqq_win, text='⚫ DO YOU DELIVER?  ➕',bd=0, font=('cambria',12,'bold'),bg='white', justify=LEFT).place(x=20, y=250)
    Button(faqq_win, image=back,bg='white',bd=0, justify=LEFT, command=main).place(x=20, y=100)

    faqq_win.mainloop()

def chatt():
    def sub():
        txt = ent.get(1.0,'end-1c')
        if txt =="":
            return True
        else:
            ent.delete(1.0,'end-1c')
            Button(chatt_win, image=send,bd=0, background='white', activebackground='white').place(x=440, y=420)
            wrapper2 = Frame(chatt_win, bd=0, height=100, width=100)
            wrapper2.grid(row=2,column=2, pady=20,padx=25)
            Label(chatt_win, image=you, bg='white').grid(row=2, column=3,pady=10)
            Label(wrapper2, text=f'''{txt}
               ''', justify=LEFT, font='bold').pack(padx=20)
            wrapper3 = Frame(chatt_win, bd=0, height=100, width=200)
            wrapper3.grid(row=3,column=1, pady=20)
            Label(chatt_win, image=admin, bg='white').grid(row=3, column=0,pady=10)
            Label(wrapper3, text='''    Hmmm. Great question
    We will get back to you
    Ciao!!''', justify=LEFT, font='bold').pack()
            ent.delete(1.0,'end-1c')

    def main():
        chatt_win.destroy()
        import CCare
    win.destroy()
    chatt_win = Tk()
    chatt_win.config(background='white')
    chatt_win.overrideredirect(True)
    screen_width = chatt_win.winfo_screenwidth()
    screen_height = chatt_win.winfo_screenheight()
    window_width = 500
    window_height = 480
    x_coord = (screen_width/2) - (window_width/2)
    y_coord = (screen_height/2) - (window_height/2)
    chatt_win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

    Label(chatt_win, text='', font=('cambria',20,'bold'),bg='white').grid(row=0,column=2, padx=10,pady=20)
    Label(chatt_win, text='CHAT WITH US', font=('cambria',20,'bold'),bg='white').place(x=150,y=20)
    admin = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/admin.png")
    back = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/back.png")
    send = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/send.png")
    you = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/you.png")
    Label(chatt_win, image=admin, bg='white').grid(row=1, column=0,pady=10)
    wrapper1 = Frame(chatt_win, bd=0, height=100, width=300)
    wrapper1.grid(row=1,column=1)
    
    Label(wrapper1, text='''    Hi there! I'm Zee.
    Thanks for getting in touch.
    How can i help you?''', justify=LEFT, font='bold').pack()

    ent = Text(chatt_win, bg='white',bd=1, width=47,height=2, font=8)
    ent.place(x=20, y=420)
    Button(chatt_win, image=send,bd=0, background='white', activebackground='white',command=sub).place(x=440, y=420)
    bak= Button(chatt_win, image=back, bd=0, bg='white',activebackground='white', command=main).place(x=110, y=20)
    chatt_win.mainloop()

win = Tk()
win.config(background='white')
win.overrideredirect(True)
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
window_width = 500
window_height = 400
x_coord = (screen_width/2) - (window_width/2)
y_coord = (screen_height/2) - (window_height/2)
win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

Label(win, text='CUSTOMER CARE SERVICE', font=('cambria',20,'bold'),bg='white').pack(pady=20)

frame=LabelFrame(win, text='Get Help', font=('cambria',15,'bold'), height=250, bg='white')
frame.pack(fill='both', padx=20, pady=10)

call= ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/call.png")
chat = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/chat1.png")
mail = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/mail.png")
faq = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/faq.png")
back = ImageTk.PhotoImage(file="DISCOUNT STORE & CUSTOMER CARE/back.png")

but = Button(frame, text='   Call Us      ',font=('cambria',15,'bold'),image=call, compound='left', 
                    bg='white', bd=0, activebackground='white', command=call_us).place(x=20, y=20)
but1 = Button(frame, text='   Chat Us ',font=('cambria',15,'bold'),image=chat, compound='left', 
                    bg='white', bd=0, activebackground='white', command=chatt).place(x=20, y=70)
but1 = Button(frame, text='   Send An Email',font=('cambria',15,'bold'),image=mail, compound='left', 
                    bg='white', bd=0, activebackground='white', command=mail_us).place(x=20, y=120)
but1 = Button(frame, text='   FAQs         ',font=('cambria',15,'bold'),image=faq, compound='left', 
                    bg='white', bd=0, activebackground='white', command=faqq).place(x=20, y=170)

Button(win, text='Exit',bd=0, bg='orange red',activebackground='orange red', 
                font='bold',fg='white', activeforeground='white',width=15, command=win.destroy).pack()

win.mainloop()
