'''
Created on 23 de mar. de 2016

@author: marcelo
# '''

from Socket import Socket

sk= Socket("127.0.0.1","CONSULTA:CLIENTE")
sk.start()










# import socket
# import sys
#  
# # Creando un socket TCP/IP "socket.AF_INET, socket.SOCK_STREAM"
# sock = socket.socket()
#  
# # Conecta el socket en el puerto cuando el servidor este escuchando
# server_address = ('localhost', 10000)
# print >>sys.stderr, 'conectando a %s puerto %s' % server_address
# sock.connect(('127.0.0.1', 8087))
# try:
#      
#     # Enviando datos
#     message = 'Este es el mensaje.  Se repitio.'
#     print >>sys.stderr, 'enviando "%s"' % message
#     sock.sendall(message)
#  
#     # Buscando respuesta
#     amount_received = 0
#     amount_expected = l en(message)
#      
#     while amount_received < amount_expected:
#         data = sock.recv(19)
#         amount_received += len(data)
#         print >>sys.stderr, 'recibiendo "%s"' % data
#  
# finally:
#     print >>sys.stderr, 'cerrando socket'
#     sock.close()