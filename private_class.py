class Element():
    """docstring for Element"""
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    def get_(self):
        print("Inside the getter")
        return(self.__name)#, self.__symbol, self.__number)

    def set_(self, name, symbol, number):
        print("Inside the setter")
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    name = property(get_, set_)
    #symbol = property(get_, set_)
    #number = property(get_, set_)

elementDict = {"name": "Hydrogen", "symbol": "H", "number": "1"}
elementDictList = list(elementDict.values())
#print(elementDictList[0])

hydrogen = Element(elementDictList[0], elementDictList[1], elementDictList[2])
print(hydrogen.name)