#!/usr/bin/python
import socket

t_host = "186.192.90.5"
t_port = 80


print "cliente UDP By: Igor Pinheiro"
print "chmod +x udp-client.py"
print "Ex: ./udp-client.py"

#Creating object
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send data
socket.sendto("AAABBBCCC",(t_host,t_port))

#Get data
data, addr = socket.recvfrom(4096)

print data
