import sqlite3

def bdd_createtable():
    conn = sqlite3.connect('books_db.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Books')
    cur.execute('CREATE TABLE Books (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, title TEXT, author TEXT, year INTEGER)')
        
    print("BOOKS DB has been initialized\n")

    conn.commit()
    conn.close()

def bdd_consultbooks():
    conn = sqlite3.connect('books_db.sqlite')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM Books')
          
    print("\nThe data base contains the following registers:\n")
    existencia = cur.fetchall()
    for row in existencia:
        if len(row) == 0:
            print("No hay registros")
        else:
            print(row)
    conn.close()

#bdd_createtable() DEBB
#bdd_consultbooks() DEBB