'''
Created on 13 de mar. de 2016

@author: marcelo
'''
import threading
from Crawer import Crawer
from Indexador import Indexador 
from MaquinaDeBusquedaServidor import MaquinaDeBusquedaServidor
from Crawler import Crawler







if __name__ == '__main__':
    crawer = Crawer(4,"http://localhost/paginas/index.html")
    crawer.start()
    indexador = Indexador()
    buscador = MaquinaDeBusquedaServidor() 
    #crawer = Crawler("http://www.python.org", 4, 5)
    #crawer.explore()
    # crawer.download_imgs()

     
     
    
