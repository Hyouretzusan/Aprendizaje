"""Debo ubicar en los archivos mbox-short.txt y mbox.txt
las líneas del tipo `New Revision: 39772`, y mediante el uso
de expresiones regulares obtener solamente la parte numérica. 
Con esto, calcular el promedio en ambos casos"""

import re

entrada = input("Por favor, ingrese el nombre del archivo: ")
revisionlista = []

try:
    fhandle = open(entrada)
except:
    print("El archivo no existe")
    exit()
#fhandle = open("mbox-short.txt")

for lines in fhandle:
    lines = lines.rstrip()
    revisioncount = re.findall('New Revision: ([0-9.]+)', lines)
    if len(revisioncount) != 1:
        continue
    numFloat = float(revisioncount[0])
    revisionlista.append(numFloat)

promedio = sum(revisionlista)/len(revisionlista)
print("El promedio es:", promedio)