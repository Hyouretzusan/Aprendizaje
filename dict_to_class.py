class Element():
    """docstring for Element"""
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

elementDict = {"name" : "Hydrogen", "symbol" : "H", "number" : "1"}
elementDictList = list(elementDict.values())
print(elementDictList[0])

myElement = Element(elementDictList[0], elementDictList[1], elementDictList[2])
print(myElement)