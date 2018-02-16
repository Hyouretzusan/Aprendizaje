"""Debo crear un script que recorra un string letra
por letra, desde la última posición hasta la primera
y vaya imprimiendo las letras"""

palabraUsu = input("Por favor, ingrese una palabra: ")

palabraLong = len(palabraUsu)
letra = palabraLong

while letra > 0:
    
    print(palabraUsu[-letra])
    letra = letra - 1