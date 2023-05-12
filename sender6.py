from scapy.all import *

sendTo = # Listener's IP address
start = # Start Port
end = # End Port

for i in range(start, end + 1):
    packet = IPv6(dst=sendTo)/UDP(sport=i, dport=i)/"Port Scan"
    send(packet)

exit(1)
