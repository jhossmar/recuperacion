'''
Created on 16 de mar. de 2016

@author: marcelo
'''
import urllib2
from cups import HTTP_ERROR
from mate._mate import URL_ERROR_URL
from urllib2 import URLError
url = "https://localhost/"
try:
    f = urllib2.urlopen(url)
    print f.Read()       
except HTTP_ERROR, e:
    print "Ocurrio un error"
    print e.code
except URL_ERROR_URL, e:
    print "Ocurrio un error"
    print e.reason
except URLError, e:
    print "No se puede conectar con:'",url,"'"
    print "Verifique su conexion a internet ......"







