#!/bin/python
# -*- coding: utf-8 -*-

import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 10002
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
    echo = raw_input("send data -> ")
    s.send(echo)
    data = s.recv(BUFFER_SIZE)
    print "received data: ", data

s.close()

