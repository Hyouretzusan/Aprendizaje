
"""Debo realizar un programa que reciba una cantidad no definida de números
por parte del usuario, y la salida sea el número de iteraciones, la suma
de todos los números ingresados, y el promedio obtenido"""

contador = 0
suma = 0
promedio = 0
numeroUsu = None
        
while numeroUsu == None or numeroUsu != "done":
    try:
        numeroUsu = input("Por favor, ingrese un número: ")
        if numeroUsu != "done":
            numeroFloat = float(numeroUsu)
            suma = suma + numeroFloat
            contador = contador + 1
            promedio = suma / contador
        
        elif numeroUsu == "done":
            print("Done!")
            break
    except:
        print("Esto no es un número")
        continue

print("El número iteraciones fue de:", contador)
print("La sumatoria de los números ingresados es:", suma)
print("El promedio obtenido fue:", promedio)