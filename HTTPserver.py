from http.server import BaseHTTPRequestHandler, HTTPServer
import os

#HTTPRequestHandler class
class test_HTTPRequestHandler(BaseHTTPRequestHandler): #this class implemetns BaseHTTPRequestHandler
	#handle GET command
	def do_GET(self):
			#send code 200 response
			self.send_response(200)
			
			#self header first
			self.send_header('Content-type','text-html')
			self.end_headers()

			#Send message back to client
			message="hey guys!"
			#write content as utf-8 data
			self.wfile.write(bytes(message,"utf-8"))
			return

def run():
	print('http server is starting...')

	#server settings
	server_address=('127.0.0.1',8081)
	httpd =  HTTPServer(server_address, test_HTTPRequestHandler)
	print('http server is running')
	httpd.serve_forever()

if __name__ == '__main__':
	run()

#Here we are going to create a simple http server.

#the code is contributed by Ankit solanki 