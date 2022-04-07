#test sending file over udp sender 

from re import T
from socket import *
from pathlib import Path
import os

menu = {
    1: 'List files on Server',
    2: 'Send File to Server',
    3: 'Exit'
}

def print_menu():
    for key in menu.keys():
        print(key, '--', menu[key])


def listfiles():
    path = "/home/core/Desktop/Servidor/"

    obj = os.scandir(path)
    
    # List all files and directories in the specified path
    print("\nFiles  in '%s':" % path)
    for entry in obj :
        if entry.is_dir():
            print("Found Directory: %s;" % entry.name)
        elif entry.is_file():
            print("Found File: %s;" % entry.name)
        else:
            print("Nothing found on '%s'", path)


def sendfile():
    s = socket(AF_INET6,SOCK_DGRAM)         #socket udp ipv6
    host = "2001:0690:2280:822::1"          #var para entrada de arg na cmd 
    port = 36363                            #porta utilizada
    buf = 1024                              #buffer size
    addr = (host,port)                      #tuplo com o ip e port
    path = "/home/core/Desktop/Clientes/"   #caminho para os ficheiros
    print("Send file to", host)      
    file_name= str(input("Choose the file you want to send: \n"))  #user input
    final_path= path + file_name
    final_path_updated = Path(final_path)
    if(final_path_updated.is_file()):                       #verifica se encontra o ficheiro
        print("File Found:", file_name)
        s.sendto(file_name.encode('utf-8'),addr)            #enviar o nome do file

        f=open(file_name,"rb")                              #abrir o file
        data = f.read(buf)                                  #ler o file
        while (data):
            if(s.sendto(data,addr)):                        #enviar o file
                data = f.read(buf) 
                print ("Sending ...\n")
                break
            else:
                print ("Error")
                break

        s.close()                                            #fechar socket
        f.close()                                            #fechar file
    else:
        print("File not found:", file_name)


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