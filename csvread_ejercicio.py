import csv

with open ("test.csv", "rt") as entrada:
    csventrada = csv.DictReader(entrada)
    for book in csventrada:
        print(book)