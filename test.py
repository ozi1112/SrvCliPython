from SocketServer import *
from threading import *
import socket
import json

MSGLEN = 128


class MessageContainer:

    class MessageType:
        Chat = 0,
        ServerCmd = 1

    class CommandRcv: #: cli -> srv
        Null = 0,
        Join = 1,
        Leave = 2
    
    class CommandResp: #: srv -> cli

    def __init__(self, sender, command, args):
        """Communication message struct

        Arguments:

            @ sender : str
                Nickname

            @ command : int
                Command ID

            @ command ID : int
                Unique for client msg ID

            @ args : list
                Args list

        """

        self.args = args
        self.command = command
        self.sender = sender

    def getString(self):
        json.dumps(self)

class RequestHandler(BaseRequestHandler):
    def setup(self):
        """Authorization."""
        print "new conn", self.client_address



    def handle(self):
        """Chat client handler."""
        bytesReaded = 1
        while bytesReaded > 0:
            try:
                bytesReaded = self.request.recv(1024)
                print self.client_address, "~~ ", bytesReaded
                self.server.sendToAll(self.request, bytesReaded)
            except Exception as ex:
                print "DC ", self.client_address, " ", ex
                break

    def finish(self):
        pass
        

class ServerHandler(ThreadingTCPServer):
    socket_list = []


    def verify_request(self, request, client_address):
        """Verify the request.  May be overridden.

        Return True if we should proceed with this request.
        """
        # TODO: Authorization // create account
        self.socket_list.append( request )
        print "Clients connected: ", len(self.socket_list)
        return True

    def close_request(self, request):
        """Called to clean up an individual request."""
        print "Close request ", request
        self.socket_list.remove( request )
        request.close()
    
    def sendToAll(self, request, message):
        for sock in self.socket_list:
            sock.sendall(message)


#srv = ServerHandler(("127.0.0.1", 8080), RequestHandler)
#srv.serve_forever()