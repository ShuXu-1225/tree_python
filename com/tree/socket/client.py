#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import socket
import time
import threading


def startSock():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 9000))

    print(s.recv(1024).decode('utf-8'))

    for data in [b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))

    # time.sleep(1)
    s.send(b'exit')
    s.close()


for i in range(1000):
    t = threading.Thread(target=startSock)
    # time.sleep(1)
    t.start()
    # t.join()
