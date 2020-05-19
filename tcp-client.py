#!/usr/bin/python

import socket 

t_host = "localhost"
t_port = 9999

#Create an object socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Socket conection

socket.connect((t_host,t_port))

#Send data

socket.send("HEAD / HTTP/1.1\r\nHost:google.com.br\r\n\r\n")
print socket
#get some data:

soc_rec = socket.recv(4096)

print ("[+] Get data [+]: ", soc_rec)

