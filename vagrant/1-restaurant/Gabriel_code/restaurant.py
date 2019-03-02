from http.server import BaseHandlerRequest, HTTPServer
import cgi
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Foreignkey, Integer, String

class HandlerRequest(BaseHandlerRequest):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        output 


    def do_POST(self):


if __name__ == '__main__':
    try:
        port = 8000
        server = HTTPServer(('',port),HandlerRequest)
        print('LISTENING ON %s', % port)
        server.serve_forever()
    except KeyBoardInterrupt:
        server.socket_close()