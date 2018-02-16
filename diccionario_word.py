wordsHandle = open("words.txt")
wordsDict = dict()
contador = 0
for wlines in wordsHandle:
    wordsKeys = wlines.split()
    for words in wordsKeys:
        if words in wordsDict:
            continue
        wordsDict[words] = str(contador)
        contador = contador + 1
print(wordsDict, type(wordsDict))