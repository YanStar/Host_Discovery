#!/usr/bin/python
# coding=UTF-8
import logging
import subprocess
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv)!=2:
	print("ERROR")
	print("Example: ./ping1.py 192.168.33.0/24")
	sys.exit()

address = str(sys.argv[1])
#prefix = address.split('.')[0]+'.'+address.split('.')[1]+'.'+address.split('.')[2]+'.'
prefix = subprocess.check_output("echo " + address + " | cut -d '.' -f 1-3",shell=True).strip()+"."
#print(prefix)

for addr in range(0,255):
	# 向目标地址发送ping包
	a = sr1(IP(dst=prefix+str(addr))/ICMP(),timeout=0.1,verbose=0)
	if a == None:
		pass
	else:
		print (prefix + str(addr))
