from scapy.all import *

def sniff_ports(source_ip):
	ports = []
	def packet_callback(pkt):
		if IP in pkt and pkt[IP].src == source_ip: # filtering only packets from the chosen sender
			if pkt[IP].sport == end_port:
				filename = # Chosen filename for capture
				f = open(filename, "w")
				for i in ports:
					f.write(str(i) + "\n") # writes the captured packet list to the file
				f.close()
				exit(1)
			else:
				ports.append((pkt[IP].src, pkt[IP].sport, pkt[IP].dport)) # adds the packet's IP and ports to list
	sniff(prn = packet_callback)
	exit(1)

source_ip = # Sender's IP
end_port = # Chosen end port

ports = sniff_ports(source_ip)
