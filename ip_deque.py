from collections import deque

def palindromo(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palabraUsu = input("Por favor, ingrese la palabra que desea evaluar")
palabra = palindromo(palabraUsu)

if palabra is True:
    print(palabraUsu, "sí es un palíndromo")
else:
    print("Esto no es un palindromo")