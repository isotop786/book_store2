import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor() 

def make_table():
    cursor.execute("DROP TABLE IF EXISTS book_store;")
    cursor.execute("CREATE TABLE book_store ( id INT PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn TEXT)")
    

#make_table()   
    
    