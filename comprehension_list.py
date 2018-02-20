#for e if: [variable de iteración for variable de iteración in iterable if condición] If opcional
number_list = [number for number in range(1,6) if number % 2 == 0]
print(number_list)


#for y for: [(v1, v2) de iteración for v1 in iterable1 for v2 in iterable 2 if condición] If opcional
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols if row != col]
for cell in cells:
    print(cell)