'''
Created on 13 de mar. de 2016

@author: marcelo
'''
from Tkinter import *
class Interfaz(object):
    '''
    classdocs
    '''


    def __init__(self):
        print "iniciando Intefaz"
        self.c = Tk()
        self.c.title("RECUPERCION DE LA INFORMACION")
        
        ###configuraciones Ventana
        self.c.config(bg="blue")
        self.c.geometry("250x250")
        
        ## elementos 
        labe4 = Label(self.c,text="SISTEMA DE BUSQUEDA" )
        txt_consulta = Entry(self.c)
        btn_enviar = Button(self.c, text="ENVIAR") ## poner un command=<nombreFuncion>
        
        ##cargando elementos 
        labe4.pack()
        txt_consulta.pack()
        btn_enviar.pack()
        
        
    def mostrar(self):
        
        self.c.mainloop()
       
        