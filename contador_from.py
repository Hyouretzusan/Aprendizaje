"""Debo crear un script que abra un archivo, identifique las líneas con la
palabra "From" (sin :), y muestre el nombre del emisor del correo así como
el número de veces que la palabra apareció en el archivo"""

contador = 0
target = None
fileUsu = input("Por favor, ingrese el nombre de un archivo: ")

try:
    fhandle = open(fileUsu) #Crea un handle
except:
    print("El archivo ingresado no existe")
    exit()

for lines in fhandle: #Recorre el handle línea por línea
    if lines.startswith("From"): #Selecciona todas las líneas con FROM
        words = lines.split() #Parte las líneas en listas de palabras
        target = lines[4]  #Ubica el quinto elemento en una línea
        if target != ":": #Si el quinto elemento es diferente de :
            contador = contador + 1
            print(words[1])
print(contador)