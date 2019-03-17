#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from socket import *

HOST = 'localhost'
REMOTE_HOST = '66.112.209.81'
PORT = 21567
BUFSIZE = 1024
ADDR = (REMOTE_HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()
