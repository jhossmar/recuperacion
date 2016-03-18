'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import threading
import urllib2
from urllib2 import URLError
from cups import HTTP_ERROR
from mate._mate import URL_ERROR_URL
from BeautifulSoup import BeautifulSoup



class Crawer(threading.Thread):
    

 
    def __init__(self,recursion,semilla):
        threading.Thread.__init__(self)
        self.recursion = recursion
        self.semilla = semilla
         
    
    def run(self):
        print "iniciando crawer"
        print "Buscando Documentos "
        url=self.semilla
        while 1:
            try:
                f = urllib2.urlopen(url)
                print f.read()
#                 num = self.buscarUrls()
#                 if(num==0):
#                     print "numero de  URLS: ",num
#                       
                f.close()
            except HTTP_ERROR, e:
                print "Ocurrio un error"
                print e.code
            except URL_ERROR_URL, e:
                print "Ocurrio un error"
                print e.reason
            except URLError, e:
                print "No se puede conectar con:'",self.semilla,"'"
                print "Verifique su conexion a internet ......"

   
    def  analisisLexico(self):
        print "analizando lexico "   
        
        # alanalisis de terminos que representan el docuemrnto (los de mayor frecuencia en el documento )
        
        
        # elimina signos de puntuacion,separadores,espacios, tabuladores tratamiento de mayusculas minusculas, se eliminan caracteres extranos 
        
    
     
    
    def capturarDocumentos(self):
        print "capturando documentos"     
      
        
    def seleccionDeTerminosVacios(self):  # se realiza tantas veces como  documentos que se van a procesar
        print "seleccionando terminos vacios usando la tabla: TBTERM-VAC y gurdando indices en la tabla : TBDOCTER" 
        # Se eliminan prepociciones conjunciones etc. (delimita el numero de terminos que servira como indice)
        
        # se registra las palabras vacias en la tabla: TBTERM-VAC
        
        # registrar terminos (indices ) en la tabla TBDOCTER
        
        


    def actualizarTablaDeTerminos(self):
        print ("actualizando tabla TBDOC-TERM de terminos ")  
    
    def registrarDocEnTabla(self):      
        print ("Registrando  documento en tabla TBDOCUMENTO")
        
        
    def buscarUrls(self):
        print "buscando links"
        count = 0
        for link in BeautifulSoup.soup.findAll('a'):
            print (link.get('href'))
            count = count +1      
        return count
    
       
       
        

    
    
    