#!/usr/bin/env python3
"""Serves static files and proxies /api/* to Mealie on port 9000."""
import http.server, urllib.request, urllib.error

MEALIE = "http://localhost:9000"
HOP_BY_HOP = {"connection","keep-alive","proxy-authenticate","proxy-authorization",
               "te","trailers","transfer-encoding","upgrade"}

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/api/"):
            self._proxy()
        else:
            super().do_GET()

    def do_OPTIONS(self):
        if self.path.startswith("/api/"):
            self._proxy()
        else:
            self.send_error(405)

    def _proxy(self):
        url = MEALIE + self.path
        fwd_headers = {k: v for k, v in self.headers.items()
                       if k.lower() not in HOP_BY_HOP}
        req = urllib.request.Request(url, headers=fwd_headers, method=self.command)
        try:
            with urllib.request.urlopen(req) as resp:
                body = resp.read()
                self.send_response(resp.status)
                for k, v in resp.headers.items():
                    if k.lower() not in HOP_BY_HOP:
                        self.send_header(k, v)
                self.end_headers()
                self.wfile.write(body)
        except urllib.error.HTTPError as e:
            body = e.read()
            self.send_response(e.code)
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass  # silence request log noise

if __name__ == "__main__":
    http.server.test(HandlerClass=Handler, port=8080)
