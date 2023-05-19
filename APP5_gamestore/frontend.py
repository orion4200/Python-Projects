from tkinter import *
import backend

def get_selected_row(event):
    try:                                            #cmd for retrieving tuple of selected row. event parameter passed as it is mandatory for binding with list
        global selected_row
        index = list1.curselection()[0]
        selected_row = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
    except IndexError():
        pass                                    #function will do nothing

def view_cmd():                                                         #cmd for executing view button and linking view function in backend to frontend
    list1.delete(0, END)
    for rows in backend.view():
        list1.insert(END, rows)

def add_cmd():                                                           #cmd for executing add button and linking view function in backend to frontend
    backend.add_it(var1.get(), var2.get(), var3.get())
    list1.delete(0, END)
    list1.insert(END,(var1.get(), var2.get(), var3.get()))

def search_cmd():                                                        #cmd for executing search button and linking view function in backend to frontend
    list1.delete(0, END)
    for rows in backend.search(var1.get(), var2.get(), var3.get()):
        list1.insert(END, rows)

def del_cmd():                                                          #cmd for executing delete button and linking view function in backend to frontend
    backend.del_it(selected_row[0])

def cl_cmd():
    win.destroy()

def upd_cmd():
    backend.upd(selected_row[0], var1.get(), var2.get(), var3.get())

win = Tk()

win.wm_title("GameStore")

l1 = Label(win, text="Title")
l1.grid(row=0, column=0)

l2 = Label(win, text="Year")
l2.grid(row=1, column=0)

var1 = StringVar()
e1 = Entry(win, textvariable=var1)
e1.grid(row=0, column=1)

var2 = StringVar()
e2 = Entry(win, textvariable=var2)
e2.grid(row=1, column=1)

l3 = Label(win, text="Type")
l3.grid(row=0, column=11)

var3 = StringVar()
e3 = Entry(win, textvariable=var3)
e3.grid(row=0, column=12)

list1 = Listbox(win, height=9, width=32)
list1.grid(row=3, column=0, rowspan=6, columnspan=11)

s1 = Scrollbar(win)
s1.grid(row=5, column=7, rowspan=2, columnspan=5)

list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview())

list1.bind("<<ListboxSelect>>", get_selected_row)                               #binding selection widget to the list. 

b1 = Button(win, text="View All", width=10, command=view_cmd)
b1.grid(row=3, column=12)

b2 = Button(win, text="Add Entry", width=10, command=add_cmd)
b2.grid(row=4, column=12)

b3 = Button(win, text="Search", width=10, command=search_cmd)
b3.grid(row=5, column=12)

b4 = Button(win, text="Update", width=10, command=upd_cmd)
b4.grid(row=6, column=12)

b5 = Button(win, text="Delete", width=10, command=del_cmd)
b5.grid(row=7, column=12)

b6 = Button(win, text="Close", width=10, command=cl_cmd)
b6.grid(row=8, column=12)


win.mainloop()