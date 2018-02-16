"""Debo crear un programa que abra el archivo mbox-short.txt y el mbox.txt,
ubique cada línea que comienza con la palabra 'FROM' (sin :).
En cada una de esas líneas, encontrar la dirección de correoAl ir obteniendo
esos resultados, elaborar un histograma utilizando un diccionario, y mostrar 
cuáles correos son los que enviaron más mensajes"""

entrada = input("Por favor, ingrese el nombre del archivo: ")
mailsDict = {}
contador = None
mayor = None
mailmayor = None

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
        mails = words[1]
        #print(mails)
        mailsDict[mails] = mailsDict.get(mails,0) + 1

for mail in mailsDict:
    contador = mailsDict[mail]
    if mayor == None or contador > mayor:
        mayor = contador
        mailmayor = mail
print(mailmayor, mayor)