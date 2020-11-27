#!/usr/bin/python3
from __future__ import print_function

ips = []
with open("access.log") as f:
    for line in f:
        ips.append(line.split()[0])

print(f"PV is {len(ips)}")
print(f"UV is {len(set(ips))}")
