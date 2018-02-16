import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('es.wikipedia.org', 443))
cmd = 'GET https://es.wikipedia.org/wiki/Hola_mundo HTTP/1.1\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(520)
    if (len(data) < 1):
        break
    print(data.decode(), end='')

mysock.close()