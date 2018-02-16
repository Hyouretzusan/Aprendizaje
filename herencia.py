class Persona:
	def __init__(self,edad): #inicializo la clase, defino argumentos
		self.edad = edad #atributo inicial de la clase

	def cantar(self,cancion): #defino un metodo de la clase "Persona"
		print(cancion)

class IngSistemas(Persona):
	def programar(self,lenguaje):
		print("Voy a programar en", lenguaje)

class LicDerecho(Persona):
	def estudiarCaso(self,caso):
		print("Voy a estudiar el caso de", caso)

claudio = IngSistemas(30)
leonor = LicDerecho(20)

claudio.programar('Python')
leonor.estudiarCaso('Claudio')

claudio.cantar('Clocks')
leonor.cantar('Gasolina')