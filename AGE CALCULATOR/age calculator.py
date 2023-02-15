from tkinter import *
from datetime import date

win = Tk()
win.title("Age calculator")
win.geometry("700x300")
win.resizable(0, 0)
win.config(bg="White")


def cal():
    today = date.today()
    e = a.get().capitalize()
    f = int(b.get())
    g = int(c.get())
    h = int(d.get())
    birthDate = date(f, g, h)
    age = today.year - birthDate.year
    if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
        age -= 1
    Label(win, text=f"Hayy {e}. You're {age} yrs old 👍", font=(
        "Franklin Gothic Demi", 20), bg="White", fg="Black").grid(row=13, column=1)


Label(win, text="❏ Welcome to the Age Calculating Application", font=(
    "Franklin Gothic Demi", 14), bg="White", fg="Green").grid(row=0, column=1)
Label(win, text="CALCULATE YOUR AGE ", font=("Franklin Gothic Demi", 10),
      bg="White", fg="Black").grid(row=1, column=1)
Label(win, text="What is your name? ➠", font=("Franklin Gothic Demi", 12),
      bg="White", fg="Black").grid(row=3, column=0, padx=20)
a = Entry(win, bg="silver", fg="black", bd=0, font=12, width=20)
a.grid(row=3, column=1)
Label(win, text="PLEASE ENTER YOUR D.O.B", font=(
    "Franklin Gothic Demi", 10), bg="White", fg="Black").grid(row=5, column=1)
Label(win, text="Year ➠ ", font=("Franklin Gothic Demi", 12),
      bg="White", fg="Black").grid(row=6, column=0)
b = Entry(win, bg="silver", fg="black", bd=0, font=12, width=20)
b.grid(row=6, column=1)
Label(win, text="Month ➠ ", font=("Franklin Gothic Demi", 12),
      bg="White", fg="Black").grid(row=7, column=0)
c = Entry(win, bg="silver", fg="black", bd=0, font=12, width=20)
c.grid(row=7, column=1)
Label(win, text="Day ➠ ", font=("Franklin Gothic Demi", 12),
      bg="White", fg="Black").grid(row=8, column=0)
d = Entry(win, bg="silver", fg="black", bd=0, font=12, width=20)
d.grid(row=8, column=1)
Button(win, text="Calculate ✔", font=("Comic Sans MS", 10), bg="Green", fg="White", width=12, activebackground='green',
       activeforeground='white', bd=0, command=cal).grid(row=10, column=1)
Button(win, text="Exit ❎", font=("Comic Sans MS", 10), background="Red", foreground="White", width=12,
       activebackground='red', activeforeground='white', bd=0, command=win.destroy).grid(row=15, column=1)

win.mainloop()
