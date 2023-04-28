import json
import socket
import threading

threads = list()

def thread_func(conn,addr):
    with conn:
        recv = json.loads(conn.recv(1024))
    return recv

if __name__ == '__main__':
    config = json.load(open())
    
    
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((config['ip'],config['port']))
        s.listen()
        
        while True:
            num_min = int(input("numero da cui iniziare la ricerca: "))
            num_max = int(input("ultimo numero della ricerca: "))
            
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=thread_func, args=(conn,addr))
                thread.start()
