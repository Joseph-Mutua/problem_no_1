# Web server (with optional secure communication)

Design a basic HTTP web-server application which can listen on a configurable TCP port and serve both static HTML and dynamically generated HTML by means of a chosen programming language, such as in the way Apache uses PHP. It is acceptable for this server application to support only a restricted subset of HTTP, such as GET or POST requests, and the only headers it must support are Content-Type and Content-Length.

## Solution

I solved this problem by building a simple web-server in Python that met the above requirements. 

## Step One
Import the following two modules at the top of your file:

-  [http.server](https://docs.python.org/3/library/http.server.html) - This module defines classes for implementing HTTP servers.


- [time](https://docs.python.org/3/library/time.html) - This module provides functions to handle various operations regarding time. We'll use it to render dynamic content for our POST requests. 
```python
# import all functions from the http.server module
from http.server import *
import time
```
## Step Two
Declare the ***HOST*** and ***PORT*** variables to hold values for the same. You can configure these values as you please.
```python
HOST = "127.0.0.1"
PORT = 8080
```
## Step Three
Create an ***echoHandler*** class to handle our GET and POST requests using ***BaseHTTPRequestHandler*** from the http.server module. 

Inside the class we'll create our first function ***do_GET()*** to handle GET requests. When the server receives a GET request, we'll respond with a success status code of ***200***. Set the *Content-type* and *Content-length* headers and then close the headers. 

Next, call the ***wfile*** method which contains the output stream for writing a response back to the client.

That's it for the GET requests function.
 
```python
# create a class for handling GET and POST requests
class echoHandler(BaseHTTPRequestHandler):

    #  Create a function for the GET request
    def do_GET(self):

        # Respond with a success status code of 200
        self.send_response(200)

        # specify the file type to be send
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", "2mb")
        self.end_headers()

        # The content to be displayed on the web-server
        self.wfile.write("<h1> My simple Python Webserver</h1>".encode())

```
## Step Four
To handle our POST requests we'll create a function ***do_POST*** that's similar to ***do_GET*** except this time round we'll respond with a dynamically generated *json* object. We'll employ the ***time*** module to generate the current year, month, date and time which we'll send back to the client when they send a POST request.


```python

    # create function for the POST request
    def do_POST(self):
        
        # Respond with a success status code of 200
        self.send_response(200)
        
        # Set the content headers
        self.send_header("Content-type", "application/json")
        self.send_header("Content-length", "2mb")
        self.end_headers()

        date = time.strftime("%Y-/%m-/%d, %H: %M: %S",
                             time.localtime(time.time()))
        message=f'The date today is {date}'
        print(message)
        
        self.wfile.write(message.encode())
```
## Step 5
Using the ***HTTPServer*** module from ***http.server*** create a server object and pass the ***HOST*** and ***PORT*** variables as parameters along with the ***echoHandler*** class. You can now run the server by calling the ***serve_forever()*** method and close it with the ***server_close()*** method.
```python
# create an object to take the port number and server-name
server = HTTPServer((HOST, PORT), echoHandler)

# Run the server for as long as you like
server.serve_forever()
server.server_close()

```

## Example
To run this server clone this repo from this [link](https://github.com/Joseph-Mutua/problem_no_1.git) into your project directory, then navigate to the folder on your terminal and run the code.


```bash
~/problem_no_1$ python3 webserver.py

127.0.0.1 - - [07/Jan/2022 12:10:05] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Jan/2022 12:10:05] "GET /favicon.ico HTTP/1.1" 200 -
127.0.0.1 - - [07/Jan/2022 12:10:07] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Jan/2022 12:10:07] "GET /favicon.ico HTTP/1.1" 200 -
127.0.0.1 - - [07/Jan/2022 12:10:20] "POST / HTTP/1.1" 200 -
The date today is 2022-/01-/07, 12: 10: 20
```
You can now jump into your bowser and got to the address *http://localhost:8080/* to view the live version (GET response)  or use the ***curl*** command to ping the address for the POST response.
