
from ast import While
from importlib.metadata import files
from socket import *
import os
from time import time
import glob
from typing import List
import json
import threading
import sys

host="2001:0690:2280:0822::1"
port = 36363
FORMAT='utf-8'
addr =((host,port))
buf = 1024

s = socket(AF_INET6,SOCK_DGRAM)


def handle_client(data,addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    message = data.decode(FORMAT)
    
    if (message == 'list'):
        list()

    elif(message == 'file-size'):
        file_size()
    
    else:
        sendfile(message,data)

def list():
    path = "/home/core/Desktop/Sv/"
    obj = os.listdir(path)
    print("[FILE] Inside dir:",obj)
    obje = " ".join(obj)
    obj_encoded=obje.encode(FORMAT)
    s.sendto(obj_encoded,addr)

def file_size():
    file_dict = {}
    path = "/home/core/Desktop/Sv/"
    obj = os.listdir(path)
    for file in obj:
        file_dict[file] = os.path.getsize(os.path.join(path,file))
        file_temp = json.dumps(file_dict)
        file_encode = file_temp.encode(FORMAT)
    s.sendto(file_encode,addr)
    print(file_temp)

def sendfile(message,data):
    data,addr = s.recvfrom(buf)
    #message1 = data.decode('utf-8')
    print("[FILE] Received FileName:", message)
    f=open(message,'wb')
    try:
        while(data):
            #print(data)
            f.write(data)
            s.settimeout(1)
            data,addr = s.recvfrom(buf)
    except timeout:
        f.close()
        #s.close()
        print("[SUCCESSFUL]File Downloaded\n")
    

"""
MAIN FUNCTION
"""

if __name__=='__main__':
    print("[STARTING] Server is starting...")
    s.bind(addr)
    print(f"[LISTENING] Server is listening on {host}:{port}")
    try:
       while(True):
         data,addr = s.recvfrom(buf)
         thread = threading.Thread(target=handle_client(data,addr)).start()
         print(f"[ACTIVE CONNECTIONS] {threading.activeCount()}")
         #thread.join()
         #s.close()
    except timeout as e:
       print(f"[ERROR] - {e}")
       #s.close()
        
