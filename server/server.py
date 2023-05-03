#Versione aplha 0.0
import json
import socket
import threading

class threadList():
    def __init__(self):
        self._list = list()
        self._lock = threading.Lock()

    def append(self, value):
        with self._lock:
            self._list.append(value)

    def extend(self, values: list):
        with self._lock:
            self._list.extend(values)

    def getList(self):
        return self._list


def thread_func(conn:socket.socket, addr, num_min, num_max):
    with conn:
        conn.sendall(json.dumps({"min":num_min,"num_max":num_max}))
        recv = conn.recv(1024)
    prime_nums.extend(json.loads(recv))
        

threads = list()
prime_nums = threadList()        
                
if __name__ == '__main__':
    last_number_given = 0
    config = json.load(open())

    num_min = int(input("primo numero da calcolare: "))
    num_max = int(input("ultimo numero da calcolare: "))
    last_number_given = num_min - 1

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((config['ip'], config['port']))
        s.listen()

        while last_number_given<num_max:
            conn,addr = s.accept()
            if num_max-last_number_given>=config['range']:
                threads.append(threading.Thread(target=thread_func,args=(conn,addr,last_number_given+1,last_number_given+config['range'])))
            else:
                threads.append(threading.Thread(target=thread_func,args=(conn,addr,last_number_given+1,last_number_given+(num_max-last_number_given))))
            last_number_given+=num_max-last_number_given
        for t in threads:
            t.join()
            
        json.dump(json.loads(json.dumps(prime_nums.getList,open(config['path-to-output']+"result.json","w"))))