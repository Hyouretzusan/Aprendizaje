import csv
import sqlite3
from books_bdd import bdd_consultbooks, bdd_createtable

conn = sqlite3.connect('books_db.sqlite')
cur = conn.cursor()
bdd_createtable()

with open ("books.csv", "rt") as entrada:
    csventrada = csv.DictReader(entrada)
    
    for book in csventrada:
        #print(book["title"]) #DEBB
        cur.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', (book["title"], book["author"], book["year"]))
        conn.commit()
        print("Book registered: %s" % book["title"])

conn.close()

bdd_consultbooks()