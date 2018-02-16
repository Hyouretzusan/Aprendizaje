oracion = input("Por favor, ingrese una frase:\n")
palabras = oracion.split()
numeroPalabras = len(palabras)
i = 0

while i <= numeroPalabras:
    for palabra in palabras:
        print(palabra)
    i = i + 1