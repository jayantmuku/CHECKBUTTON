import tkinter as t
from tkinter import messagebox as msg

def choose():
    mylist=[]
    if myvar.get():
        mylist.append("C")
    if myvar2.get():
        mylist.append("java")
    if myvar3.get():
        mylist.append("python")
    if myvar4.get():
        mylist.append("c++")
    msg.showinfo("LANGUAGE","YOU HAVE SELECTED ") 




win =t.Tk()
myvar = t.StringVar(win)
myvar.set(None)


myvar = t.StringVar()
ch=t.Checkbutton(win,text="c")
ch.place(x=10,y=10)

myvar2 = t.StringVar()
ch1=t.Checkbutton(win,text="java")
ch1.place(x=10,y=30)

myvar3 = t.StringVar()
ch2=t.Checkbutton(win,text="python")
ch2.place(x=10,y=50)

myvar4 = t.StringVar()
ch3=t.Checkbutton(win,text="C++")
ch3.place(x=10,y=70)

bt=t.Button(win,text="SUBMIT",bg="#00CDD1",command=choose)
bt.place(x=10,y=120)
