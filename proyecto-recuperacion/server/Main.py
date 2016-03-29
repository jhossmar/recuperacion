'''
Created on 13 de mar. de 2016

@author: marcelo
'''


from Crawer import Crawer
from Indexador import Indexador 
from MaquinaDeBusquedaServidor import MaquinaDeBusquedaServidor
from Crawler import Crawler
from Socket import Socket

# import threading
# import Crawer
# import Socket


if __name__ == '__main__':
    #crawer =Crawer(4,"http://localhost/index.html")
   # crawer.start()
    print "sokets de escucha para la ip:  192.168.43.5"
    sk= Socket("192.168.43.5",8087)
    sk.start() 
    
    
     
    
