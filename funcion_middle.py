def middle():
    entrada = input("Ingrese una serie de palabras o números separados por comas, sin espacios:\n")
    listaUsu = entrada.split(',') #convierte el input en una lista
    lonLista = len(listaUsu) #Indica el número de ítems en la lista
    middleLista = listaUsu[1:lonLista - 1] #Slicing desde el segundo elemento hasta el último pero sin incluirlo
    return(middleLista) 

resultado = middle()
print(resultado, type(resultado))
