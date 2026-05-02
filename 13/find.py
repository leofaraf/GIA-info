from ipaddress import *

s = ip_address("217.9.142.131")
m = ip_address("255.255.192.0")

print(f"{s:b}")
print(f"{m:b}")

print()

print(f"{s:b}"[16:16+8])
print(f"{m:b}"[16:16+8])

print(int('10000000', 2))