#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 9999))

while True:
    data, addr = s.recvfrom(1024)
    s.sendto(b'Hello -> %s' % data, addr)
