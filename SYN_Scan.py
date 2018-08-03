#!/usr/bin/python
# coding=UTF-8
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import time
import sys

if len(sys.argv)!=4:
	print("ERROR")
	print("Example: ./SYN_Scan.py 192.168.30.5 1 100")
	sys.exit()

ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for port in range(start,end):
	# 发送SYN包
	a = sr1(IP(dst=ip)/TCP(dport=port),timeout=1,verbose=0)
	time.sleep(1)
	if a == None:
		pass
	else:
		if int(a[TCP].flags)==18:
			print(port)
		else:
			pass
