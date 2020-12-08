import tkinter
from tkinter import *
from tkinter import messagebox
import dbhelper


def add():
    if(len(addtask.get()) == 0):
        messagebox.showerror(
            "ERROR", "No data Available\nPlease Enter Some Task")
    else:
        dbhelper.insertdata(addtask.get())
        addtask.delete(0, END)
        populate()

def update():
    dbhelper.updatedata(id1.get(),id2.get())
    populate()


def populate():
    listbox.delete(0, END)
    for rows in dbhelper.show():
        listbox.insert(END, rows[1])


def deletetask(event):
    dbhelper.deletebytask(listbox.get(ANCHOR))
    populate()


main = tkinter.Tk()
main.title("TODO")
main.geometry("600x600")
#main.resizable(False, False)
main.configure(
    background="#1d1d1d",
)

tkinter.Label(
    main,
    text="Task Manager",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Verdana 20")
).pack(pady=10)

addframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
addframe.pack()
addtask = tkinter.Entry(
    addframe,
    font=("Verdana"),
    background="#eeeeee",
)
addtask.pack(ipadx=20, ipady=5, side="left")

addbtn = tkinter.Button(
    addframe,
    text="ADD TASK",
    command=add,
    background="#000000",
    foreground="#eeeeee",
    relief="flat",
    font=("Verdana"),
    highlightcolor="#000000",
    activebackground="#1d1d1d",
    border=0,
    activeforeground="#eeeeee",
)
addbtn.pack(padx=20, ipadx=20, ipady=5)

tkinter.Label(
    main,
    text="Your Tasks",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Calibri", 18),
).pack(pady=10)

taskframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
taskframe.pack(fill=BOTH, expand=300)
scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(
    taskframe,
    font=("Verdana 18 bold"),
    bg="#1d1d1d",
    fg="#eeeeee",
    selectbackground="#eeeeee",
    selectforeground="#1d1d1d",
)
listbox.pack(fill=BOTH, expand=300)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.bind("<Double-Button-1>", deletetask)
listbox.bind("<Delete>", deletetask)
populate()

tkinter.Label(text="enter here to update data id&task",font=("Verdana 18 bold"),bg="#1d1d1d",fg="#eeeeee",).pack(padx=15, ipadx=1, ipady=3,anchor=NW)
tkinter.Label(text="id",font=("Verdana 18 bold"),bg="#1d1d1d",fg="#eeeeee",).pack(padx=15, ipadx=1, ipady=3,anchor=NW)

id1=tkinter.Entry().pack(padx=10, ipadx=15, ipady=7,anchor=NW)

tkinter.Label(text="TASK",font=("Verdana 18 bold"),bg="#1d1d1d",fg="#eeeeee",).pack(padx=15, ipadx=1, ipady=3,anchor=NW)
id2=tkinter.Entry().pack(padx=10, ipadx=15, ipady=7,anchor=NW)
tkinter.Label(
    main,
    text="TIP : Double Click On A Task to Delete",
    background="#1d1d1d",
    foreground="#FFEB3B",
    font=("Calibri 18"),
).pack(side=BOTTOM, pady=10)

main.mainloop()

