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
	print("Example: ./UDP_Scan.py 192.168.30.5 1 100")
	sys.exit()

ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for port in range(start,end):
	# 发送UDP包，如果没收到响应，则说明开放
	a = sr1(IP(dst=ip)/UDP(dport=port),timeout=1,verbose=0)
	time.sleep(1)
	if a == None:
		print(port)
	else:
		pass
