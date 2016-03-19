'''
Created on 19 de mar. de 2016

@author: marcelo
'''

class DB(object):


    def __init__(self,host,usuario,contrasenia,nomDB):
        self.host = host
        self.usuario = usuario
        self.contrasenia = contrasenia  
        self.nombreDB = nomDB  
        
    
    def conectarConDB(self):
        print "estableciendo conexion con la base de datos"
        if(self.establecerConeccion()==False):
            return True
        else:
            return False
    
    def getDatos(self,consulta):
        print "obteniendo datos de la  DB "
        
    def setDatos(self,consulta):
        print "aumentando datos a DB"
        
            
            
        