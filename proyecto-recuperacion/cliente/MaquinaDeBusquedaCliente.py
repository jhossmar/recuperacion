'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import socket
s = socket.socket()
s.connect(("localhost", 9999))
while True:
    mensaje = raw_input("> ")
    s.send(mensaje)
    mensaje == "quit"
    break

print "adios"
s.close()


        
        
        
        
        