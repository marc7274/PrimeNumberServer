import json
import socket
import threading

IP = '0.0.0.0'
PORT = 12345
threads = list()

def thread_func(conn,addr):
    with conn:
        recv = json.loads(conn.recv(1024))
    return recv

if __name__ == '__main__':
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((IP,PORT))
        s.listen()
        
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=thread_func, args=(conn,addr))
            thread.start()
