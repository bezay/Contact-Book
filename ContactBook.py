import tkinter as tk
from tkinter import *

win = tk.Tk()
win.geometry("900x900")
##win.config(bg = '#d3f3f5')
win.resizable(0,0)
win.title("Contact Book")

import ContactBookLogic as cb


frame = Frame(win)
frame.place(x=500,y=70)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=("Courier",20), bg= "#f0fffc", width=20, height=20, borderwidth=3, relief=GROOVE)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH,expand=1)

label1 = Label(win, text="Name: ", font=("Courier", 25,"bold"), bg= "Gray")
label1.place(x=30, y=70)
entry1 = Entry(win, textvariable=cb.name, width=30)
entry1.place(x=270,y=70)

label2 = Label(win, text="Contact NO:", font=("Courier", 25,"bold"), bg= "Gray")
label2.place(x=30, y=120)
entry2 = Entry(win, textvariable=cb.contactNum, width=30)
entry2.place(x=270,y=120)

bt1 = Button(win, text="ADD", font=("Courier",22,"bold" ), bg="#add8e6", command=lambda: cb.AddContact(select))
bt1.place(x=30,y=170)

bt2 = Button(win, text="EDIT", font=("Courier",22,"bold" ), bg="#add8e6", command=lambda: cb.UpdateDetail(select))
bt2.place(x=30,y=220)

bt3 = Button(win, text="DELETE", font=("Courier",22,"bold" ), bg="#add8e6", command=lambda: cb.Delete_Entry(select))
bt3.place(x=30,y=270)

bt4 = Button(win, text="VIEW", font=("Courier",22,"bold" ), bg="#add8e6",command=lambda: cb.View(select))
bt4.place(x=30,y=320)

bt5 = Button(win, text="RESET", font=("Courier",22,"bold" ), bg="#add8e6", command=lambda: cb.EntryReset())
bt5.place(x=30,y=370)

bt6 = Button(win, text="EXIT", font=("Courier",22,"bold" ), bg="#add8e6", command=lambda: cb.EXIT(win))
bt6.place(x=335,y=750)





cb.Select_Set(select)

win.mainloop()
