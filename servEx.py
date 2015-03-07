#!/usr/bin/env python

import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        
        #self.request.sendall(self.data.upper())
        self.request.sendall("I am a simple tcp server made by Marios and I am answering your request....!")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Ctrl-C to exit
    server.serve_forever()