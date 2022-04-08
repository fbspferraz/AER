#RECEIVER SCRIPT FOR THE SERVER FOR THE PROJECT OF THE CLASS AER

#!/usr/bin/env python

from ast import While
from socket import *
import os
from this import d
from time import time

while True:
    host= "2001:0690:2280:0822::1"          #IP of the server
    port = 36363                            #port used 
    s = socket(AF_INET6,SOCK_DGRAM)         #socket udp ipv6
    s.bind((host,port))                     #bind of the socket

    addr = (host,port)                      #tuple with the IP and the port
    buf=1024                                #buffer size

    print ("Waiting for Connection")

    data,addr = s.recvfrom(buf)             #receive data 
    message = data.decode('utf-8')          #put the decode data in another var
    
    if(message == 'list'):      #if the received message is "list"

        path = "/home/core/Desktop/Servidor/"   #path for the directory with the files
        obj = os.listdir(path)                  #put all the file names in a list 
        print("Inside Dir:",obj)                #print the file names
        obj_joined=" ".join(obj)                #use join to turn the list to a string
        obj_encoded=obj_joined.encode("utf-8")  #encode the string with all the file names 
        s.sendto(obj_encoded,addr)              #send the list to the client

    else:       #if the received message isnt "list"                                       

        print("Received File:", data)   #print the file name 
        f=open(data,'wb')               #open/create a file with the name received

        try:
            while(data):                        #while there is data
                f.write(data)                   #write that data to the created file
                s.settimeout(2)                 #timeout 
                data,addr = s.recvfrom(buf)     #put the data from the buffer in the data variable
        except timeout:                         #when done
            f.close()                           #close file
            s.close()                           #close socket
            print("File Downloaded\n")          #print to let the user know its done

