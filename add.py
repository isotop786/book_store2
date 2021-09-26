from tkinter import * 
from tkinter import ttk
from db import conn,cursor
from view import view_all



def add_book():
    t =Toplevel()
    t.title("Add new Entry")
    t['bg'] ="#eee"
    t.geometry("400x200")
   
    
    # title
    lt = Label(t,text="Title")
    lt.grid(row=0,column=0)

    t_val = StringVar()
    t_en = ttk.Entry(t,textvariable=t_val)
    t_en.grid(row=0,column=1)

    # Author
    la = Label(t,text="Author")
    la.grid(row=0,column=2)

    a_val = StringVar()
    a_en = ttk.Entry(t,textvariable=a_val)
    a_en.grid(row=0,column=3)

    # Year
    ly = Label(t,text="Year")
    ly.grid(row=1,column=0)

    y_val = StringVar()
    y_en = ttk.Entry(t,textvariable=y_val)
    y_en.grid(row=1,column=1)

    # ISBN
    li = Label(t,text="ISBN")
    li.grid(row=1,column=2)

    i_val = StringVar()
    i_en = ttk.Entry(t,textvariable=i_val)
    i_en.grid(row=1,column=3)

    l=Label(t)
    l.grid(row=2,column=2)
    
    def insert_book():
        val = [t_val.get(),a_val.get(),y_val.get(),i_val.get()]
        cursor.execute("INSERT INTO book_store(title,author, year,isbn) values(?,?,?,?)",
                   val)
        conn.commit()
        print(cursor.rowcount)
        t.destroy()
        view_all()

    b1 = ttk.Button(t,text="Add Entry",command=insert_book)
    b1.grid(row=3,column=3,rowspan=2)
      
    t.mainloop()