#!/usr/bin/python
# coding=UTF-8
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv)!=2:
	print("ERROR")
	print("Example: ./DUP_Ping.py 192.168.33.0/24")
	sys.exit()

address = str(sys.argv[1])
#prefix = address.split('.')[0]+'.'+address.split('.')[1]+'.'+address.split('.')[2]+'.'
prefix = subprocess.check_output("echo " + address + " | cut -d '.' -f 1-3",shell=True).strip()+"."
#print(prefix)

for addr in range(1,254):
	# 发送IP和UDP组成的Ping包
	response = sr1(IP(dst=prefix+str(addr))/UDP(dport=445),timeout=0.1,verbose=0)
	try:
		if int(response[IP].proto) == 1:
			print(prefix+str(addr))
	except:
		# print("not found")
		pass
