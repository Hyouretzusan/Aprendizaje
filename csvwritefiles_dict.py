import csv

villains2 = [
{'first': 'Doctor', 'last': 'No'},
{'first': 'Rosa', 'last': 'Klebb'},
{'first': 'Mister', 'last': 'Big'},
{'first': 'Auric', 'last': 'Goldfinger'},
{'first': 'Ernst', 'last': 'Blofeld'},
]
with open('villains2', 'wt') as fout:
    csvout = csv.DictWriter(fout, ['first', 'last'])
    csvout.writeheader()
    csvout.writerows(villains2)