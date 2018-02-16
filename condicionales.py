#encoding utf-8

edad = int(input("Ingrese su edad, por favor: "))

if edad >= 0 and edad < 13:
	print("Eres un niño")
elif edad >= 13 and edad < 18:
	print("Eres un pre-adolescente")
else:
	print("Eres un adulto")