from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from deep_translator import GoogleTranslator
import time
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = "Server is ok"
        self.wfile.write(message.encode())
        return
    def do_POST(self):
        content_len = self.rfile.read(int(self.headers.get('Content-Length')))
        content = json.loads(content_len)
        check = 0
        errors = ""
        if 'text' in content:
            check += 1
            if len(content['text']) <= 100:
                check += 1
            else:
                errors.join("Error: content length incorrect\n")
        else:
            errors.join("tag 'text' does not exist\n")
        if 'from' in content:
            check += 1
        else:
            errors.join("Error: tag «from» does not exist\n")
        if 'to' in content:
            check += 1
        else:
            errors.join("Error: tag «from» does not exist\n")
        if (check == 4):
            mytext = GoogleTranslator(source=content['from'], target=content['to']).translate(content['text'])
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(mytext.encode())
        else:
            self.send_response(500)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(errors)
