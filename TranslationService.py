from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json
import translators as ts # Переводим текст
import time

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
  server_address = ('', 8000)
  httpd = server_class(server_address, handler_class)
  try:
      httpd.serve_forever()
  except KeyboardInterrupt:
      httpd.server_close()
class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Был получен GET-запрос.</body></html>'.encode())
    def do_POST(self):

        content_len = self.rfile.read(int(self.headers.get('Content-Length')))
        content = json.loads(content_len)
        mytext = ts.google(content['text'], from_language=content['from'], to_language=content['to'])
        self.red.set(int(time.time()),content['text'])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(mytext.encode())
run(handler_class=HttpGetHandler)