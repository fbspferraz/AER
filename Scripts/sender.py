#test sending file over udp sender 

from socket import *
import sys

s = socket(AF_INET6,SOCK_DGRAM)  #socket udp ipv4
host = "2001:0690:2280:822::1"               #var para entrada de arg na cmd 
port = 36363                     #porta utilizada
buf = 1024                       #buffer size
addr = (host,port)               #tuplo com o ip e port

file_name=sys.argv[1]            #var que vai receber o nome do file via arg na cmd

s.sendto(file_name.encode('utf-8'),addr)    #enviar o nome do file

f=open(file_name,"rb")           #abrir o file
data = f.read(buf)              #ler o file
while (data):
    if(s.sendto(data,addr)):    #enviar o file
        print ("sending ...")
        data = f.read(buf) 

s.close()   #fechar socket
f.close()   #fechar file