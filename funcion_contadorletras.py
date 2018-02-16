"""Debo crear una función que recorra un string ingresado
por el usuario que indique el número de veces que una letra
se repite en la palabra"""

def contadorletras(palabraUsu, letraUsu):
    palabraFunc = palabraUsu
    letraFunc = letraUsu
    contador = 0

    for letraString in palabraFunc:
        if letraString == letraFunc:
            contador = contador + 1
    return(contador)

palabraUsu = input("Por favor, ingrese una palabra: ")
letraUsu = input("Por favor, ingrese una letra: ")
resultado = contadorletras(palabraUsu, letraUsu)
print("El número de veces que la letra", letraUsu, "aparece en", palabraUsu, "\nes de:", resultado)