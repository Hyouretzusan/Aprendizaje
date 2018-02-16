def computeaverage():

    suma = 0
    promedio = 0
    numeroUsu = None
    contador = 0
            
    while numeroUsu == None or numeroUsu != "done":
        numeroUsu = input("Por favor, ingrese un número: ")
        if numeroUsu != "done":
            try:
                numeroFloat = float(numeroUsu)
            except:
                print("Esto no es un número")
                continue
            suma = suma + numeroFloat
            contador = contador + 1
            promedio = suma / contador
            
        elif numeroUsu == "done":
            print("Done!")
            break

    print("El número iteraciones fue de:", contador)
    print("La sumatoria de los números ingresados es:", suma)
    print("El promedio obtenido fue:", promedio)

computeaverage()