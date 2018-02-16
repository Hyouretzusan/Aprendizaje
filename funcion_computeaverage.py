"""Debo realizar una función que reciba una cantidad no definida de números
por parte del usuario, y la salida sea el número de iteraciones, la suma
de todos los números ingresados, y el promedio obtenido.
La función debe poder indicarle al usuario cuando no ingrese un número,
y debe detenerse cuando se ingrese la palabra done"""

def computeaverage(numeroInit):

    suma = 0
    promedio = 0
    contador = 0
    escape = 0 #sirve para escapar del primer if
    numeroUsu = None
            
    while numeroUsu == None or numeroUsu != "done":
        if contador == 0 and escape == 0: #solo se ejecuta con el primer numero del usuario
            try: #si el usuario hace lo que debe la primera vez, esto se ejecuta
                if numeroInit != "done":
                    numeroFloat = float(numeroInit)
                    suma = suma + numeroFloat
                    contador = contador + 1
                    promedio = suma / contador
                    print("Si desea detener el programa y obtener los resultados, \nescriba la palabra 'done' en minúsculas")
                
                elif numeroInit == "done":
                    print(">>> Done!")
                    break
            except: #si el usuario ingresa otro dato que no sea un numero la primera vez, esto se ejecuta
                print(">>> Esto no es un número")
                print("Para detener el programa y obtener resultados, \nintroduzca 'done' en minúsculas\n")
                salida = salida + 1 #se cambia el valor de escape para que en la siguiente iteración se ejecute el else
                continue

        else: #esto se ejecuta la segunda iteración independientemente de las acciones anteriores del usuario
            try: #identico al anterior
                numeroUsu = input("Por favor, ingrese un número: ") #para seguir solicitando mas numeros
                if numeroUsu != "done":
                    numeroFloat = float(numeroUsu)
                    suma = suma + numeroFloat
                    contador = contador + 1
                    promedio = suma / contador
                    print("Para detener el programa y obtener resultados, \nintroduzca 'done' en minúsculas\n")
                
                elif numeroUsu == "done":
                    print(">>> Done!")
                    break
            except:
                print("Esto no es un número")
                print("Para detener el programa y obtener resultados, \nintroduzca 'done' en minúsculas\n")
                continue
    return(contador, suma, promedio) #devuelve los valores deseados en forma de una tupla

numeroPrim = input("Por favor, ingrese un número: ")
resultado = computeaverage(numeroPrim)

print(">>> El número iteraciones fue de:", resultado[0]) #se imprimen los valores
print(">>> La sumatoria de los números ingresados es:", resultado[1])
print(">>> El promedio obtenido fue:", resultado[2])