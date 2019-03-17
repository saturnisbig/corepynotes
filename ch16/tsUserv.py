#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from socket import *
from time import ctime

HOST = ''
PORT = 21566
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from and returned to :', addr

udpSerSock.close()
