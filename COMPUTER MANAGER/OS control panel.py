from tkinter import *
from PIL import ImageTk
import os
import pyttsx3 #pip install pyttsx3 module

def tm():
    pyttsx3.speak ('I am opening your pc task manager')
    os.system('taskmgr')
def cp():
    pyttsx3.speak ('I am opening your pc control panel')
    os.system('control')
def dt():
    pyttsx3.speak ('I am opening your pc date & time settings')
    os.system('timedate.cpl')
def sys():
    pyttsx3.speak ('I am opening your pc system servies')
    os.system('services.msc')
def dm():
    pyttsx3.speak ('I am opening your pc device manager')
    os.system('devmgmt.msc')
def up():
    pyttsx3.speak ('I am opening your windows update page')
    os.system('control update')
def ms():
    pyttsx3.speak ('I am opening your pc mouse properties')
    os.system('main.cpl')
def sp():
    pyttsx3.speak ('I am opening your system properties')
    os.system('sysdm.cpl')
def un():
    pyttsx3.speak ('I am opening your pc uninstalling page')
    os.system('appwiz.cpl')
def net():
    pyttsx3.speak ('I am showing you your network connections')
    os.system('ncpa.cpl')
def but():
    pyttsx3.speak ("You shouldn't have pressed that, Bye for now")
    root.destroy()

root=Tk()
root.title('Computer Manager')
root.resizable(0,0)
bg=ImageTk.PhotoImage(file="COMPUTER MANAGER/images/white.jpg")
bgL=Label(root, image=bg).grid(row=0, column=0)

bgF=Frame(root, height=90, width=626, bg='black', bd=0, relief=SUNKEN).place(x=1, y=5)
tool=PhotoImage(file="COMPUTER MANAGER/images/tool.png")
a=Label(bgF, text='  AI COMPUTER MANAGER', font=('verdana',18,'bold'), fg='white', bg='black', image=tool, compound=LEFT )
a.place(x=100, y=20)

ff=Frame(root, height=320, width=626, bg='white', relief=SUNKEN).place(x=1, y=110)
task=PhotoImage(file="COMPUTER MANAGER/images/task.png")
b=Button(ff, text=' Task Manager', font=('verdana',14,'bold'),bd=0, fg='blue', bg='white',activebackground='white', 
            activeforeground='blue', image=task, compound=LEFT, cursor='hand2', command=tm)
b.place(x=20, y=122)

panel=PhotoImage(file="COMPUTER MANAGER/images/panel.png")
b=Button(ff, text='  Control Panel', font=('verdana',14,'bold'),bd=0, fg='black', bg='white', activebackground='white', 
            activeforeground='black', image=panel, compound=LEFT, cursor='hand2', command=cp)
b.place(x=350, y=122)

detentime=PhotoImage(file="COMPUTER MANAGER/images/dt.png")
b=Button(ff, text=' Date and Time', font=('verdana',14,'bold'),bd=0, fg='red', bg='white', activebackground='white', 
            activeforeground='red', image=detentime, compound=LEFT, cursor='hand2', command=dt)
b.place(x=20, y=172)

system=PhotoImage(file="COMPUTER MANAGER/images/system.png")
b=Button(ff, text=' System Services', font=('verdana',14,'bold'),bd=0, fg='green', bg='white', activebackground='white', 
            activeforeground='green', image=system, compound=LEFT, cursor='hand2', command=sys)
b.place(x=350, y=172)

device=PhotoImage(file="COMPUTER MANAGER/images/device.png")
b=Button(ff, text=' Device Manager', font=('verdana',14,'bold'),bd=0, fg='gray28', bg='white', activebackground='white', 
            activeforeground='gray28', image=device, compound=LEFT, cursor='hand2', command=dm)
b.place(x=20, y=222)

update=PhotoImage(file="COMPUTER MANAGER/images/update.png")
b=Button(ff, text=' Windows Update', font=('verdana',14,'bold'),bd=0, fg='dark violet', bg='white', activebackground='white', 
            activeforeground='dark violet', image=update, compound=LEFT, cursor='hand2', command=up)
b.place(x=350, y=222)

mouse=PhotoImage(file="COMPUTER MANAGER/images/mouse.png")
b=Button(ff, text=' Mouse Properties', font=('verdana',14,'bold'),bd=0, fg='navy blue', bg='white', activebackground='white', 
            activeforeground='navy blue', image=mouse, compound=LEFT, cursor='hand2', command=ms)
b.place(x=20, y=272)

properties=PhotoImage(file="COMPUTER MANAGER/images/properties.png")
b=Button(ff, text=' System Properties', font=('verdana',14,'bold'),bd=0, fg='olive', bg='white', activebackground='white', 
            activeforeground='olive', image=properties, compound=LEFT, cursor='hand2', command=sp)
b.place(x=350, y=272)

uninstall=PhotoImage(file="COMPUTER MANAGER/images/uninstall.png")
b=Button(ff, text=' Uninstall Softwares', font=('verdana',14,'bold'),bd=0, fg='black', bg='white', activebackground='white', 
            activeforeground='black', image=uninstall, compound=LEFT, cursor='hand2', command=un)
b.place(x=20, y=322)

network=PhotoImage(file="COMPUTER MANAGER/images/network.png")
b=Button(ff, text=' Network connections', font=('verdana',14,'bold'),bd=0, fg='peru', bg='white', activebackground='white', 
            activeforeground='peru', image=network, compound=LEFT, cursor='hand2', command=net)
b.place(x=350, y=322)

end=PhotoImage(file="COMPUTER MANAGER/images/end.png")
Button(ff, image=end, bg='white', bd=0,
            activebackground='white',command=but).place(x=280, y=362)

#pyttsx3.speak ('Hii... How can i help you?')
root.mainloop()