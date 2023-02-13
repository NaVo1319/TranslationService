
from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
import time
from gtts import gTTS # Озвучиваем текст
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = "server is ready"
        self.wfile.write(message.encode())
        return
    def do_POST(self):
        content_len = self.rfile.read(int(self.headers.get('Content-Length')))
        content = json.loads(content_len)
        file = gTTS(text=content['text'], lang=content['lang'], slow=False)
        self.send_response(200)
        self.send_header("Content-type", "audio/mpeg")
        self.end_headers()
        self.wfile.write(file.read())
