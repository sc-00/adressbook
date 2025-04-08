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

def deleteentries():
    selected_checkbox = booklist.curselection()
    for selected_checkbox in selected_checkbox[::-1]:
        booklist.delete(selected_checkbox)

def editcontact():
    selected_name = booklist.get(booklist.curselection())
    contactinfo = adressbook[selected_name]
    namebox.delete(0,END)
    namebox.insert(0,selected_name)
    adressbox.delete(0,END)
    adressbox.insert(0,contactinfo[0])
    mobilebox.delete(0,END)
    mobilebox.insert(0,contactinfo[1])
    emailbox.delete(0,END)
    emailbox.insert(0,contactinfo[2])
    birthdaybox.delete(0,END)
    birthdaybox.insert(0,contactinfo[3])

def openfile():
    with open("downloads.txt","w") as b:
        b.write("vivid bad squad")

open = Button(root,text = "Open",command = openfile)
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

deleteb = Button(root,text = "Delete",command = deleteentries)
deleteb.place(x = 190,y = 370)

editb = Button(root,text = "Edit",command = editcontact)
editb.place(x = 20,y = 370)

saveb = Button(root,text = "Save",width = 40)
saveb.place(x = 150,y = 420)

booklist = Listbox(root,height = 19,width = 40,selectmod = MULTIPLE)
booklist.place(x = 20,y = 50)

root.mainloop()