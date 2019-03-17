#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from socket import *

REMOTE_HOST = '66.112.209.81'
PORT = 21566
BUFSIZE = 1024
ADDR = (REMOTE_HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data
udpCliSock.close()
