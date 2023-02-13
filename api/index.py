from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
import translators as ts # Переводим текст
import time
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        if "name" in dic:
            message = "Hello, " + dic["name"] + "!"
        else:
            message = "Hello, stranger!"

        self.wfile.write(message.encode())
        return
    def do_POST(self):
        content_len = self.rfile.read(int(self.headers.get('Content-Length')))
        content = json.loads(content_len)
        mytext = ts.google(content['text'], from_language=content['from'], to_language=content['to'])
        self.red.set(int(time.time()),content['text'])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(mytext.encode())
