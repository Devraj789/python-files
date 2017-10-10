'''
Definition:

A socket is one endpoint of a two-way communication link between two programs running on the network. 
A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent to.
An endpoint is a combination of an IP address and a port number. Every TCP connection can be uniquely identified by its two endpoints. 
That way you can have multiple connections between your host and the server.
steps for connection:
1. server runs on a specific computer and has a socket that is bound to a specific port number. 
The server just waits, listening to the socket for a client to make a connection request.

2. The client knows the hostname of the machine on which the server is running and the port number on which the server is listening. 
To make a connection request, the client tries to rendezvous with the server on the server's machine and port. 
The client also needs to identify itself to the server so it binds to a local port number that it will use during this connection. 
This is usually assigned by the system.

3. If everything goes well, the server accepts the connection. 
Upon acceptance, the server gets a new socket bound to the same local port and also has its remote endpoint set to the address and port of the client. 
It needs a new socket so that it can continue to listen to the original socket for connection requests while tending to the needs of the connected client.

4. On the client side, if the connection is accepted, a socket is successfully created and the client can use the socket to communicate with the server.


'''

import socket

s =  socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host,port))
s.listen(5)   # wait for client connection

while True:
	c,addr = s.accept()
	print ('Got conection from: ',addr)
	c.send(b'Thanks for conecting')
	c.close()

	