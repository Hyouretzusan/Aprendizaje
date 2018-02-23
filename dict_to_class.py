class Element():
    """docstring for Element"""
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

elementDict = {"name": "Hydrogen", "symbol": "H", "number": "1"}
elementDictList = list(elementDict.values())
#print(elementDictList[0])

hydrogen = Element(elementDictList[0], elementDictList[1], elementDictList[2])
hydrogen.dump()
#print(hydrogen)

#elementList = []
elementName = input("Ingrese el nombre del elemento: ")
#elementList.append(elementName)
elementSymbol = input("Ingrese el símbolo del elemento: ")
#elementList.append(elementSymbol)
elementNumber = input("Ingrese el número del elemento: ")
#elementList.append(elementNumber)
#print(elementList)

newelement = Element(elementName, elementSymbol, elementNumber)
newelement.dump()

#elementDict["name"] = elementList[0]
#elementDict["symbol"] = elementList[1]
#elementDict["number"] = elementList[2]
#print(elementDict)