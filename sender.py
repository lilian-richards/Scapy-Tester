from scapy.all import *

sendTo = # receiver's IP address
start = # Starting port
end = # Ending port

for i in range(start, end + 1):
    packet = IP(dst=sendTo)/UDP(sport=i, dport=i)/"Port Scan"
    send(packet)

exit(1)
