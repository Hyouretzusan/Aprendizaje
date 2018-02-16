"""Debo tomar el siguiente string, ubicar el
símbolo ':', hacer un slice, y convertir el número final
de un tipo string, a un tipo float"""

userString = "X-DSPAM-Confidence:0.8475"

busquedapos = userString.find(':')
stringtofloat = busquedapos + 1
busquedafloat = float(userString[stringtofloat:])
print("Posición del símbolo:", busquedapos)
print("Valor obtenido:", busquedafloat)
print("Tipo del valor:", type(busquedafloat))