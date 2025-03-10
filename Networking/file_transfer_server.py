"""
A file transfer server and client can be implemented using sockets by reading and sending
file data in chunks. The server listens for a client connection, then sends file data. The client
receives and writes the data to a file.
"""

# In server.py

import socket

def send_file(server_socket, file_path):
    with open(file_path, 'rb') as file:
        while chunk := file.read(1024):
            server_socket.sendall(chunk)
    print("File sent successfully.")


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen()
conn, addr = server_socket.accept()
send_file(conn, 'file.txt')
conn.close()


# In client.py

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

with open('received_file.txt', 'wb') as file:
    while chunk := client_socket.recv(1024):
        file.write(chunk)
print("File received successfully")
client_socket.close()

