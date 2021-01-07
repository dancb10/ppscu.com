from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class HServer(BaseHTTPRequestHandler):

    @staticmethod
    def get_response(method, body=''):
        response = BytesIO()
        response.write(b'Backend Server UP!\n')
        response.write(b'%s request\n' % method.encode())
        if body:
            response.write(b'Received: %s\n' % body.encode())
        return response

    def do_GET(self):
        print(str(self.path), str(self.headers))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = self.get_response(method='GET')
        self.wfile.write(response.getvalue())

    def do_POST(self):
        print(str(self.path), str(self.headers))
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = self.get_response(method='POST', body=str(body))
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('0.0.0.0', 9090), HServer)
httpd.serve_forever()
