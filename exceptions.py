#Ejercicio generator function
def get_odds(rangUsu = 10):
    genOdd = (number for number in range(rangUsu) if number % 2 != 0)
    return(genOdd)
count = 0
for numberOdd in get_odds():
    if count == 3:
        print("Get odds:",numberOdd,"\n")
    count += 1

#funcion para prueba
def good():
    goodList = ["Harry", "Ron", "Hermione"]
    return(goodList)

#Ejercicio decorador
def deco_funct(func):
    print("Start")
    print("The function passed:",func())
    print("Finish\n")
deco_funct(good)

#Mi propia excepción
class OopsException(Exception):
    """docstring for Oops_Exception"""
    pass

words = [5, "5", "darling"]
for word in words:
    checking = type(word)
    if checking == int or checking == float:
        print("Original", word)
    else:
        try:
            convFloat = float(word)
        except:
            raise OopsException
            continue
        print("Converted", convFloat)