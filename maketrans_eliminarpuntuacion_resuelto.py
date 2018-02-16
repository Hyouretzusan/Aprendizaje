import string

fhand = open('romeocompleto.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    
    """ANOTACIÓN IMPORTANTE: maketrans tiene 3 parámetros. El primer parámetro
    son los caracteres en el string (fromstr), el segundo parámetro son los caracteres
    que queremos intercambiar por los que pasamos en el primer parámetro (tostr).
    El tercer parámetro es para BORRAR todo lo que le indiquemos en el string.
    en la sentencia str.translate(str.maketrans('', '', string.punctuation)) lo
    que ocurre es que NO estoy pasando los primeros 2 parámetros (fromstr y tostr)
    sino que los dejo en blanco (''), y en el tercer parámetro le estoy diciendo que
    borre todo lo que aparezca en la función string.punctuation, que son todos aquellos
    caracteres que python reconoce como signos de puntuación.
    OJO: str.maketrans() SIEMPRE se usa como parámetro para str.translate()"""

    line = line.lower()
    words = line.split()

    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] = counts[word] + 1
    print(words)
print(string.punctuation)