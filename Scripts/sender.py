#SENDER SCRIPT FOR THE CLIENT FOR THE PROJECT OF THE CLASS AER

from re import T
from socket import *
from pathlib import Path
import os

""" 
Menu options
"""
menu = {
    1: 'List files on Server',
    2: 'Send File to Server',
    3: 'Exit'
}

""" 
function that prints the menu
"""
def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])

""" 
function that lists the files on the server
"""
def listfiles():
    s = socket(AF_INET6,SOCK_DGRAM)         #socket udp ipv6
    host = "2001:0690:2280:822::1"          #IP of the server
    port = 36363                            #port used 
    buf = 1024                              #buffer size
    addr = (host,port)                      #tuple with the IP and the port

    print("Ask for list from", host)
    s.connect(addr)                         #connect the socket
    s.send('list'.encode('utf-8'))          #send list as a string
    print("Waiting for response", host)

    data,addr = s.recvfrom(buf)             #receive response 
    print(data)                             #print the response- list of files in the server
    s.close()

""" 
function to that sends the files 
"""
def sendfile():

    #essential parameters
    s = socket(AF_INET6,SOCK_DGRAM)         #socket udp ipv6
    host = "2001:0690:2280:822::1"          #IP of the server
    port = 36363                            #port used 
    buf = 1024                              #buffer size
    addr = (host,port)                      #tuple with the IP and the port
    path = "/home/core/Desktop/Clientes/"   #caminho para os ficheiros

    print("Send file to", host)     #print for clarity   

    file_name= str(input("Choose the file you want to send: \n"))  #user input
    final_path= path + file_name            #concat of the path + the file name 
    final_path_updated = Path(final_path)   #final path used for verification

    if(final_path_updated.is_file()):              #verifies if the file exists in the path

        print("File Found:", file_name)
        s.sendto(file_name.encode('utf-8'),addr)   #sends the file name 
        f=open(file_name,"rb")                     #abrir o file
        data = f.read(buf)                         #ler o file
        
        while (data):                       #while there is data                       
            if(s.sendto(data,addr)):        #enviar o file
                data = f.read(buf)          #read the buffer
                print ("Sending ...\n")
                break
            else:
                print ("Error")
                break

        s.close()   #close socket
        f.close()   #close file
    else:
        print("File not found:", file_name)


"""
Main function 
"""
if __name__=='__main__':
    while(True):
        print("\nApp Menu:\n")
        print_menu()
        option= ''
        try:
            option = int(input('Enter your choice:'))
        except:
            print('Wrong input. Please enter a valid choice:')
        if option==1:
            listfiles()
        elif option==2:
            sendfile()
        elif option==3:
            exit()
        else:
            print('Invalid Option! Please choose a valid one')