"""Rehacer el código que calcula el máximo y mínimo de una
serie de números ingresados por el usuario, utilizando una lista
y las funciones max() y min(). El programa debe detenerse cuando se 
ingrese la palabra 'Done', y debe ser capaz de lidiar con datos no
numéricos (errores de usuario)"""

numLista = list()
entrada = None

while entrada != "done":
    entrada = input("Por favor, ingrese un número: ")
    entrada.lower()

    if entrada != "done":
        try:
            entradaFloat = float(entrada)
        except:
            print("Esto no es un número")
            print("Para detener el programa, ingrese la palabra 'Done'")
            continue

        numLista.append(entradaFloat)

print("Done!")
if len(numLista) != 0:
    print(">>> Máximo ingresado:", max(numLista))
    print(">>> Mínimo ingresado:", min(numLista))