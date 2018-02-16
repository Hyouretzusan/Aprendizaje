entrada = input("Por favor, ingrese el nombre del archivo: ")
domainDict = {}
domain = None
contador = 0

try:
    fhandle = open(entrada)
except:
    print("El archivo no existe.")
    exit()

for lines in fhandle:
    if lines.startswith("From"):
        lines.lower()
        lines.rstrip()
        if lines[4] == ":":
            continue
        words = lines.split()
        email = words[1]
        arrobapos = email.find("@")
        espaciopos = email.find(" ", arrobapos)
        domain = email[arrobapos + 1 :]
        domainDict[domain] = domainDict.get(domain, 0) + 1

print(domainDict)

"""valores = list(domainDict.values())
tuplas = domainDict.items()
cantidadTuplas = len(tuplas)
valoresOrdenados = valores.sort()
print(type(valores))

while contador < cantidadTuplas:
    for posicion in valoresOrdenados:
        for tupla in tuplas:
            if posicion == tupla[contador][1]:
                print(tupla[contador][1])
                contador = contador + 1
            else:
            continue"""
            