import csv

with open('villains', 'rt') as fin: 
    cin = csv.reader(fin)
    villains = [row for row in cin if len(row) > 0] # Comprension

print(villains)

with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last']) #Crea un ordereed dict
    villains = [row for row in cin]

print(villains)