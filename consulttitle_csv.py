import sqlite3

conn = sqlite3.connect('books_db.sqlite')
cur = conn.cursor()

cur.execute('SELECT title FROM Books ORDER BY title')
existencia = cur.fetchall()
for row in existencia:
    print("Title:", row)
conn.close()