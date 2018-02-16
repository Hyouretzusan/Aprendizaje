import socket
import re

urlUsu = input("Por favor, ingrese una url que comience por http: ")
protocol = re.findall('(h[a-z]+:?)', urlUsu)
hostSearch = re.findall('^[a-z]+:/+([0-9a-z.]+)', urlUsu)
host = hostSearch[0]
port = None

print(host, protocol[0])

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if protocol[0] == "https:":
    port = 443

elif protocol[0] == "http:":
    port = 80

mysock.connect((host, port))
cmd = 'GET ' + urlUsu +' HTTP/1.0\r\n\r\n'
print(cmd)
codifica = cmd.encode()

#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(codifica)

while True:
    data = mysock.recv(5200)
    if (len(data) < 1):
        break
    print(data.decode(), end ='')

mysock.close()