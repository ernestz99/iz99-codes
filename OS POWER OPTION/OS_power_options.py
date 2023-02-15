import os
from tkinter import *
import tkinter.messagebox as Messagebox
import pyttsx3 #pip install pyttsx3 module
from PIL import ImageTk

def shutdown_os():
    if Messagebox.askyesno('CONFRIM', 'Are you sure you want to shutdown your pc?'):
        sec=15
        os.system(f'shutdown /s /t {sec}')
        pyttsx3.speak (f'OK sir. I am shutting down your pc in the next {sec} seconds')

def restart_os():
    if Messagebox.askyesno('CONFRIM', 'Are you sure you want to restart your pc?'):
        sec=15
        os.system(f'shutdown /r /t {sec}')
        pyttsx3.speak (f'OK sir. I am rebooting your pc in the next {sec} seconds')

def log_out():
    if Messagebox.askyesno('CONFRIM', 'Are you sure you want to log this user?'):
        pyttsx3.speak ('OK sir I am logging out this user')
        os.system(f'shutdown -l')
    
win=Tk()
win.title('OS Power Options')
win.config(bg="White")
win.resizable(0,0)
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
window_width = 690
window_height = 380
x_coord = (screen_width/2) - (window_width/2)
y_coord = (screen_height/2) - (window_height/2)
win.geometry("%dx%d+%d+%d" % (window_width, window_height, x_coord, y_coord))

bgImage=ImageTk.PhotoImage(file='power.jpg')

bgLabel=Label(win, image=bgImage)
bgLabel.grid()
bL=Label(win, text='POWER OPTIONS', font=("verdana", 25,"bold"),bd=0, bg="White", 
            fg="brown").place(x=200,y=120)

shutL=Label(win, text='SHUTDOWN', font=("verdana", 10,"bold"),bd=0, bg="White", fg="brown").place(x=60,y=330)
Sicon=PhotoImage(file='shutdown.png')
shutB=Button(win, image=Sicon, bd=0, bg='white', activebackground='white', cursor='hand2', command=shutdown_os)
shutB.place(x=40,y=200)

risL=Label(win, text='RESTART', font=("verdana", 10,"bold"),bd=0, bg="White", fg="brown").place(x=320,y=330)
Ricon=PhotoImage(file='restart.png')
RistB=Button(win, image=Ricon, bd=0, bg='white', activebackground='white', cursor='hand2', command=restart_os)
RistB.place(x=290,y=200)

logL=Label(win, text='LOG OUT', font=("verdana", 10,"bold"),bd=0, bg="White", fg="brown").place(x=570,y=330)
Licon=PhotoImage(file='exit.png')
logB=Button(win, image=Licon, bd=0, bg='white', activebackground='white', cursor='hand2', command=log_out)
logB.place(x=540,y=200)

win.mainloop()