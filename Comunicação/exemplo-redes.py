
import socket

hostName  = "google.com"
ipAddress = socket.gethostbyname(hostName)
conecction_info = socket.getaddrinfo(hostName,"http")
print("IP address of the host name {} is: {}".format(hostName, ipAddress))
print(conecction_info)