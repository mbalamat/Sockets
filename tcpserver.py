# Time Server
# We suppose that this T/S knows the address od the dir server

import socket

host = '127.0.0.1'
port = 8888

s = socket.socket()

s.connect((host, port))

msg = "10.7.4.57:8855"
s.send(msg)

s.close()

inSocket = socket.socket()

inSocket.bind(('127.0.0.1', port))
insocket.listen(1)

c, addr = inSocket.accept()

while True:
	data = inSocket.recv(1024)
	if not data:
		break
print "> " + str(data)
