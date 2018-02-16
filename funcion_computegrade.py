def computegrade(notaEval):
    try:
        notaFloat = float(notaEval)
        if notaFloat > 1.0 or notaFloat < 0.0:
            print("Número inválido. Por favor, ingrese un valor entre 0.0 y 1.0")
        elif notaFloat >= 0.9 and notaFloat <= 1.0:
            notaLit = "A"
        elif notaFloat >= 0.8:
            notaLit = "B"
        elif notaFloat >= 0.7:
            notaLit = "C"
        elif notaFloat >= 0.6:
            notaLit = "D"
        elif notaFloat <= 0.6 and notaFloat >= 0.0:
            notaLit = "F"
        return(notaLit)

    except:
        print("Dato incorrecto. Por favor, ingrese un número")

notaEval = input("Por favor, ingrese una calificación entre 0.0 y 1.0:\n")
notaFin = computegrade(notaEval)
print("Su calificación es:", notaFin)