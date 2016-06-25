
  
import socket
import sys
from thread import *
  
HOST = '' 
PORT = 5188 
a = []
c=[]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
print 'Socket bind complete'
s.listen(10)
print 'Socket now listening'
def cthread(conn):
    n=conn.recv(1024)
    c.append(n)
    for i in range(len(c)-1):
	a[i].sendall(n +' is Available:')	
    conn.send(' Available clients are : \n')
    for i in range(len(c)):
	conn.send(c[i].upper()+'\n')
    while True:  
	data = conn.recv(1024)
	reply=data		
	for x in range(len(c)):		
		a[x].sendall(r)
    conn.close()
  

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    address.append(conn)
    start_new_thread(cthread ,(conn,))
 	 
s.close()
