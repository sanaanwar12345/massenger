import socket               # Import socket module
import sys
import os
from thread import *
 

s = socket.socket()         
host = socket.gethostname()
port = 5188                # Reserve a port for your service.
 
s.connect((host, port))
name = raw_input("Enter Your Name : ")
name=name.upper()
s.send(name)
print s.recv(1024)
#to = raw_input()
def rec():
    while True:  
        #Receiving from client        
	data = s.recv(1024)
        print data
start_new_thread(rec,())
while 1:		
	msg = raw_input()
	if msg.lower()=='list':
		os.system('clear')
		s.send(' list')				
	else:	
		reply = msg		
		s.send(reply)
	if not reply:
		break
	
