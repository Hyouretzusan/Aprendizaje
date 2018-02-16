pagoHoras = 10
horasExtra = 0.5
horas = input("Ingrese el numero de horas trabajadas esta semana:")
try:
    horasInt = int(horas)
    if horasInt <= 40:
        salarioSemana = horasInt * pagoHoras
    elif horasInt > 40:
        bono = pagoHoras * horasExtra
        pagoBono = pagoHoras + bono
        salarioSemana = horasInt * pagoBono

    print("Su salario semanal es de:", salarioSemana)
except:
    print("Por favor, ingrese un numero.")