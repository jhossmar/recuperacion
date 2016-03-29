'''
Created on 16 de mar. de 2016

@author: marcelo
'''
# import urllib2
# # 
# import MySQLdb
# from bs4 import BeautifulSoup
# from cups import HTTP_ERROR
# from mate._mate import URL_ERROR_URL
# from urllib2 import URLError
# #from Socket import Socket
# import random
# url = "https://localhost/paginas/index.html"
# try:
#     f = urllib2.urlopen(url)
#     soup = BeautifulSoup(f)
#     contenido = soup.get_text()
#     palabras = contenido.split(' ')
#     frecuenciaDeTerminos = []
#     for palabra in palabras:
#         df = palabras.count(palabra)
#         var = palabra,df
#         frecuenciaDeTerminos.append(var)
#     print "IMPRIMIENDO TERMINOS MAS SU FRECUENCIA"
#     for df in frecuenciaDeTerminos:
#         print df[0],"->",df[1]
#         print ""
#           
     
#      
#     links = soup.find_all('a')
#     for link in links:
#         print link.get('href')#"http://"link.get('href')
#         
#     #print f.Read()       
# except HTTP_ERROR, e:
#      print "Ocurrio un error"
#     print e.code
# except URL_ERROR_URL, e:
#     print "Ocurrio un error"
#     print e.reason
# except URLError, e:
#     print "No se puede conectar con:'",url,"'"
#     print "verifique la direccion de la URL"
#     print "Verifique su conexion a internet ......"
# 
# try:
#      
#     ###establecemos la coneccion con la base de datos: utilizamos Ip local en vez de localhost por problemas con xampp
#     conexion = MySQLdb.connect("127.0.0.1","root","","recuperacion")
#     ##preparamos cursor para poder manipular la db
#     cursor = conexion.cursor()
#  
#     idDocumento= 2
#     termino = 'TERMINO'
#     df= random.uniform(10, 1000)
#     pesoTermino = random.uniform(0.00000, 1.00000)
#     consulta1= "INSERT INTO TBDOCTER(id_documento,no_termino,nu_frecuencia,nu_peso,nu_pesnor) VALUES(%i,'%s',%i,%f,%f)" % (idDocumento,termino,df,pesoTermino,pesoTermino)
#     
#     ##hacemos un query#
#     cursor.execute(consulta1)
#     conexion.commit()
#     
#     #datos = cursor.fetchall()
#     print "Version base de datos:"
#  
#  
#     ##cerramos o desconectamos de la base de tatos
#     conexion.close()
# except Exception, e:
#     print "verifique su conexion a la Base de DATOS"
#     print e
    
# respuestas = "|www.google.com;0.89;192.168.6.7|www.google.com;0.90;192.168.6.7|www.google.com;0.78;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.60;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|www.google.com;0.89;192.168.6.7|"
# listaDeRespuestas  =  respuestas.split('|')
# suma =0
# for respuesta in listaDeRespuestas[1:-1]:
#     #print respuesta
#      res = respuesta.split(";") 
#      print res[1]
#      suma = suma+integ(res[1])

#sk = Socket("127.0.0.1","8087")
# while 1:
#     print random.uniform(0.00000, 1.00000)
# import socket
# import sys
#  
# # Creando el socket TCP/IP socket.AF_INET, socket.SOCK_STREAM
# sock = socket.socket()
# # Enlace de socket y puerto
# #server_address = ("localhost", 10000)
# #print  'empezando a levantar %s puerto %s' % server_address
# sock.bind(("127.0.0.1", 8087))
#     
# while True:
#     # Esperando conexion
#     print >>sys.stderr, 'Esperando para conectarse'
#     conn, client_address = sock.accept()
#  
#     try:
#         print >>sys.stderr, 'concexion desde', client_address
#  
#         # Recibe los datos en trozos y reetransmite
#         while True:
#             data = conn.recv(19)
#             print >>sys.stderr, 'recibido "%s"' % data
#             if data:
#                 print >>sys.stderr, 'enviando mensaje de vuelta al cliente'
#                 conn.sendall(data)
#             else:
#                 print >>sys.stderr, 'no hay mas datos', client_address
#                 break          
#     finally:
#         # Cerrando conexion
#         conn.close()

# from Socket import Socket
# 
# sk= Socket("127.0.0.1",8087)
# sk.start()
# 
# f = open("diccionario_negativo.txt","r")
# diccionarioNegativo = f.read().split()
# 
# print diccionarioNegativo
# for t in diccionarioNegativo:
#     print t


import os
f = os.popen('ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
your_ip=f.read()
hola = "HOLA"
bola = "BOLA"
print type(your_ip)
print"%s%s"%(hola,bola)
print "SELECT %s fROM %s"%(your_ip,hola)



