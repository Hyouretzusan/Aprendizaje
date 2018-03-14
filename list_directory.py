import os

dirActual = os.path.abspath('Aprendizaje') #Indica el path completo, pero repite el ultimo directorio
print("\n",dirActual,"\n")
separador = "\\" 
dirSplit = dirActual.split(separador)
print(dirSplit,"\n")
dirActual2 = separador.join(dirSplit[:3]) #Directorio actual limpio
print("Directorio actual:", dirActual2)

dirLista = os.listdir(dirActual2)
print("Lista de archivos en directorio actual: \n \t%s" % dirLista)