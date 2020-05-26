#!/usr/bin/python
#IGOR PINHEIRO 25/05/2020

import socket


ip = raw_input ("WHat's IP: ")
port = input ("What's Port: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip,port))

banner = client.recv(2048)
print banner
