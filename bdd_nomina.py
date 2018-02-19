import sqlite3

class nomina_management:
    def __init__(self):
        print("")

    def bdd_creartabla():
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS Trabajador')
        cur.execute('CREATE TABLE Trabajador (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, nombre TEXT, apellido TEXT, cedula INTEGER, especialidad TEXT)')
        cur.execute('DROP TABLE IF EXISTS Familiar')
        cur.execute('CREATE TABLE Familiar (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, nombre TEXT, apellido TEXT, cedula INTEGER, parentezco TEXT, trabajador_id INTEGER, UNIQUE(id, trabajador_id))')
        conn.commit()
        conn.close()


    def bdd_borrartabla(tabla):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS ?', (tabla,))
        conn.commit()
        conn.close()


    def bdd_insertartrabajador(nomTrab, apeTrab, cedTrab, espTrab):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('INSERT INTO Trabajador (nombre, apellido, cedula, especialidad) VALUES (?, ?, ?, ?)', (nomTrab, apeTrab, cedTrab, espTrab))
        conn.commit()
        print("Trabajador registrado")
        conn.close()


    def bdd_insertarfamiliar(cedTrab, nomFam, apeFam, cedFam, parFam):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Trabajador WHERE cedula = ?', (cedTrab,))
        trab_id = cur.fetchone()[0]
        cur.execute('INSERT INTO Familiar (nombre, apellido, cedula, parentezco, trabajador_id) VALUES (?, ?, ?, ?, ?)', (nomFam, apeFam, cedFam, parFam, trab_id))
        conn.commit()
        print("Familiar registrado")
        conn.close()


    def bdd_consultartrabajador(cedTrab):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Trabajador WHERE cedula = ?', (cedTrab,))
        trab = cur.fetchone() #hace exactamente lo mismo que el código de abajo
        print(trab)
        conn.close()


    def bdd_consultarfamiliar(cedFam):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Familiar WHERE cedula = ?', (cedFam,))
        fam = cur.fetchone() #hace exactamente lo mismo que el código de abajo
        print(fam)
        conn.close()


    def bdd_editartrabajador(nomEd, apeEd, cedEd, espEd, cedTrab):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('UPDATE Trabajador SET nombre = ?, apellido = ?, especialidad = ?, cedula = ? WHERE cedula = ?', (nomEd, apeEd, espEd, cedEd, cedTrab))
        conn.commit()
        print("Datos modificados")
        conn.close()


    def bdd_editarfamiliar(nomEd, apeEd, cedEd, parEd, cedFam):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('UPDATE Familiar SET nombre = ?, apellido = ?, parentezco = ?, cedula = ? WHERE cedula = ?', (nomEd, apeEd, parEd, cedEd, cedFam))
        conn.commit()
        print("Datos modificados")
        conn.close()


    def bdd_consultartabla(tabla):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        
        if tabla == "Trabajador":
            cur.execute('SELECT * FROM Trabajador')
        elif tabla == "Familiar":
            cur.execute('SELECT * FROM Familiar')
        
        print("La base de datos contiene los siguientes registros:\n")
        for row in cur:
            if row is None:
                print("No hay registros")
            else:
                print(row)
        conn.close()


    def bdd_borrartrabajador(cedTrab):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Trabajador WHERE cedula = ?', (cedTrab,))
        trab_id = cur.fetchone()[0]
        cur.execute('DELETE FROM Familiar WHERE trabajador_id = ?', (trab_id,))
        cur.execute('DELETE FROM Trabajador WHERE cedula = ?', (cedTrab,))
        conn.commit()
        conn.close()
        print("\nTrabajador eliminado")


    def bdd_borrarfamiliar(cedFam):
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('DELETE FROM Familiar WHERE cedula = ?', (cedFam,))
        conn.commit()
        conn.close()
        print("\nFamiliar eliminado")


    def bdd_cargafamiliar(cedTrab):
        contador = 0
        conn = sqlite3.connect('nomina_prueba.sqlite')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Trabajador WHERE cedula = ?', (cedTrab,))
        trab_id = cur.fetchone()[0]
        cur.execute('SELECT * FROM Trabajador JOIN Familiar ON Trabajador.id = Familiar.trabajador_id WHERE Trabajador.id = ?', (trab_id,))
        #carga = cur.fetchone()
        #print("El trabajador: ", carga[1:4])
        #print("Tiene los siguientes familiares: ")
        for row in cur:
            if contador == 0:
                print("El trabajador:", row[1:5])
                print("\nTiene los siguientes familiares:")
                contador = contador + 1
            print(row[6:10])
        conn.close()