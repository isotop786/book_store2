from tkinter import * 
from tkinter import ttk

window = Tk()
window.title("Book Store Application")
window.geometry("500x500")

# title
lt = Label(window,text="Title")
lt.grid(row=0,column=0)

t_val = StringVar()
t_en = ttk.Entry(window,textvariable=t_val)
t_en.grid(row=0,column=1)

# Author
la = Label(window,text="Author")
la.grid(row=0,column=2)

a_val = StringVar()
a_en = ttk.Entry(window,textvariable=a_val)
a_en.grid(row=0,column=3)

# Year
ly = Label(window,text="Year")
ly.grid(row=1,column=0)

y_val = StringVar()
y_en = ttk.Entry(window,textvariable=y_val)
y_en.grid(row=1,column=1)

# ISBN
li = Label(window,text="ISBN")
li.grid(row=1,column=2)

i_val = StringVar()
i_en = ttk.Entry(window,textvariable=i_val)
i_en.grid(row=1,column=3)




window.mainloop()