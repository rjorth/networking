#!/usr/bin/env python 

import scapy.all as scapy

def scan(ip):
	#discover clients on the same network 
	arp_req = scapy.ARP(pdst=ip)
	arp_req.show()
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	broadcast.show()
	#scapy.ls(scapy.Ether())
	arp_req_broadcast = broadcast/arp_req
	print(arp_req_broadcast.summary())
	arp_req_broadcast.show()

# >> route -n to check ip of router
# /24 to check the whole subnet (0 to 254)
scan("10.0.2./24")

