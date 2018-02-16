colums = 3
filas = 3
matriz = [0 for x in range(colums) for y in range(filas)] #Y esto para que?

matrizeditada = matriz.insert(5 , 1) #primer numero es posicion. Segundo numero es valor nuevo

print(matriz)