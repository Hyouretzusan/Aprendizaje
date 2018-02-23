class Element():
    """docstring for Element"""
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    """def get_(self):
        print("Inside the getter")
        return(self.__name, self.__symbol, self.__number)"""

    def get_name(self):
        print("Inside the name getter")
        return(self.__name)

    def get_symbol(self):
        print("Inside the symbol getter")
        return(self.__symbol)

    def get_number(self):
        print("Inside the number getter")
        return(self.__number)

    def set_(self, name, symbol, number):
        print("Inside the setter")
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    name = property(get_name, set_)
    symbol = property(get_symbol, set_)
    number = property(get_number, set_)

elementDict = {"name": "Hydrogen", "symbol": "H", "number": "1"}
elementDictList = list(elementDict.values())
#print(elementDictList[0])

hydrogen = Element(elementDictList[0], elementDictList[1], elementDictList[2])
print("Nombre:", hydrogen.name, "Simbolo:", hydrogen.symbol, "Numero:", hydrogen.number)