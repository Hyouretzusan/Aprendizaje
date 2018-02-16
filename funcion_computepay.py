def computepay(horas, pagoHoras):
    horasExtra = 0.5
    try:
        horasInt = int(horas)
        pagoFloat = float(pagoHoras)
        if horasInt <= 40:
            salarioSemana = horasInt * pagoFloat
        elif horasInt > 40:
            bono = pagoFloat * horasExtra
            pagoBono = pagoFloat + bono
            salarioSemana = horasInt * pagoBono

        print("Su salario semanal es de:", salarioSemana)

    except:
        print("Datos incorrectos. Por favor, solo ingrese números.")

horas = input("Ingrese el numero de horas trabajadas esta semana:")
pagoHoras = input("Ingrese el monto a pagar por hora trabajada:")
computepay(horas, pagoHoras)