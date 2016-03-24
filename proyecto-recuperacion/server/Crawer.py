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
from Indexador import Indexador


class Crawer(threading.Thread):
    

 
    def __init__(self,recursion,semilla):
        threading.Thread.__init__(self)
        self.recursion = recursion
        self.semilla = semilla
         
    
    def run(self):
        print "iniciando crawer"
        print "Buscando Documentos "
        url=self.semilla #localhost/paginas/index.html
        count =0
        listaUrls = self.optenerlistaUrls(url) #[0,1]
        documento =  self.capturarDocumentos(url)
        if(documento != None):
            listaDeTterminos =self.analisisLexico(documento)
            self.indexarDocumento(listaDeTterminos,url)
       
        for link in  listaUrls:
            print link,"---->>>>"
            documento =  self.capturarDocumentos(link)
            if(documento != None):
                listaDeTterminos =self.analisisLexico(documento)
                self.indexarDocumento(listaDeTterminos,link)    
            else:
                print " no se pudo obtener  el contenido del documento. ", url
                print "verificar su coneccion a internet." 
        print "crawer finalizo!!!"   
             
                  
    def optenerlistaUrls(self,url):
        print "Obteniendo lista de urls a indexar"
        res =[]
        try:
            soup = self.capturarDocumentos(url)
            links =  soup.find_all('a')
            for link in links:
                newUrl= link.get('href')
                if(self.esCorrectaURL(newUrl)==True):
                    res.append( newUrl)
            return res
           
        except Exception, e:
            print "no se pudo conectar con :", url
            return res
        
#         if(self.contarLinks(url)==0 ):
#             print "no hay mas links"
#             print len(lista), "TAMANIOO DE LA LISTA DE URLS"
#             res=[]
#             for u in lista:
#                 print u
#                 res.append(u)
#             
#         else:
#             f = urllib2.urlopen(url)
#             soup = BeautifulSoup(f)
#             links =  soup.find_all('a')
#             lista.append(url)
#             for link in links:
#                 newUrl= link.get('href')#"http://"link.get('href')
#                 if(self.esCorrectaURL(newUrl)==True):
#                     print newUrl,"URL nueva"
#                     self.optenerlistaUrls(newUrl,lista)
#                     print "---------------------------"
                    
                    
                
    def esCorrectaURL(self,url):
        if(url == None):
            return False
        if (len(url) <= 2):
            return False
        if(url[0:10] == 'javascript'):
            return False
        if((url[0:7] == 'http://') or (url[0:8] == 'https://')):
            return True
        else:
            return False
        
    
    def contarLinks(self,url):
        f = urllib2.urlopen(url)
        soup = BeautifulSoup(f)
        links = soup.find_all('a')
        res = 0
        for link in links:
            res = res +1
        print "cantidad de links  en ", url, "= a ", res
        return res
        
          
        
    
        
        
        
    def indexarDocumento(self,listaTerminos,url):
        print "indexando documentos: ", url
        indexador = Indexador(listaTerminos,url)
#         bd = DB("127.0.0.1","root","","recuperacion")
#         bd.conectarConDB()
#        # ultimoid=self.UltimoIDDB()
#         consulta1= "INSERT INTO DOCUMENTO(url) VALUES ('%s')" % url
#         bd.setDatos(consulta1)
#         bd.cerrarConexion()
#         for termino in listaTerminos:
#             print "guardando en la BD el termino: ",termino
#             consulta= "INSERT INTO DOCUMENTO VALUES (1,'%s')" % termino
#             #consulta = "INSERT INTO DOCUMENTO VALUES(1,'localhost')"
#             print consulta,""
#             bd.setDatos(consulta)
    
        
        
        
        
    def UltimoIDDB(self):
         bd = DB("127.0.0.1","root","","recuperacion")
         bd.conectarConDB()
         consulta = "SELECT id_documento FROM DOCUMENTO" 
         res = bd.getDatos(consulta)
         print res
         ult=0
         for r in res:
             ult = ult+1
         return ult
         
         
       
         
         
         
         
    def  analisisLexico(self, documento ):
        # elimina signos de puntuacion,separadores,espacios, tabuladores tratamiento de mayusculas minusculas, se eliminan caracteres extranos 
        print "analizando lexico " 
        contenido = documento.get_text()
        palabras = contenido.split(' ')
        palabras_limpias = self.extraer_caracteres_extranios(palabras)
        lista_terminos = [] #lista de terminos de este documento#
        for palabra in palabras_limpias:
            if (self.verificarPalabra(palabra)==True):
                palabraMayuscula = palabra.upper()
                print "termino en mayuscula :", palabraMayuscula
                lista_terminos.append(palabraMayuscula)
        print " IMPRIMIENTDO LISTE DE TERMINOS"
        count =1
        for ter in lista_terminos:
            print count,": ",ter
            count = count+1
        return lista_terminos
        # alanalisis de terminos que representan el docuemrnto (los de mayor frecuencia en el documento )
        
            
                
    
    def extraer_caracteres_extranios(self, palabras):
        palabras_limpias =[]
        for palabra in palabras:
            print "limpiando palabra : ", palabra
            if (palabra != "-" and palabra !=' - ' and palabra !='- ' and palabra != ' -'): #No esta controlando que sea el caracter "-"#
                if (palabra[-1] != "," and palabra[-1] != "."):
                    print "se aumento  la palabra termino: ", palabra
                    palabras_limpias.append(palabra)
                    print ""
                else:
                    print " quitando '.' o ',' al final de la palabra: ", palabra
                    palabra_limpia  = palabra[0:-1]
                    print "palabra nueva = ", palabra_limpia
                    print "se aumento  el palabra: ", palabra_limpia
                    palabras_limpias.append(palabra_limpia)
                    print ""
        return palabras_limpias
         
     
    
    def capturarDocumentos(self,url):
        print "capturando documentos"  
        try:
            f = urllib2.urlopen(url)
            soup = BeautifulSoup(f)
            return soup
#            print f.read()
#             num = self.buscarUrls(url)
#             if(num!=0):
#                 print "numero de  URLS: ",num
#                 f.close()
#                 break
        except HTTP_ERROR, e:
            print "Ocurrio un error"
            print e.code
            return None
        except URL_ERROR_URL, e:
            print "Ocurrio un error"
            print e.reason
            return None
        except URLError, e:
            print "No se puede conectar con:'",self.semilla,"'"
            print "Verifique su conexion a internet ......"   
            return None
      
        
    def seleccionDeTerminosVacios(self):  # se realiza tantas veces como  documentos que se van a procesar
        print "seleccionando terminos vacios usando la tabla: TBTERM-VAC y gurdando indices en la tabla : TBDOCTER" 
        # Se eliminan prepociciones conjunciones etc. (delimita el numero de terminos que servira como indice)
        
        # se registra las palabras vacias en la tabla: TBTERM-VAC
        
        # registrar terminos (indices ) en la tabla TBDOCTER
    
    
    def verificarPalabra(self, palabra):
        ##Verifica las palabras con el diccionario invertido. 
        return True   
        


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
    
       
       
        

    
    
    