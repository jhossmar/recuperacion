'''
Created on 15 de mar. de 2016

@author: marcelo
'''
import socket
class Socket(object):

    def __init__(self,host,puerto):
       print "iniciando socket servidor:"
       self.s = socket.socket()
       self.s.bind(("192.168.43.5", 8087))
       self.s.listen(10)
       self.sc, self.addr = self.s.accept()
       self.recibirDatos() ## Esperando la consulta del cliente
           
        
    
    def enviarDatos(self, string):
        print "enviando datos:"
        
     
   
    def recibirDatos(self):
         recibido = self.sc.recv(1000)
         print "se recibio: ", recibido
        

    def cerrarSocket(self):
        print "cerrando socket"
        self.sc.close()
        self.s.close()
     
     