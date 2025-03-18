import os
from http.server import HTTPServer, CGIHTTPRequestHandler


web_dir = 'web_source/cgi-bin'
port = 80

os.chdir(web_dir)
server_addr = ("", port)
server_obj = HTTPServer(server_addr, CGIHTTPRequestHandler)
server_obj.serve_forever()
