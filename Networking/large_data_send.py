"""
Handling large data transfers over sockets requires managing data in chunks, as there is
usually a limit to the amount of data that can be sent or received at once. When transferring
large files or large amounts of data, it’s best to break the data into smaller segments and
send each segment sequentially. Both the sender and receiver should keep track of how
much data has been transferred to ensure all data is received.
"""

import socket


def send_large_file(client_socket, file_path):
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print('Server listening on port 12345')

conn, addr = server_socket.accept()
print('Connected to', addr)

send_large_file(conn, 'large_file.txt')

