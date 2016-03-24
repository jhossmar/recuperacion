
from Socket import  Socket
class MaquinaDeBusquedaServidor(object):
    
    def __init__(self):
        print "inicializando al maquina de busqueda del Servidor"
        sk= Socket("127.0.0.1",8087)
        sk.start()
          
            
            
            
  
    
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










