'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import threading
import urllib2
from urllib2 import URLError
from cups import HTTP_ERROR
from mate._mate import URL_ERROR_URL


class Crawer(threading.Thread):
    

 
    def __init__(self,recursion,semilla):
        threading.Thread.__init__(self)
        self.recursion = recursion
        self.semilla = semilla
         
    
    def run(self):
        print "iniciando crawer"
        print "Buscando Documentos "
        try:
            f = urllib2.urlopen(self.semilla)
            print f.read() 
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
    
       
       
        

    
    
    