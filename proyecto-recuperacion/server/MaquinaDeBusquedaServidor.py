
#from Socket import  Socket
from DB import DB
import unicodedata
import os

class MaquinaDeBusquedaServidor(object):
    
    def __init__(self,consulta):
        print "inicializando Maquina De Busqueda servidor"
        self.consulta = consulta
        self.lista_terminos_consulta = self.obtenerTerminos(consulta)
        self.respuesta = "|"
        self.ipLocal = self.optenerIP()
        print "LISTA DE TERMINOS DE LA CONSULA"
        for termino in self.lista_terminos_consulta:
            print termino
        
       
          
            
    def generarRespuesta(self):
        print "generando respuesta "
        #### FORMATO = |url;angulo;IP|
        
        ##Obteniendo informacion de la base de datos
        bd = DB("127.0.0.1","root","","recuperacion")
        bd.conectarConDB()
        agregado = ""
        for termino in self.lista_terminos_consulta:
             agregado =agregado+"and TBDOCTER.no_termino='%s'"%termino
             
        consulta= "SELECT   url, nu_peso FROM DOCUMENTO, TBDOCTER WHERE DOCUMENTO.id_documento= TBDOCTER.id_documento %s GROUP BY url"%agregado   
        print consulta
        tuplas = bd.getDatos(consulta)
        bd.cerrarConexion()
        #print tuplas
        #####FORMANDO LA RESPUESTA PARA EL CLIENTE#####
        for tupla in tuplas:
            print tupla
            self.respuesta = self.respuesta+"%s;%f;%s|"%(tupla[0],tupla[1],self.ipLocal)
        print "#############RESPUESTA######"
        print str(self.respuesta)
        return str(self.respuesta)
        
        
        
    def obtenerTerminos(self,consulta):
        print "opteniendo terminos de la consulta"
        lista_terminos=consulta.split()
        ####COMVERTIMOS a MAYSCULA
        res = []
        for termino in lista_terminos:
            if(self.estaEnDiccionarioNegativo(termino)!=True):
                terminoMayuscula=termino.upper()
                TerminoSinTilde= self.elimina_tildes(unicode(terminoMayuscula))
                res.append(unicode(TerminoSinTilde))
                print ""
                print ""
                print ""
        return res
   

    def estaEnDiccionarioNegativo(self,termino):
        print "Buscando en diccionario negatibo el termino->>", termino 
        f = open("diccionario_negativo.txt","r")
        cadena = f.read()
        diccionarioNegativo=cadena.split()
        conteo = diccionarioNegativo.count(termino)
        if (conteo>0):
            print "true "
            return True
        else:
            print "false"
            return False
        
    def optenerIP(self):
        f = os.popen('ifconfig wlan0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
        your_ip=f.read()
        return str(your_ip)
          


    def seleccionarTerminosConsulta(self):
        print "seleccionando terminos de la consulta del usuario"
        # se  guarda los terminos en la tabla ; TBCONTER  junto con el identificador del usuario y cosulta
        # se guarda tambien los pesos 
         
    def calcularPesosConsultaUsuario(self):
        print "calculando pesos de la consulta del usuario"
        
    def CalculoDeSimilaridad(self):
        print "calculando la similaridad entre la consulta del usuario y cada documento de la coleccion"

        
        
        
    def OrdenarYEnviarResultados(self):
        print "se esta ordenando resultados y se envia al usuario "
    
    
    def elimina_tildes(self,s):
        return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 
  
### PROBANDO CLASE
# procesador = MaquinaDeBusquedaServidor("Ejemplo de una consulta de un cliente")
# print procesador.generarRespuesta()
  

       










