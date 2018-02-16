def area_paralelogramo(base, altura):
	area = base * altura #estas variables solo existem dentro de la funcion
	print(area)

base = int(input("Ingrese la base del paralelogramo: "))
altura = int(input("Ingrese la altura del paralelogramo: "))
#Estas variables son otras, y existen fuera de la funcion
area_paralelogramo(base, altura) #Llamado a la funcion. Los parametros en el parentesis