'''
Created on 16 de mar. de 2016

@author: marcelo
'''
import urllib2
# 
# import MySQLdb
from bs4 import BeautifulSoup
from cups import HTTP_ERROR
from mate._mate import URL_ERROR_URL
from urllib2 import URLError
url = "https://localhost/paginas/index.html"
try:
    f = urllib2.urlopen(url)
    soup = BeautifulSoup(f)
    contenido = soup.get_text()
    palabras = contenido.split(' ')
    frecuenciaDeTerminos = []
    for palabra in palabras:
        df = palabras.count(palabra)
        var = palabra,df
        frecuenciaDeTerminos.append(var)
    print "IMPRIMIENDO TERMINOS MAS SU FRECUENCIA"
    for df in frecuenciaDeTerminos:
        print df[0],"->",df[1]
        print ""
         
     
     
    links = soup.find_all('a')
    for link in links:
        print link
    #print f.Read()       
except HTTP_ERROR, e:
    print "Ocurrio un error"
    print e.code
except URL_ERROR_URL, e:
    print "Ocurrio un error"
    print e.reason
except URLError, e:
    print "No se puede conectar con:'",url,"'"
    print "verifique la direccion de la URL"
    print "Verifique su conexion a internet ......"
# 
# try:
#     
#     ###establecemos la coneccion con la base de datos: utilizamos Ip local en vez de localhost por problemas con xampp
#     conexion = MySQLdb.connect("127.0.0.1","root","","recuperacion")
#     ##preparamos cursor para poder manipular la db
#     cursor = conexion.cursor()
# 
#     ##hacemos un query#
#     cursor.execute("SELECT * FROM DOCUMENTO")
#     datos = cursor.fetchall()
#     print "Version base de datos:",datos
# 
# 
#     ##cerramos o desconectamos de la base de tatos
#     conexion.close()
# except Exception, e:
#     print "verifique su conexion a la Base de DATOS"
#     print e
    








