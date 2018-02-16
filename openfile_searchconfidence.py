fileUsu = input("Por favor, ingrese el nombre del archivo: ")
total = 0
contador = 0
promedio = 0
try:
    fhandle = open(fileUsu)
except:
    print("El archivo ingresado no fue encontrado")
    exit()
for line in fhandle:
    line = line.lower()

    if line.startswith("x-dspam-confidence:"):
        puntospos = line.find(":")
        espaciopos = line.find(" ",puntospos + 2) #puntospos + 2
        confidenceFloat = float(line[puntospos + 2:espaciopos]) #quite el float()
        total = total + confidenceFloat
        contador = contador + 1
        promedio = total / contador
    else:
        continue
print("Ocurrencias:", contador)
print("Sumatoria:", total)
print("Promedio:", promedio)
    #print(line[puntospos + 2:espaciopos])