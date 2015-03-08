#######################
#TCP Directory Server
#######################

import socket

host = 'localhost'

port = 8888

print "Directory server is running " + host + ":", port
# Create a socket to listen to incoming connections
s = socket.socket()

# Binds the IP and Port to the socket
s.bind((host, port))

# Listens for 1 connection from the socket
s.listen(2)

# Accepts the connection and gets the connection as object and the IP
c, addr = s.accept()

print "Incoming connection from " + str(addr)
print "Let's recieve some data...\n"

while True:
  print "la"
	data = c.recv(1024)
	if not data:
		break
print ">> " + str(data)

print "Sending an aknowledge to the incoming connection that i recieved the data...\n"
awk = "Die Server knows T/S."
c.send(awk)

s.close()
