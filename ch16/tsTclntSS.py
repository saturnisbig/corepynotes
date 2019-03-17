#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from socket import *

REMOTE_HOST = '66.112.209.81'
PORT = 21567
BUFSIZE = 1024
ADDR = (REMOTE_HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
