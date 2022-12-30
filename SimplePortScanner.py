import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM
s.settimeout(6)

host = input("Enter IP address to scan: ")
port = int(input("Enter the port to scan: ")

def portScan(port)
  if s.connect_ex((host, port))
    print("Port closed")
  else:
    print("Port open")
   
portScan(port)
