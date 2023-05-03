import json
import socket

HOST = "127.0.0.1" 
PORT = 65432 


def get_primes(lower, upper):
    numbers = set(range(upper, lower, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, upper+1, p)))
    return primes
    
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = json.loads(s.recv(1024))
    s.sendall(findPrimi(data["min"], data["max"]))
