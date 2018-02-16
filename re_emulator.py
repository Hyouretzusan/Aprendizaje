import re
entrada = None


while entrada == None or entrada !="terminar":
    entrada = input("Ingrese la expresión regular que desea probar: ")
    if entrada == "detener":
        print("FIN!")
        break
        
    else:
        fhandle = open("mbox.txt")
        contador = 0

        for lines in fhandle:
            lines.rstrip()
            if re.search(entrada, lines):
                contador = contador + 1
        if contador == 0:
            print("No se obtuvieron resultados. Revise la sintaxis de la expresión ingresada")

        print("El número de ocurrencias para", entrada, " en mbox.txt es de:", contador)
        print("Para salir, ingrese la palabra 'detener' en minúsculas.")