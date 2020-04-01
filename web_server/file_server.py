#coding=utf-8
from http.server import BaseHTTPRequestHandler
import cgi
class   PostHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/records":
            return "Error."
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     }
        )
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        # print(self.client_address)
        # _client = 'Client: %sn' % self.client_address[0]
        # print(_client)
        # _agent = 'User-agent: %sn' % self.headers["user-agent"]
        # _path = 'Path: %sn' % self.path
        # _data = 'Form data:n'
        # _clent = _client.encode(encoding="utf-8")
        # _agnt = _agent.encode(encoding="utf-8")
        # _pah = _path.encode(encoding="utf-8")
        # _daa = _data.encode(encoding="utf-8")
        # self.send_header('User-agent', self.headers["user-agent"])
        # self.send_header('Content-Length', len(frame))
        # self.wfile.write(_client)
        # self.wfile.write(_agent)
        # self.wfile.write(_path)
        # self.wfile.write(_data)
        self.wfile.write("OK".encode(encoding="utf-8"))
        for field in form.keys():
            field_item = form[field]
            filename = field_item.filename
            filevalue  = field_item.value
            # filesize = len(filevalue)#文件大小(字节)
            #print len(filevalue)
	    #print (filename)
            with open(f"./records/{filename}",'wb') as f:
                f.write(filevalue)
        return 
 
def StartServer():
    from http.server import HTTPServer
    sever = HTTPServer(("",8000),PostHandler)
    sever.serve_forever()
 
 
 
 
if __name__=='__main__':
    StartServer()
