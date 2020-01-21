#!/usr/bin/env python 

import scapy.all as scapy

def scan(ip):
	#discover clients on the same network 
	scapy.arping(ip)

# >> route -n to check ip of router
scan("10.0.2.1")

