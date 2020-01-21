#!/usr/bin/env python 

import scapy.all as scapy

def scan(ip):
	#discover clients on the same network 
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broadcast = broadcast/arp_req
	answered = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0] #only want answered

	print("IP\t\t\tMAC Address\n--------------------------")
	for element in answered:
		print(element[1].psrc + "\t\t" + element[1].hwsrc)
# >> route -n to check ip of router
# /24 to check the whole subnet (0 to 254)
scan("10.0.2./24")

