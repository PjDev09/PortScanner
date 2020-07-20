#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Arguements")    
    print("Syntax- python3 nmap.py <IP>")
    sys.exit()

# Add Banner ;D
print("-" * 50)
print("Scanning Target " + target)
print("Time Started: " +str(datetime.now()))
print("-" * 50)

try:
    for port in range(0,500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.5)
        result = s.connect_ex((target , port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close
except KeyboardInterrupt:
    print("\nExiting Program")           
    sys.exit()
except socket.gaierror:
    print("Hostname not found")    
    sys.exit()
except socket.error:
    Print("Couldn't connect to server")    
    sys.exit()
