#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'A', b'B', b'C']:
    s.sendto(data, (socket.gethostname(), 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
