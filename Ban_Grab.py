#!/usr/bin/python

import socket
import select
import sys

if len(sys.argv)!=4:
	print("ERROR")
	print("Example: ./Ban_Grab.py 192.168.30.5 1 100")
	sys.exit()

ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for port in range(start,end):
	try:
		bangrab = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		bangrab.connect((ip,port))
		# ready是接收系统的消息，readable, writable, exceptional = select.select(inputs, outputs, inputs)
		ready = select.select([bangrab],[],[],1)
		if ready[0]:
			print("TCP Port " + stra(port) + "-" + bangrab.recv(4096))
			bangrab.close()
	except:
		pass
