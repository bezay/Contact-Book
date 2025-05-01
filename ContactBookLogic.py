import tkinter as tk
from tkinter import *
from tkinter import messagebox

contactList = [
    ["Bijay Acharya", "0426414366"],
    ["Samikshya Acharya","0411661031"]
               ]
name = StringVar()
contactNum = StringVar()

def Select_Set(select):
    contactList.sort()
    select.delete(0,END)
    for name,contactNum in contactList:
        select.insert (END, name)
    
def EXIT(win):
    win.destroy()

def Selected(select):
   ## print("hello",len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error","Please Select the Name")

    else:
        return int(select.curselection()[0])

def AddContact(select):
    if name.get() != "" and contactNum.get != "":
        contactList.append ([name.get(), contactNum.get()])
        print (contactList)
        Select_Set(select)
        EntryReset(select)
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")
    else:
        messagebox.showerror("Error","Please fill the information")
 
def UpdateDetail(select):
    if name.get() and contactNum.get():
        contactList[Selected(select)] = [name.get(), contactNum.get()]
   
        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset(select)
        Select_Set(select)
 
    elif not(name.get()) and not(contactNum.get()) and not(len(select.curselection())==0):
        messagebox.showerror("Error", "Please fill the information")
 
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                          """
            messagebox.showerror("Error", message1)
def Delete_Entry(select):
    if len(select.curselection()) != 0:
        result = messagebox.askyesno("Confirmation","You Want to delete contact ?")
        if result == True:
            del contactList[Selected(select)]
            Select_Set(select)

        else:
            messagebox.showerror("Error","Please select the Contact")
    
def View(select):
    NAME, PHONE = contactList[Selected(select)]
    name.set(NAME)
    contactNum.set(PHONE)

def EntryReset():
	name.set('')
	contactNum.set('')