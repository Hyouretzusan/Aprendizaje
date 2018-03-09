import csv

with open('villains', 'rt') as fin: 
    csvin = csv.reader(fin)
    villains = [row for row in csvin if len(row) > 0] # Comprension

print(villains)

with open('villains', 'rt') as fin:
    csvin = csv.DictReader(fin, fieldnames=['first', 'last']) #Crea un ordered dict
    villains = [row for row in csvin]

print(villains)