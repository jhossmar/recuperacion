'''
Created on 13 de mar. de 2016

@author: marcelo
'''
from Tkinter import *
from Socket import Socket
class Interfaz(object):

    '''
    classdocs
    '''


    def __init__(self):
        print "iniciando Intefaz"
        self.c = Tk()
        self.txt_consulta = Entry(self.c)
        self.c.title("RECUPERCION DE LA INFORMACION")
        
        ###configuraciones Ventana
        self.c.config(bg="blue")
        self.c.geometry("250x250")
        
        ## elementos 
        labe4 = Label(self.c,text="SISTEMA DE BUSQUEDA" )
        
        btn_enviar = Button(self.c, text="ENVIAR",command=lambda:self.enviar(Entry.get(self.txt_consulta))) ## poner un command=<nombreFuncion>
        
        ##cargando elementos 
        labe4.pack()
        self.txt_consulta.pack()
        btn_enviar.pack()
        
        
    def mostrar(self):
        
        self.c.mainloop()
    
    def enviar(self,consulta):
        #print consulta
        listaServidores = ['109876543','192.168.43.5','192.168.3.2']
        listaSocketEsperando = []
        for servidor in listaServidores:
            sk = Socket(servidor,consulta)
            sk.start()
            #listaSocketEsperando.append(sk)
            print "next IP"
            
       
        