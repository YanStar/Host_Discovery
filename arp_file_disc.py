#!/usr/bin/python
# coding=UTF-8
import logging	# 导入日志模块
import subprocess	# 导入subprocess模块，实现系统命令的调用
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)	# 对日志进行记录
from scapy.all import *	 # 导入scapy模块

# 判断输入的命令参数是不是等于2
if len(sys.argv)!=2:
	print("ERROR")
	print("Example: ./arp_disc.py host.txt")
	# 退出程序
	sys.exit()

filename = str(sys.argv[1])
file = open(filename,'r')

for addr in file:
	# 发送ARP包，verbose=0是表示不显示详细信息
	answer = sr1(ARP(pdst=addr.strip()),timeout=0.1,verbose=0)
	if answer == None:
		pass
	else:
		print(addr.strip())
