class Persona:
	def __init__(self,edad): #inicializo la clase, defino argumentos
		self.edad = edad #atributo inicial de la clase
		print("Soy un nuevo objeto") #metodo inicial de la clase

	def cantar(self,cancion): #defino un metodo de la clase "Persona"
		print(cancion)

claudio = Persona(30)
karina = Persona(25)

print("Soy Claudio, y tengo", str(claudio.edad), "años")
print("Soy Karina, y tengo", karina.edad, "años") #llamo al atributo edad

claudio.cantar('Clocks')
karina.cantar('You really got me')