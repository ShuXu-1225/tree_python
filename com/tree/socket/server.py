#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import socket
import threading
import time


def tcplink(sock, addr):
    print('connect address is %s, connect port is %s' % addr)  # addr is a tuple include ip and port

    sock.send(b'Welcome')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s, @time= %s' % (data.decode('utf-8'), time.time())).encode('utf-8'))
    sock.close()
    print('connection %s : %s is closed' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 9000))  # 绑定监听
s.listen(10)  # 启动监听

print('waiting for connections...')

while True:
    sock, addr = s.accept()  # 接收连接请求
    t = threading.Thread(target=tcplink, args=(sock, addr))  # 启动线程处理
    t.start()
