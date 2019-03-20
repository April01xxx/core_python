from socket import *

HOST = '127.0.0.1'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZ = 1024

fd = socket(AF_INET, SOCK_STREAM)
fd.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    # python3 发送byte类型数据
    fd.send(bytes(data, 'utf-8'))
    data = fd.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

fd.close()
