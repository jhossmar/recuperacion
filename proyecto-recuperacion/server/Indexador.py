'''
Created on 13 de mar. de 2016

@author: marcelo
'''

class Indexador(object):
    '''
    classdocs
    '''


    def __init__(self,semilla,nivelRecurcion):
        self.semilla = semilla
        self.nivelRecursion = nivelRecurcion
    
    def imprimirCampos(self):
        print (self.semilla)
        print (self.nivelRecursion)
        
        
    

indexador = Indexador("localhost",4)
indexador.imprimirCampos()




