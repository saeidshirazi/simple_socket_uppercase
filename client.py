import socket

file = open("file.txt","r")
myString = file.readlines()

s = socket.socket()          
port = 12345                
  
s.connect(('127.0.0.1', port)) 

for sss in myString:
    output = sss
    s.sendall(output.encode('utf-8')) 

s.close()        
