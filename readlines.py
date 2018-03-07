fin = open('relativity', 'rt' )
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')

for line in lines:
	print(line, end='')
