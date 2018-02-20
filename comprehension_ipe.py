#Ejercicio list comprehension
even = [number for number in range(10) if number % 2 == 0]
print(even)

#Ejercicio dict comprehension
squares = {number: number**2 for number in range(10)}
print(squares)

#Ejercicio set comprehension
odd = {number for number in range(10) if number % 2 != 0}
print(odd)

#Ejercicio generator comprehension
genCom = (numberG for numberG in range(10))
for number in genCom:
    print("Got:", number, type(genCom))