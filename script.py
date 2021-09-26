from tkinter import * 
from tkinter import ttk
from db import conn,cursor,make_table

from add import add_book
from view import view_all

make_table()

window = Tk()
window.title("Book Store Application")
window.geometry("500x500")
window['bg'] ='#eee'



add = ttk.Button(window,text="Add New Entry",command=add_book)
add.grid(row=0,column=1)

view = ttk.Button(window,text="View All",command=view_all)
view.grid(row=0,column=0)




window.mainloop()