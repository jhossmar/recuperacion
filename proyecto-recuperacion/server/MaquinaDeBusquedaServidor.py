'''
Created on 13 de mar. de 2016

@author: 
'''
from _socket import AF_INET, SOCK_STREAM
import socket
class Servidor(object):
    
    def _init_(self):
        
        
    
    def iniciar(self):  
    
        mi_socket_server = socket.socket(AF_INET, SOCK_STREAM)
        address = ("localhost", 8087)
        mi_socket_server.bind(address)
        mi_socket_server.listen(backlog)  
        socket_cliente, datos_cliente = mi_socket_server.accept()
        bufsize = 1000
        datos_recibidos = socket_cliente.recv(bufsize)
        datos_a_enviar = "El server t manda saludos..." 
        socket_cliente.send(datos_a_enviar)
    
   