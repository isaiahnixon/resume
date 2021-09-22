"""
@file server.py

Creates a local development server.

Based on: https://linuxhint.com/use-python-simplehttpserver/
"""

import http.server

HOST = "localhost"
PORT = 4000

# Define class to display the index page of the web server
class PythonServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        else:
            try:
                route,extension = self.path.split('.', 1)
            except ValueError:
                self.path += '.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Declare object of the class
webServer = http.server.HTTPServer((HOST, PORT), PythonServer)

# Print the URL of the webserver
print("Server started http://%s:%s" % (HOST, PORT))

try:
    # Run the web server
    webServer.serve_forever()

except KeyboardInterrupt:
    # Stop the web server
    webServer.server_close()
    print("The server is stopped.")