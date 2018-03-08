bdata = bytes(range(0, 256))
len(bdata)

fout = open('bfile', 'wb')
fout.write(bdata)
fout.close()
print(bdata)