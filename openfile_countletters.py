import string

lettersDict = {}
entrada = input("Por favor, ingrese el nombre de un archivo: ")
try:
    fhandle = open(entrada)
except:
    print("El archivo no existe.")
    exit()

#fhandle = open("romeocompleto.txt")

for lines in fhandle:
    lines = lines.rstrip()
    lines = lines.translate(lines.maketrans("", "", string.punctuation))
    lines = lines.translate(lines.maketrans("", "", "1234567890"))
    lines = lines.lower()
    words = lines.split()
    for word in words:
        for letters in word:
            lettersDict[letters] = lettersDict.get(letters, 0) + 1
#print(lettersDict)

templist = []
tuplist = lettersDict.items()

for key, val in tuplist:
    nuevatup = (val, key)
    templist.append(nuevatup)

ordenLista = sorted(templist, reverse = True)

for val, key in ordenLista:
    print(key, val)