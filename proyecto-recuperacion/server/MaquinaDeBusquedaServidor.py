import socket



class MaquinaDeBusquedaServidor(object):
    
    def _init_(self):
        print "inicializando al maquina de busqueda del Servidor"
    
    def seleccionarTerminosConsulta(self):
        print "seleccionando terminos de la consulta del usuario"
        # se  guarda los terminos en la tabla ; TBCONTER  junto con el identificador del usuario y cosulta
         # se guarda tambien los pesos 
         
    def calcularPesosConsultaUsuario(self):
        print "calculando pesos de la consulta del usuario"
        
    def CalculoDeSimilaridad(self):
        print "calculando la similaridad entre la consulta del usuario y cada documento de la coleccion"
        
        '''
          propuesta para el calculo de similaridad desde la consulta a la DB:
          
          “ select doc.id_docume,doc.no_titulo,doc.no_resume,” +
          “ sum(dt.nu_pesnor*con.nu_peso) as nu_simila “ +
          “ from tbconter con,tbdocter dt,tbdocume doc where “ +
          “ doc.id_docume=dt.id_docume and “ +
          “ dt.no_termin=con.no_termin and “ +
          “ con.id_consul=? “ +
          “ group by doc.id_docume,doc.no_titulo,doc.no_resume “ +
          “ order by nu_simila desc “;
          
        '''
        
        
        
        
    def OrdenarYEnviarResultados(self):
        print "se esta ordenando resultados y se envia al usuario "










