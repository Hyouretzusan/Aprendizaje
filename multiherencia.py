class Persona:
	def __init__(self,edad): #inicializo la clase, defino argumentos
		self.edad = edad #atributo inicial de la clase
		print("Tengo", edad, "años")
	def cantar(self,cancion): #defino un metodo (funcion) de la clase "Persona"
		print(cancion)

class IngSistemas(Persona): #Heredo de la clase Persona
	def programar(self,lenguaje): #funcion de la clase IngSistemas
		print("Voy a programar en", lenguaje)

class Instrumentista(Persona):
	def calibrarInstrumento(self,instrumento):
		print("Voy a practicar calibrar un", instrumento)

class Estudioso(IngSistemas, Instrumentista):
	pass
		
claudio = Estudioso(30) #Argumento para la clase Persona

claudio.programar('Python') #Argumentos para los metodos de las clases IngSistemas
claudio.calibrarInstrumento('Manometro') #e Instrumentista
