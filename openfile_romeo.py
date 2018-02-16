fhandle = open("romeo.txt")
finalLista = list()
for line in fhandle:
    words = line.split()
    for word in words:
        if word in finalLista:
            continue
        else:
            finalLista.append(word)
            finalLista.sort()
print(finalLista)
