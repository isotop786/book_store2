from db import conn, cursor


def insert_book(title,author,year,isbn):
    val = [title,author,year,isbn]
    cursor.execute("INSERT INTO book_store(title,author, year,isbn) values(?,?,?,?)",
                   val)
    conn.commit()
    print(val)
    print(cursor.rowcount)
    
def select_book():
    res = cursor.execute("SELECT * FROM book_store")
    
    return res

def update_book():
    pass

def delete_book(id):
    cursor.execute(f"DELETE FROM book_store WHERE id={id}")
    conn.commit()