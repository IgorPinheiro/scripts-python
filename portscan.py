#!/usr/bin/python
#IGOR PINHEIRO 25/05/2020

import socket,sys

#if len(sys.argv) <= 0:
#	print "User mode: ./portscan.py ip.to.verification"
	
#else:
for port in range(1, 65535):

	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if my_socket.connect_ex((sys.argv[1],port)) == 0:

		print "[+]--> Oper Port[" ,port, "] <--[+]"
		my_socket.close()

