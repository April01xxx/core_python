from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
LISTENQ = 5

sockfd = socket(AF_INET, SOCK_STREAM)
sockfd.bind(ADDR)
sockfd.listen(LISTENQ)

while True:
    print('Waiting for connection ...')
    clifd, addr = sockfd.accept()
    print('...Connected from:', addr)

    # 处理客户端请求
    while True:
        data = clifd.recv(BUFSIZ)
        if not data:
            break
        # python3 发送byte类型数据
        clifd.send('[{}] {}'.format(ctime(), data).encode('utf-8'))

    # 关闭客户端套接字
    clifd.close()

# nerver reach here
sockfd.close()
