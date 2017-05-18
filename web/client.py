#!/usr/bin/env python
#coding=utf-8

import socket

ip_port = ('127.0.0.1',9090)
c = socket.socket()
c.connect(ip_port)
c.sendall(bytes('hello server,my name client'))

server_reply = c.recv(1024)

print(str(server_reply))
c.close()