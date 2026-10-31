#!/usr/bin/env python3
"""
Local development & verification server that serves both static files (index.html, data/*)
and the Vercel serverless endpoint (/api/index) on http://127.0.0.1:8080
"""
import http.server
import socketserver
import os
import json
from api.index import handler as ApiHandler

PORT = 8080

class CombinedHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            ApiHandler.do_GET(self)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path.startswith("/api/"):
            ApiHandler.do_POST(self)
        else:
            self.send_error(404)

    def _send_json(self, status_code: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    with socketserver.TCPServer(("127.0.0.1", PORT), CombinedHandler) as httpd:
        print(f"Serving CCM Internal Audit Portal on http://127.0.0.1:{PORT}")
        httpd.serve_forever()
