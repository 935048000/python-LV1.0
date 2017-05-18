#!/use/bin/env python
#coding=utf-8

import socket
ip_port=('127.0.0.1',9090)
web = socket.socket()
web.bind(ip_port)
web.listen(2)
print('the is a python socket connect test ....')
while True:
    conn,addr = web.accept()
    data = conn.recv(1024)
    print(data)
    conn.send(bytes('<h1>hello python socket client! </h1>'))
    conn.close()
    