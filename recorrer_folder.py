import os

palabraUsu = input("Ingrese la palabra que desea buscar: ")
rootDir = "C:/Users/CLAUDIO/Desktop/Archivos TXT"
contador = 0

for dirName, subdirList, fileList in os.walk(rootDir):
    print('Directorio encontrado: %s' % dirName)
    
    for fname in fileList:
        print('%s' % fname)
        fhandle = open(fname)
        
        for lines in fhandle:

            lines = lines.rstrip()
            
            if lines.startswith(palabraUsu):
                print("\t%s" % lines)
                contador += 1
            
            if contador == 0:
                print("\tNo hay resultados")
                break