import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = Tk()
root.geometry("550x470")

root.title("this is a title- suling chu")

title = Label(root,text = "Adress Book")
title.place(x = 100,y = 20)

adressbook = {}

def addcontact():
    nameval = namebox.get()
    adrval = adressbox.get()
    mobileval = mobilebox.get()
    emailval = emailbox.get()
    birthval = birthdaybox.get() 
    adressbook[nameval] = (adrval,mobileval,emailval,birthval)
    booklist.insert(END,nameval)
    clearentries()
    messagebox.showinfo("succes","contacts have been added succesfuly")

def clearentries():
    namebox.delete(0,END)
    adressbox.delete(0,END)
    mobilebox.delete(0,END)
    emailbox.delete(0,END)
    birthdaybox.delete(0,END)

open = Button(root,text = "Open")
open.place(x = 200, y = 20)

name = Label(root,text ="Name:")
name.place(x = 300,y = 70)

namebox = Entry(root,width = 30)
namebox.place(x = 350,y = 70)

adress = Label(root,text ="Adress:")
adress.place(x = 300,y = 130)

adressbox = Entry(root,width = 30)
adressbox.place(x = 350,y = 130)

mobile = Label(root,text ="Mobile:")
mobile.place(x = 300,y = 190)

mobilebox = Entry(root,width = 30)
mobilebox.place(x = 350,y = 190)

email = Label(root,text ="Email:")
email.place(x = 300,y = 250)

emailbox = Entry(root,width = 30)
emailbox.place(x = 350,y = 250)

birthday = Label(root,text ="Birthday:")
birthday.place(x = 300,y = 310)

birthdaybox = Entry(root,width = 30)
birthdaybox.place(x = 350,y = 310)

updateb = Button(root,text = "Update/Add",command = addcontact)
updateb.place(x = 400,y = 370)

deleteb = Button(root,text = "Delete")
deleteb.place(x = 190,y = 370)

editb = Button(root,text = "Edit")
editb.place(x = 20,y = 370)

saveb = Button(root,text = "Save",width = 40)
saveb.place(x = 150,y = 420)

booklist = Listbox(root,height = 19,width = 40)
booklist.place(x = 20,y = 50)

root.mainloop()