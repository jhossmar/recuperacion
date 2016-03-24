'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import random
from DB import DB

class Indexador(object):
    '''
    classdocs
    '''


    def __init__(self,listaTerminos,url):
        print "inicializando indexador... se encarga de los calculos de los pesos "  
        self.listaTerminos = listaTerminos
        self.url=url
        bd = DB("127.0.0.1","root","","recuperacion")
        bd.conectarConDB() 
        #GUARDANDO EN TABLA DOCUMENTO
        consulta1= "INSERT INTO DOCUMENTO(url) VALUES ('%s')" % url
        bd.setDatos(consulta1)
        ## ObteniendoIDDocumento
        consulta2= "SELECT DOCUMENTO.id_documento FROM DOCUMENTO ORDER BY  id_documento DESC"
        tuplas = bd.getDatos(consulta2)
        self.idDocumento=int(tuplas[0][0])
        bd.cerrarConexion()
        self.indexar()
        
    def indexar(self):
        # una vez seleccionado los terminos de un documento se deben calcular los pesos
        print "indexando documento:", self.url
        for termino in self.listaTerminos:
             df = self.hayarFrecuenciaDeTermino(termino, self.url)
             pesoTermino = self.calcularPeso(termino, self.url)
             self.GuardarEnDB(self.url,termino,df,pesoTermino)
        
        
    
    def GuardarEnDB(self,url,termino,df,pesoTermino):
        bd = DB("127.0.0.1","root","","recuperacion")
        bd.conectarConDB()
        
        
       
        
        ## GUARDANDO EN LA TABLA TBDOCTER
        consulta1= "INSERT INTO TBDOCTER(id_documento,no_termino,nu_frecuencia,nu_peso,nu_pesnor) VALUES(%i,'%s',%i,%f,%f)" % (self.idDocumento,termino,df,pesoTermino,pesoTermino)
        bd.setDatos(consulta1)
        bd.cerrarConexion()
        
      
    def calcularPeso(self, termino, url):
        print "calculando  peso del termino i para el documento j,  se guarda en tabla: TBFORPES"
        
        #Calcular las frecuencias de cada termino en la coleccion 
        
        
        # calculo del IDF 
      
        
        # claculo de la frecuencia en cada documento 
        
        
        # hallar el peso del termino en cada documento 
        peso = random.uniform(0.0, 1.0)
        print "peso del termino:",termino,"en:", url, "==", peso
        return peso
        

        
        
    def hayarFrecuenciaDeTermino(self,termino,url):
        print "hayando  TF del termino i en el documento j"
        #  si un termino aparece mucho en un documento, se supone que es importante en ese documento 
        df = self.listaTerminos.count(termino)
        print "frecuencia del termino: ", termino,"es",df 
        return df
          
          
    def calcularFactorIDF(self,termino,documento):
        print "calculando idf para el termino i, en el cocumento j, "
        # se utiliza la tabla TBFORIDF
        
        
   



