import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    print(data.decode("utf-8"))
    
    # if len(data.decode("utf-8")) == 0: 
    #     print(f'Fechando conexão client')
    #     s.close()

    time.sleep(2)