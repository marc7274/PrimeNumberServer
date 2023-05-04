import json
import socket

HOST = "127.0.0.1" 
PORT = 65432 


def findPrimi(lower, upper):
    primes = list()
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes  
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = json.loads(s.recv(1024).decode('utf-8'))
    s.sendall(json.dumps(findPrimi(data["min"], data["max"])).encode('utf-8'))
