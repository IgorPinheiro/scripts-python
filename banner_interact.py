#!/usr/bin/python
#IGOR PINHEIRO 25/05/2020

import socket

print "Interacting with the server"

ip = raw_input ("WHat's IP: ")
port = 21

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))
banner = client.recv(2048)
print banner


print "Sending User"
client.send("USER user\r\n")
banner = client.recv(2048)
print banner

print "Sending password "
client.send("PASS anonymous\r\n")
banner = client.recv(2048)
print banner
