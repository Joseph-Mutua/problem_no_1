# import all functions from the http.server module
from http.server import *

HOST = "127.0.0.1"
PORT= 8080


# create a class for handling GET and POST requests
class echoHandler(BaseHTTPRequestHandler):
     
    #  Create a function for the GET request
    def do_GET(self):
        
        # Respond with a success status code of 200
        self.send_response(200)
        
        # specify the file type to be send
        self.send_header("content-type", "text/html")
        self.end_headers()
        
        # The content to be displayed on the web-server
        self.wfile.write("<h1> My simple Python Webserver</h1>".encode())
        
    
        
        
# create an object to take the port number and server-name
server = HTTPServer((HOST, PORT), echoHandler)

# Run the server for as long as you like
server.serve_forever()
server.server_close()
print("Server is now running..")