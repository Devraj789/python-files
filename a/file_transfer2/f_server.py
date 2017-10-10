import socket
import pickle

s = socket.socket()
host = socket.gethostname()
port = 9000

s.bind((host,port))
s.listen(10)
print ('waiting for connection........')
clientsocket,addr = s.accept()

dir_recieved = clientsocket.recv(4096)

try:
	data = pickle.loads(dir_recieved)
except Exception as e:
	print(e)

print ('The List Of File To choose from:')
i=1
for j in data:
	print (i,'.',j)
	i = i+1

u_choice = input('Choose the file, you want to recieve')
clientsocket.send(u_choice.encode('utf-8'))

while True:
    size = clientsocket.recv(16) # Note that you limit your filename length to 255 bytes.
    if not size:
        break
    size = int(size, 2)
    filename = clientsocket.recv(size)
    filesize = clientsocket.recv(32)
    filesize = int(filesize, 2)
    file_to_write = open(filename, 'wb')
    chunksize = 4096
    while filesize > 0:
        if filesize < chunksize:
            chunksize = filesize
        data = clientsocket.recv(chunksize)
        file_to_write.write(data)
        filesize -= chunksize

    file_to_write.close()
    print ('File received successfully')

s.close()

