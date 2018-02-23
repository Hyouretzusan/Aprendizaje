from collections import namedtuple

Perro = namedtuple('Perro', 'Nombre Color')
perro = Perro('Kid', 'Blanco', )
#print(perro)

partes = {"Nombre" : "Kid", "Color" : "Beige"}
perro2 = Perro(**partes)
print(perro2)