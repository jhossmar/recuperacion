'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import threading
from Crawer import Crawer
from Indexador import Indexador 
from MaquinaDeBusquedaServidor import MaquinaDeBusquedaServidor






if __name__ == '__main__':
    crawer = Crawer(4,"http://localhost")
    crawer.start()
    indexador = Indexador()
    buscador = MaquinaDeBusquedaServidor()   
     
    
