"""Debo crear un programa que reciba una serie de
números por parte del usuario, y en cada iteración me indique
cuál es el máximo y el mínimo en esa serie. Debe ser capaz de
manejar datos incorrectos por parte del usuario, y detenerse con
la palabra 'done'"""

numerosUsu = None
maximo = None
minimo = None

while numerosUsu != 'done' or numerosUsu is None:    

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