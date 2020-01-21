#!/usr/bin/env python 

import scapy.all as scapy
import optparse

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="Target IP / IP range")
	options, arguments = parser.parse_args()
	return options 

def scan(ip):
	#discover clients on the same network 
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broadcast = broadcast/arp_req
	answered = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0] #only want answered

	clients_list = []
	for element in answered:
		client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

def print_result(results_list):
	print("IP\t\t\tMAC Address\n--------------------------")
	for client in results_list:
		print(client"[ip]" + "\t\t" + client["mac"])
# >> route -n to check ip of router
# /24 to check the whole subnet (0 to 254)
options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

