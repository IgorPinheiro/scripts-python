#!/usr/bin/python

#Create a server TCP

import socket
import threading

bind_ip = "0.0.0.0"

bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))
server.listen(5)

print "[+] Listening on %s:%d" % (bind_ip,bind_port)

#Thead
def handle_client(client_socket):
	#show that the  client send
	request = client_socket.recv(4096)
	
	print "[+] Receive: %s " % request
	
	#Send a pack canback 
	client_socket.send("ACK!")

	client_socket.close()

while True:	
	client,addr = server.accept()
	
	print "[+] Accepted connection from: %s %d" % (addr[0],addr[1])

	#starting the thread of action client 
	client_handler = threading.Thread(target=handle_client,args=(client,))	
	client_handler.start()
