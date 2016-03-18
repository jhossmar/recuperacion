'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import threading
import urllib2
from urllib2 import URLError
from cups import HTTP_ERROR
from mate._mate import URL_ERROR_URL
from bs4 import BeautifulSoup



class Crawer(threading.Thread):
    

 
    def __init__(self,recursion,semilla):
        threading.Thread.__init__(self)
        self.recursion = recursion
        self.semilla = semilla
         
    
    def run(self):
        print "iniciando crawer"
        print "Buscando Documentos "
        url=self.semilla
        count =0
        while count <=self.recursion:
           documento =  self.capturarDocumentos(url)
           self.analisisLexico(documento)
            
           

   
    def  analisisLexico(self, documento ):
        print "analizando lexico " 
        contenido = documento.get_text()
        palabras = contenido.split(' ')
        lista_palabras = {}
        for palabra in palabras:
            print palabra.upper()
            
        # elimina signos de puntuacion,separadores,espacios, tabuladores tratamiento de mayusculas minusculas, se eliminan caracteres extranos 
        
        
        
        # alanalisis de terminos que representan el docuemrnto (los de mayor frecuencia en el documento )
            
    
     
    
    def capturarDocumentos(self,url):
        print "capturando documentos"  
        try:
            f = urllib2.urlopen(url)
            soup = BeautifulSoup(f)
            return soup
            #print f.read()
#             num = self.buscarUrls(url)
#             if(num!=0):
#                 print "numero de  URLS: ",num
#                 f.close()
#                 break
        except HTTP_ERROR, e:
            print "Ocurrio un error"
            print e.code
        except URL_ERROR_URL, e:
            print "Ocurrio un error"
            print e.reason
        except URLError, e:
            print "No se puede conectar con:'",self.semilla,"'"
            print "Verifique su conexion a internet ......"   
      
        
    def seleccionDeTerminosVacios(self):  # se realiza tantas veces como  documentos que se van a procesar
        print "seleccionando terminos vacios usando la tabla: TBTERM-VAC y gurdando indices en la tabla : TBDOCTER" 
        # Se eliminan prepociciones conjunciones etc. (delimita el numero de terminos que servira como indice)
        
        # se registra las palabras vacias en la tabla: TBTERM-VAC
        
        # registrar terminos (indices ) en la tabla TBDOCTER
        
        


    def actualizarTablaDeTerminos(self):
        print ("actualizando tabla TBDOC-TERM de terminos ")  
    
    def registrarDocEnTabla(self):      
        print ("Registrando  documento en tabla TBDOCUMENTO")
        
        
    def buscarUrls(self,url):
        print "buscando links"
        f = urllib2.urlopen(url)
        soup = BeautifulSoup(f)
        count = 0
        for link in soup.findAll('a'):
            print "buscando URLs en ", link.get('href')
            self.buscarUrls(link.get('href'))
            
            count = count +1      
        return count
    
       
       
        

    
    
    