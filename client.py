from socket import *
import sys
from time import sleep
from threading import Thread


class Client:
    MSGLEN = 128
    HOST, PORT = "localhost", 8080
    data = "NICK"

    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        pass
    
    def Connect(self):
        self.sock.connect((self.HOST, self.PORT))
        self.thread = Thread(target=self.RecvThread, args=(self.sock,) )
        self.thread.start()
        pass

    def RecvThread(self, sock):
        while True:
            received = sock.recv(1024)
            print "Received: {}".format(received)

    def sendPacket(self, msg):
        sent = self.sock.sendall(msg)




client = Client()
client.Connect()
client.sendPacket("Nick")


while True:
    print "Write message..."
    msg = raw_input()
    client.sendPacket(msg)
    
    