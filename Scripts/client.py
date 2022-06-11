
from __future__ import print_function
from re import T
from socket import *
from pathlib import Path
import os


menu= {
    1: 'List files on Server',
    2: 'Send Files to Server',
    3: 'File Size',
    4: 'Exit'
}


def print_menu():
    for key in menu.keys():
        print(key,'--',menu[key])

def listfiles():
    s = socket(AF_INET6,SOCK_DGRAM)
    host = "2001:0690:2280:822::1"
    port = 36363
    buf = 1024
    addr = (host,port)

    print("Ask for list from", host)
    s.connect(addr)
    s.send('list'.encode('utf-8'))
    print("Waiting for response",host)
    s.settimeout(60)
    data,addr = s.recvfrom(buf)
    print("Inside Dir: ")
    print(data.decode('utf-8'))
    s.close()

def filesize():
    s = socket(AF_INET6,SOCK_DGRAM)
    host = "2001:0690:2280:822::1"
    port = 36363
    buf = 1024
    addr = (host,port)

    print("Ask for list from", host)
    s.connect(addr)
    s.send('file-size'.encode('utf-8'))
    print("Waiting for response",host)
    data,addr = s.recvfrom(buf)
    print("Inside Dir: ")
    print(data.decode('utf-8'))
    s.close()


def sendfile():
    s = socket(AF_INET6,SOCK_DGRAM)
    host = "2001:0690:2280:822::1"
    port = 36363
    buf = 1024
    addr = (host,port)
    s.connect(addr)
    path = "/home/core/Desktop/Cl/"
    fList=[]
    print("[FILE] Sending file to: ", host)

    file_name=str(input("[FILE] Choose the file you want to send: "))
    final_path = path + file_name
    final_path_updated = Path(final_path)

    if(final_path_updated.is_file()):
        size = os.path.getsize(final_path_updated)

        print("[FILE] File found: ", file_name, "with the size", size)

        with open(final_path, "rb") as f:
            file_name_encoded=file_name.encode('utf-8')
            s.sendto((file_name_encoded), addr)
            while True:
                chunk = f.read(1024)
                if chunk:
                    fList.append(chunk)
                    numBlocks = len(fList)
                    print("[FILE] Number of the chunk being sent: ", numBlocks)
                    s.sendto(chunk,addr)
                else:
                    numBlocks = len(fList)
                    break
        print("[FILE] Total number of chunks: ")
        print(numBlocks)
        s.close()
        f.close()
    else:
        print("[FILE] File not found:", file_name)


if __name__=='__main__':
    while(True):
        print("\nApp Menu:\n")
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a valid choice: ')
        if option == 1:
            listfiles()
        if option == 2:
            sendfile()
        if option == 3:
            filesize()           
        if option == 4:    
            exit()
else:
    print('Invalid Option! Please choose a valid one')       
