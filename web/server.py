#!/usr/bin/env python
#coding=utf-8

import socket

ip_port = ('127.0.0.1',9090)
s = socket.socket()
s.bind(ip_port)
s.listen(2)
while True:
    print('server waiting......')
    conn,addr = s.accept()
    client_data = conn.recv(1024)
    print(str(client_data))
    conn.sendall(bytes('my name server...'))
    conn.close()