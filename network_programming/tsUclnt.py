from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

sockfd = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    sockfd.sendto(data.encode(), ADDR)
    data, ADDR = sockfd.recvfrom(BUFSIZ)
    if not data:
        break

    print(data.decode())

sockfd.close()
