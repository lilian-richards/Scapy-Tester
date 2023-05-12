from scapy.all import *

source_ip = # Enter the sender's IP address
end_port = # Enter the final port number

def sniff_ports(source_ip):
  ports = []
  def packet_callback(pkt):
    if IPv6 in pkt and pkt[IPv6].src == source_ip:
      if pkt[IPv6].dport == end_port:
        filename = # Chosen filename
        f = open(filename, "w")
        for i in ports:
          f.write(str(i) + "\n")
        f.close()
        exit(1)
      else:
        ports.append((pkt[IPv6].src, pkt[IPv6].sport, pkt[IPv6].dport))
  sniff(prn = packet_callback)
ports = sniff_ports(source_ip)
