import csv

books = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
with open("test.csv", "wt") as csvout:
    csvout.write(books)