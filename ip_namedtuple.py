from collections import namedtuple

"""Perro = namedtuple('Perro', 'Color')
mascota = Perro('Kid', 'Blanco')
print(mascota)"""

Perro = namedtuple('Perro', 'Longitud cola')
perro = Perro('Kid', 'Corta')
print(perro)