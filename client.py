import json
import socket

HOST = "127.0.0.1" 
PORT = 65432 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = json.loads(s.recv(1024))
    s.sendall(findPrimi(data["min"], data["max"]))