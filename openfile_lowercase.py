fileUsu = input("Por favor, ingrese el nombre del archivo: ")
try:
    fhandle = open(fileUsu)
except:
    print("El archivo ingresado no fue encontrado")
    exit()
for line in fhandle:
    line = line.rstrip()
    print(line.lower())