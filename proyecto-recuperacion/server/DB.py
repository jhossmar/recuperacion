'''
Created on 19 de mar. de 2016

@author: marcelo
'''
import MySQLdb

class DB(object):


    def __init__(self,host,usuario,contrasenia,nomDB):
        self.host = host
        self.usuario = usuario
        self.contrasenia = contrasenia  
        self.nombreDB = nomDB
        self.conexion = None
        
    
    def conectarConDB(self):
        self.conexion = self.establecerConeccion()
        if(self.conexion !=False):
            print "se conecto con la base de datos"
        
       
        
    def establecerConeccion(self):
        try:
            ###establecemos la coneccion con la base de datos: utilizamos Ip local en vez de localhost por problemas con xampp
            conexion = MySQLdb.connect("127.0.0.1","root","","recuperacion")
            ##preparamos cursor para poder manipular la db
            return conexion
        except Exception, e:
            print "verifique su conexion a la Base de DATOS"
            print e
            return False
 
    
    def getDatos(self,consulta):
        print "obteniendo datos de la  DB "
        cursor = self.conexion.cursor()
        cursor.execute(consulta)
        datos = cursor.fetchall()
        return datos
        
    def setDatos(self,consulta):
        print "aumentando datos a DB"
        try:
            cursor = self.conexion.cursor()
            cursor.execute(consulta)
            self.conexion.commit()
            print "OK OK"
        except Exception, e:
            print "no se pudo guardar los cambios "
            print e
        
    def cerrarConexion(self):
        self.conexion.close()
        
        
# bd = DB("127.0.0.1","root","","recuperacion")  
# bd.conectarConDB()
# bd.setDatos("INSERT INTO DOCUMENTO VALUES (8,'www.facebook.com')")
# print bd.getDatos("SELECT * FROM DOCUMENTO")
# bd.cerrarConexion()
            
        