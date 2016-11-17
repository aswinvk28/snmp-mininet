import sys
import socket
import snmpload

HOST = "mininet"               # Symbolic name meaning all available interfaces
PORT = 8001              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_TCP, socket.IPPROTO_IP)

connection, bind_address = s.accept()

while 1:
    data = connection.recv(1024)
    list = data.split("\t")
    mininetSNMPValues = mininet_snmp_load(list[0], list[1], list[2]) # returns a dictionary
    connection.send(str(mininetSNMPValues))

