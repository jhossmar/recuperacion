'''
Created on 16 de mar. de 2016

@author: marcelo
'''
import urllib2

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
    lista_palabras = {}
    for palabra in palabras:
        print palabra.upper()
    
    
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







