import sys
import socket
import time
import os
import os.path
from filehash import FileHash
import datetime
from datetime import date


#Menu that allows the user to choose between the hash application or the port scan application
def program_menu():
    target_ip=port_menu()
    port_scan(target_ip)
	

  

#captures how much time has passed
def run_time():
    timer=time.time()
    return timer


def port_scan(target_ip):
    start_time=run_time()
    try:
    #scanning every single port
        for port in range(1,65535):
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            #set default timeout for the socket in seconds
            socket.setdefaulttimeout(1)

            #setting up the connection for the socket
            result=s.connect_ex((target_ip,port))
            if result==0:
                #this means that the ports are open
                print("[*] Port {} is open".format(port))
                s.close()

#exiting the program
    except KeyboardInterrupt:
        print('\n exiting program')
        sys.close()

    except socket.error:
        print("could not reach host IP")
        sys.close()
    end_time=run_time()

    elapsed_time= (end_time-start_time)

    scan_complete=f'Scan Completed in {elapsed_time:.2f} seconds'

    print(scan_complete)


#menu to enter the target IP
def port_menu():
    print("_"*50)
    #Printing the current Date to ensure the program is running correcctly
    current_time = datetime.datetime.now()
    print("Current date and time: ",current_time)
    print("Welcome to Port Scan!!!")
    #target_ip= str(input("Enter target IP address: "))
    target_ip = '192.168.18.12'
    print("Your IP is :"+target_ip)
    
    print("Scanning the Target IP -> "+target_ip)
    print("_"*50)
    print('\n')
    return target_ip

if __name__=='__main__':
    program_menu()

    
