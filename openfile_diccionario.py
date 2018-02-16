"""Debo crear un programa que abra el archivo mbox-short.txt y
ubique cada línea que comienza con la palabra 'FROM' (sin :).
En cada una de esas líneas, encontrar el día se la semana en que
fue enviado cada correo. Al ir obteniendo esos resultados, elaborar
un histograma utilizando un diccionario, y mostrar el contenido del 
diccionario sin importar el orden de aparición de los elementos"""

entrada = input("Ingrese el nombre del archivo: ")
wordsDict = {}
contador = 0

try:
    fhandle = open(entrada)
except:
    print("El archivo no existe.")
    exit()

for lines in fhandle:
    if lines.startswith("From"):
        lines.lower()
        lines.rstrip()
        if lines[4] == ":":
            continue
        words = lines.split()
        weekday = words[2]
        #print(weekday)
        wordsDict[weekday] = wordsDict.get(weekday,0) + 1
print(wordsDict)
