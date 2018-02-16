def computemaxmin(numeroInit):

    numerosUsu = None
    maximo = None
    minimo = None
    escape = 0

    while numerosUsu != 'done' or numerosUsu is None:    
        if escape == 0:
            if numeroInit != 'done':
                try:
                    numeroFloat = float(numeroInit)
                    if maximo is None or numeroFloat > maximo:
                        maximo = numeroFloat
                    
                    if minimo is None or numeroFloat < minimo:
                        minimo = numeroFloat

                    print(">>> Máximo ingresado hasta ahora:", maximo)
                    print(">>> Mínimo ingresado hasta ahora:", minimo)
                    escape = escape + 1
                
                except:
                    print("Esto no es un número")
                    print("Puede detener el programa ingresando la palabra 'done' en minúsculas")
                    escape = escape + 1
                    continue
            if numeroInit == 'done':
                print("Done!")
                break

        else: 
            numerosUsu = input("Por favor, ingrese un número: ")
            if numerosUsu != 'done':
                try:
                    numeroFloat = float(numerosUsu)
                    if maximo is None or numeroFloat > maximo:
                        maximo = numeroFloat
                    
                    if minimo is None or numeroFloat < minimo:
                        minimo = numeroFloat

                    print(">>> Máximo ingresado hasta ahora:", maximo)
                    print(">>> Mínimo ingresado hasta ahora:", minimo)
                
                except:
                    print("Esto no es un número")
                    print("Puede detener el programa ingresando la palabra 'done' en minúsculas")
                    continue
            elif numerosUsu == 'done':
                print("Done!")
                break

numeroPrim = input("Por favor, ingrese un número: ")
resultado = computemaxmin(numeroPrim)