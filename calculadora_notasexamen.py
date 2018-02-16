notaEval = input("Por favor, ingrese una calificación entre 0.0 y 1.0:\n")

try:
    notaFloat = float(notaEval)
    if notaFloat > 1.0:
        print("Número inválido. Por favor, ingrese un valor entre 0.0 y 1.0")
    elif notaFloat >= 0.9 and notaFloat <= 1.0:
        print("Su calificación es A")
    elif notaFloat >= 0.8:
        print("Su calificación es B")
    elif notaFloat >= 0.7:
        print("Su calificación es C")
    elif notaFloat >= 0.6:
        print("Su calificación es D")
    elif notaFloat <= 0.6 and notaFloat >= 0.0:
        print("Su calificación es F")
    elif notaFloat < 0.0:
        print("Número inválido. Por favor, ingrese un valor entre 0.0 y 1.0")
except:
    print("Dato incorrecto. Por favor, ingrese un número")