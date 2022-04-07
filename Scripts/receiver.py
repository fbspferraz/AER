#test sending file over udp receiver

#!/usr/bin/env python

from socket import *
import sys
import select

while True:
    host= "2001:0690:2280:0822::1"    #ip do host
    port = 36363                      #porta utilizada
    s = socket(AF_INET6,SOCK_DGRAM)   #socket udp ipv4
    s.bind((host,port))               #bind do socket ao ip e port

    addr = (host,port)  #tuplo do addr
    buf=1024            #buffer size

    data,addr = s.recvfrom(buf)             #receber dados via a socket
    print ("Received File:",data.strip())   #print do nome do file recebido

    f = open(data.strip(),'wb')             #abrir file recebido
    data,addr = s.recvfrom(buf)

    #try para ler dados da socket 
    try:
        while(data):
            f.write(data)
            s.settimeout(2)
            data,addr = s.recvfrom(buf)
    except timeout:
        f.close()
        s.close()
        print ("File Downloaded")