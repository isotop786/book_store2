from os import write
from tkinter import * 
from tkinter import ttk
from db import conn,cursor
import csv

    

def view_all():

    """SQL statement """
    res = cursor.execute("SELECT * FROM book_store")


    t = Toplevel()
    t.title("All Entry")
    t.geometry("500x300")

    f = ttk.Frame(t)
    f.pack()
    
    # table
    tbl = ttk.Treeview(f)
    tbl['columns'] = ('Title','Author','Year','ISBN')

    # defining colums 
    tbl.column("#0",width=0,stretch=NO)
    tbl.column("Title",anchor=CENTER,width=80)
    tbl.column("Author",anchor=CENTER,width=80)
    tbl.column("Year",anchor=CENTER,width=80)
    tbl.column("ISBN",anchor=CENTER,width=80)
    
    
    # defining heading
    tbl.heading("#0",text="",anchor=CENTER)
    tbl.heading("Title",text="Title",anchor=CENTER)
    tbl.heading("Author",text="Author",anchor=CENTER)
    tbl.heading("Year",text="Year",anchor=CENTER)
    tbl.heading("ISBN",text="ISBN",anchor=CENTER)
    
    
    for r in res:
        tbl.insert(parent='',index='end',
         values=(r[1],r[2],r[3],r[4]
                 ))
        
    def export():
        header = ['Title','Author','Year','ISBN'] 
        data = ['my title','my author',23023,232323]
        r = cursor.execute("SELECT * FROM book_store")
        #csv.writer.writerow(header)
        for x in r: 
            with open('store_data.csv','w',encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(X)
        print(data)        
        # for d in res:
        #     data = [d[0],d[1],d[2],d[3],d[4]]
        #     print(d[1])
        #     with open('store_data.csv','w', encoding='UTF-8') as f:
        #         writer = csv.writer(f)
        #         writer.writerow(header)
        #         writer.writerow(data)
        #         print("done")
        #         #print(data)
            
        
        
       
    export = ttk.Button(t,text="Export",command=export) 
    export.pack()
    

    tbl.pack()
    t.mainloop()