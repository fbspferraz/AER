#test sending file over udp receiver

#!/usr/bin/env python

from ast import While
from socket import *
import time
from turtle import delay

while True:
    host= "2001:0690:2280:0822::1"          #ip do host
    port = 36363                            #porta utilizada
    s = socket(AF_INET6,SOCK_DGRAM)         #socket udp ipv6
    s.bind((host,port))                     #bind do socket ao ip e port

    addr = (host,port)                      #tuplo do addr
    buf=1024                                #buffer size
    print ("Waiting for Connection")
    data,addr = s.recvfrom(buf)             #receber dados via a socket
    print ("Received File: ",data)          #print do nome do file recebido
    f = open(data,'wb')                     #abrir file recebido

    try:                                    #try para ler dados da socket
        while(data):
            f.write(data)
            s.settimeout(2)
            data,addr = s.recvfrom(buf)
    except timeout:
        f.close()
        s.close()
        print ("File Downloaded \n")