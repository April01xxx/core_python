import socket
import sys

"""
简易socket客户端，接受命令行参数并发送给服务端。
"""
HOST, PORT = 'localhost', 21567
data = ' '.join(sys.argv[1:])

# Create a socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + '\n', 'utf-8'))

    # Receive data from the server and shut down
    received = str(sock.recv(1024), 'utf-8')


print('Send:    {}'.format(data))
print('Received:{}'.format(received))
