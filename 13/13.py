from ipaddress import *

k = 0

net = ip_network("204.152.228.160/255.255.255.224")

for ip in net:
    if f"{ip:b}".count("1") <= f"{ip:b}".count("0"):
        k += 1

print(k)
