#**********************************#
#********simple port scanner******#
#**********************************#

from socket import *

s = socket(AF_INET, SOCK_STREAM)
ports = []
n = '1'
serv_list = {21 : "ftp", 22 : "ssh", 23 : "telnet", 25 : "smtp", 80 : "http"}
print("-------------------------------------------------------------")
host = input("Enter the ip address: ")

while (n != '0'):
    n = input("Enter the port (or \"0\" to start the scan): ")
    if (n != '0'):
        ports.append(n)
print("-------------------------------------------------------------") 

def scanner(port):
    if (s.connect_ex((host, port)) == 0):
        print(('Port ' + str(port) + ' is \033[32m open\033[0;0m'))
			
    else:
        print(('Port ' + str(port) + ' is \033[31mclosed\033[0;0m'))
			
    if port in serv_list:
        print("" + serv_list[port] + "\n")

print("\n\nStarting to scan " + host + "\n")

for port in ports:
    scanner(int(port))
