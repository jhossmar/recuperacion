'''
Created on 15 de mar. de 2016

@author: marcelo
'''

import socket

class Socket(object):

    def __init__(self, host):
       print "iniciando socket servidor:"
       self.s = socket.socket()
       self.s.connect((host,8087))

       
        
    
    def enviarDatos(self, string):
        print "enviando datos:"
        mensaje = raw_input("> ") ##REmplazar por la consulta del usuario
        self.s.send(mensaje)
       
     
   
    def recibirDatos(self):
         self.s.listen(10) # esperando datos
         recibido = self.sc.recv(1000)
         return recibido 
        

    def cerrarSocket(self):
        print "cerrando socket"
        self.sc.close()
        self.s.close()
     
     