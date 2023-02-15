from tkinter import *
import random

win = Tk()
win.title ("Guessing Game")
win.geometry ("600x400")
win.configure(bg="Black")

e= random.randint(1,31)

def exi():
    win.destroy()
def submit():
    z= int(c.get())

    print (e)
    if z == e:
        g = Label (win, text= "Welldone. You guessed right ✓✓✓✓",bg= "Black", fg="White", font=("Cambria Bold", 12)).grid (row=4, column=1)
            
        h=  Button (win, text= "exit", command=exi, bg="Red", fg="White", font=("Arial Bold", 10)).grid (row=5, column= 1)
            
    elif z>30:
        g= Label (win, text= "<<< ⇶ Guess between 1 and 30 >>>", bg="Black", fg="White", font=("Arial", 9)).grid (row=4, column=1)
            
    elif z<e:
        g= Label (win, text= "Your guess is lower ✕, guess higher ").grid (row=4, column=1)
            
    elif z>e:
        g= Label (win, text= "Your guess is higher ✕, guess lower").grid (row=4, column=1)
            
    else:
        g= Label (win, text= "Guess between 1 and 30......", bg="Black", fg="White").grid (row=5, column=1)

      
a = Label (win, text = "THE GUESSING GAME ⇄", font=("Cambria Bold", 20), bg="Black", fg="White").grid (row=0, column=1)
b = Label (win, text = "Guess a number: ", font=("Cambria", 16), bg="Black", fg="White").grid (row=1, column=0)
c = Entry (win, width=30)
c.grid (row=1, column=1)

f = 1

while f <= 5:
    d = Button (win, text = "Submit", font=("Cambria", 14), bg="Dark Green", fg= "White", command=submit ).grid (row=2, column=1)
    f = f + 1
if f == 5:
    k = Label(win, text = "Oops").grid(row = 2, column = 1)

win.mainloop()       
        


