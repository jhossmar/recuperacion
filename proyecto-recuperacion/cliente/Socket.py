'''
Created on 15 de mar. de 2016

@author: marcelo
'''

import socket
import threading

class Socket(threading.Thread):

    def __init__(self, host,consulta):
       threading.Thread.__init__(self)
       print "iniciando socket cliente:"
       self.s = socket.socket()
       self.host = host
       self.consulta = consulta
     
    
    def run(self):
        try:
           
            self.s.connect((self.host,8087))
            self.enviarDatos(self.consulta)
#             while 1:
#                 print "esperando respuesta del servidor"
        except Exception,e:
            print 'no se conecto con el servidor',self.host
       
       
        
    
    def enviarDatos(self, string):
        print "enviando datos:"
        mensaje = string ##REmplazar por la consulta del usuario
        self.s.send(mensaje)
       
     
   
    def recibirDatos(self):
         self.s.listen(10) # esperando datos
         recibido = self.sc.recv(1000)
         return recibido 
        

    def cerrarSocket(self):
        print "cerrando socket"
        self.sc.close()
        self.s.close()
     
     