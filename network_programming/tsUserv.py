from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = sockfd.recvfrom(BUFSIZ)
    sockfd.sendto('[{}] {}'.format(ctime(), data).encode(), addr)
    print('...received from and returned to:', addr)

sockfd.close()
