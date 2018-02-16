def chop():
    entrada = input("Ingrese una serie de palabras o números separados por comas, sin espacios:\n")
    listaUsu = entrada.split(',') #convierte el input en una lista
    lonLista = len(listaUsu) #Indica el número de ítems en la lista
    chopLista = listaUsu.remove(listaUsu[lonLista - 1]) #Remueve el último elemento
    chopLista = listaUsu.remove(listaUsu[0]) #Remueve el primer elemento 
    print(listaUsu) #Muestra lo que queda
    print(chopLista) #Devuelve None porque el método usado fue Remove

chop()