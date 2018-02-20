#Ejercicio generator function
def get_odds(rangUsu = 10):
    genOdd = (number for number in range(rangUsu) if number % 2 != 0)
    return(genOdd)
count = 0
for numberOdd in get_odds():
    if count == 3:
        print("Get odds:",numberOdd)
    count += 1

print("\n")

#funcion para prueba
def good():
    goodList = ["Harry", "Ron", "Hermione"]
    return(goodList)

#Ejercicio decorador
def deco_funct(func):
    print("Start")
    print("The function passed:",func())
    print("Finish")
deco_funct(good)

print("\n")

#Mi propia excepción
class OopsException(Exception):
    """docstring for Oops_Exception"""
    pass

words = [5, "Darling", "4"]
while True:
    for word in words:
        checking = type(word)
        if checking == 'int' or checking == 'float':
            print("Original", word)
        """else:
            raise OopsException
            continue"""