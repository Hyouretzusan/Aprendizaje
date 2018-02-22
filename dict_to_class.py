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