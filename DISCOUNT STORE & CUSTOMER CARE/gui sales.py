from tkinter import *
import tkinter.messagebox as Messagebox

def Ghelp():
    root.destroy()
    import CCare

def sub():
    def but2():
        bt1 = Button (frame2, text='Proceed to Pay',command=None).pack(pady=5)
        bt2 = Button (frame2, text='Complain', command= Ghelp).pack(pady=5)
    sales = ent.get()
    if sales == "":
        Messagebox.showerror('Error', 'Enter the goods num!!')
    else:
        sales = int(ent.get())
        if sales <1 or sales >5 :
          Messagebox.showerror('Error', "We don't have that, Choose again")
          ent.delete(0, END)
        elif sales == 1:
            b = 1500 * 0.15
            c = Label(frame2, text= f" The 15% discount price for SODA is ${b}", bg='white', font='bold').pack()
            but2()
        elif sales == 2:
            b = 900 * 0.15
            c = Label(frame2, text= f" The 15% discount price for MILK is ${b}", bg='white', font='bold').pack()
            but2()
        elif sales == 3:
            b = 1000 * 0.15
            c = Label(frame2, text= f" The 15% discount price for CHIPS is ${b}", bg='white', font='bold').pack()
            but2()
        elif sales == 4:
            b = 2500 * 0.15
            c = Label(frame2, text= f" The 15% discount price for BREAD is ${b}", bg='white', font='bold').pack()
            but2()
        else:
            b = 500 * 0.15
            c = Label(frame2, text= f" The 15% discount price for VEGETABLE is ${b}", bg='white', font='bold').pack()
            but2()

root = Tk()
root.title('247 MiNi STORE')
root.config(background='white')
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 800
window_height = 420
x_coord = (screen_width/2) - (window_width/2)
y_coord = (screen_height/2) - (window_height/2)
root.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

lab= Label(root, text= '247 MiNi STORE', 
                    bg='white', font=('cambria', 15, 'bold'))
lab.pack(pady=10)

frame = LabelFrame(root, text= 'What do you want to buy? (You will be given 15% Discount on our sales)', 
                        font=('cambria',12,'bold'), height=150, bg='white')
frame.pack(fill='both', padx=20, pady=10)

frame2 = LabelFrame(root, text='Total Discount Price', font=('cambria',12,'bold'), height=100, bg='white')
frame2.pack(fill='both', padx=20, pady=10)

lab2= Label(frame, text='1. SODA ($1500)', font=('verdana', 10), bg='white')
lab2.grid (row=0, column=0)
lab3= Label(frame, text='2. MILK ($900)', font=('verdana', 10), bg='white')
lab3.grid (row=1, column=0)
lab4= Label(frame, text='3. CHIPS ($1000)', font=('verdana', 10), bg='white')
lab4.grid (row=2, column=0)
lab5= Label(frame, text='4. BREAD ($2500)', font=('verdana', 10), bg='white')
lab5.grid (row=3, column=0)
lab6= Label(frame, text='5. VEGETABLE ($500)', font=('verdana', 10), bg='white')
lab6.grid (row=4, column=0)

lab1 = Label(frame, text='Enter goods num (1-5)', font=('cambria', 11, 'bold', 'underline'), bg='white')
lab1.grid (row=5, column=0, padx=10, pady=10)
ent = Entry(frame, bd=4, width=10)
ent.grid(row=5, column=1)
but = Button(frame, text='Submit', command=sub).grid(row=5, column=2, padx=10)

but1 = Button(root, text='Leave', width=15, command=root.destroy).pack(pady=5)
root.mainloop()