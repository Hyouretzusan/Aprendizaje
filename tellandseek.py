fhandle = open("bfile", "rb")
print("Primer tell:", fhandle.tell())

print("Seek byte 255: ", fhandle.seek(255))
print("Segundo tell en b255:", fhandle.tell())

print("Seek byte 254, con origin = 1: ", fhandle.seek(-1, 1))

print("Seek byte 250, con origin = 2: ", fhandle.seek(-6, 2))