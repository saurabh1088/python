import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
use_custom_handler = True

class CustomHandler(Handler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == "__main__":
    if use_custom_handler:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"Serving at port {PORT}")
            httpd.serve_forever()
    else:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at port {PORT}")
            httpd.serve_forever()
