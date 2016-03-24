'''
Created on 15 de mar. de 2016

@author: marcelo
'''
import socket

import threading
class Socket(threading.Thread):

    def __init__(self,host,puerto):
       threading.Thread.__init__(self)
       print "iniciando socket servidor:"
       self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.s.bind((host, puerto))
       self.s.listen(10)
       
       #self.recibirDatos() ## Esperando la consulta del cliente
       self.parar = True
           
    def run(self):
        while self.parar:
            print "ESPERANDO CLIENTE"   
            self.sc, self.addr = self.s.accept()
            print "ESPERANDO DATOS"
            self.recibirDatos()
            respuesta = raw_input("introcucir respuesta para cliente")
            self.enviarDatos(respuesta)

       
           
           
        
        
        
        
    
    def enviarDatos(self, string):
        print "enviando datos:", string
        self.sc.send(string)
        
     
   
    def recibirDatos(self):
         recibido = self.sc.recv(1000)
         print "se recibio: ", recibido
        

    def cerrarSocket(self):
        print "cerrando socket"
        self.sc.close()
        self.s.close()
    def parar(self):
        self.parar = False
     
     