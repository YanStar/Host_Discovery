#! /usr/bin/python
# coding=UTF-8
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

# 判断是否是一个合格的僵尸机
def ipid(zombie):
    # sr1发送过后还会接收返回的数据包
    repaly1 = sr1(IP(dst=zombie) / TCP(flags="SA"), timeout=2, verbose=0)
    # send发送过后不接收返回的数据包
    send(IP(dst=zombie) / TCP(flags="SA"), verbose=0)
    repaly2 = sr1(IP(dst=zombie) / TCP(flags="SA"), timeout=2, verbose=0)
    # print(repaly2[IP].id)
    if repaly2[IP].id == (repaly1[IP].id + 2):
        print("IPID sequence is incremental and target appears to be idle,ZOMBIE LOCATED")
        responese = input("Do you want to use this zombie to perform a scan ? (Y or N ): ")
        if responese.upper() == "Y":
            target = input("Enter the ip address of the target system: ")
            range_port = target.split(" ")[1]
            start_port = range_port.split("-")[0]
            end_port = range_port.split("-")[1]
            zombiescan(target, zombie, start_port, end_port)
    else:
        print("Either the IPID sequence is not incremental or the target is not idle. NOT A GOOD ZOMBIE")


def zombiescan(target, zombie, start_port, end_port):
    print("\nScanning target " + target + " with zombie " + zombie)
    print("\n------------ Open Port on Target -----------\n")
    for port in range(int(start_port), int(end_port)):
        try:
            start_val = sr1(IP(dst=zombie) / TCP(flags="SA", dport=port), timeout=1, verbose=0)
            send(IP(src=zombie, dst=target) / TCP(flags="S", dport=port), verbose=0)
            end_val = sr1(IP(dst=zombie) / TCP(flags="SA", dport=port), timeout=1, verbose=0)
            if end_val[IP].id == (start_val[IP].id + 2):
                print(port)
        except:
            pass


print("----------------Zombie Scan Suite-----------------\n")
print("1.   Identify Zombie Host\n")
print("2.   Perfrom Zombie Scan\n")
ans = input("Select an Option (1 or 2): ")

if ans == "1":
    zombie = input("Enter IP addresss to test IPID sequence: ")
    ipid(zombie)
else:
    if ans == "2":
        zombie = input("Enter IP address for zombie system: ")
        target = input("Enter IP address for scan target: ")
        range_port = target.split(" ")[1]
        start_port = range_port.split("-")[0]
        end_port = range_port.split("-")[1]
        zombiescan(target, zombie, start_port, end_port)
