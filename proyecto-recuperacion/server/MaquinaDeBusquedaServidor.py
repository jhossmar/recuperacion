import socket

s = socket.socket()
s.bind(("localhost", 9999))
s.listen(1)
sc, addr = s.accept()
while True:
    
    recibido = sc.recv(1000)
    if recibido == "quit":
       break
    print "Recibido:", recibido
    
   
   

sc.close()
s.close()
