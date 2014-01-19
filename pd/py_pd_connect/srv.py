import socket

#--------------------- srv ----------------

R_PORT   = 2000   # socR
S_port   = 2010   # socS_main

class Srv:
    def connect(self):
        self.socR = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socR.bind(('',R_PORT))
        print 'Waiting for connection'
        self.socR.listen(1)
        self.connR, self.adrR = self.socR.accept()
        print 'Receive from :', R_PORT

        self.socS_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socS_main.connect(('',S_port))
        print 'Send to :', S_port

    def close(self):
        self.socR.close()
        self.socS_main.close()

    def send(self,a):
        print a

net = Srv()
