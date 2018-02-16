from bdd_prueba import bdd_management

print("\nBienvenido a la base de datos para canciones.\n")
print("Opción 1: Iniciar base de datos\nOpción 2: Borrar base de datos")
print("Opción 3: Insertar registro\nOpción 4: Consultar registro")
print("Opción 5: Mostrar todos los registros\nOpción 6 Borrar registro\n")
opUsu = input("Ingrese el número de la opción escogida: ")
print("\n")
bDatos = bdd_management

try:
    opUsu = int(opUsu)
except:
    print("\n>>> La opción ingresada no es válida.")
    exit()

if opUsu == 1:
    bDatos.bdd_creartabla()

elif opUsu == 2:
    bDatos.bdd_borrartabla()

elif opUsu == 3:
    songUsu = input("\nIngrese el nombre de la canción: ")
    timesUsu = input("\nIngrese el número de reproducciones: ")
    print("\n")
    bDatos.bdd_insertarfila(songUsu, timesUsu)

elif opUsu == 4:
    songUsu = input("\nIngrese el nombre de la canción: ")
    print("\n")
    bDatos.bdd_consultarfila(songUsu)

elif opUsu == 5:
    bDatos.bdd_consultartabla()

elif opUsu == 6:
    songUsu = input("\nIngrese el nombre de la canción: ")
    print("\n")
    bDatos.bdd_borrarfila(songUsu)

else:
    print("\n>>> La opción ingresada no es válida")
    exit()