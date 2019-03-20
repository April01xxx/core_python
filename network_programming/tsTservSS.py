"""
用socketserver标准库实现的简易服务器
"""

import socketserver

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)

# 首先要实现一个request handler，标准库中提供了几种基础类型。
class MyTcpHandler(socketserver.StreamRequestHandler):
    """
    The request handler for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        self.data = self.rfile.readline().strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(self.data.upper())

if __name__ == '__main__':
    # Create the server, binding to localhost on port 21567
    with socketserver.TCPServer(ADDR, MyTcpHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
