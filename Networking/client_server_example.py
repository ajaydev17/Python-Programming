"""
To create a client-server application in Python, use the socket library, where the server listens
on a specific port, and the client connects to that port. The server accepts the connection,
enabling data transfer. Both client and server should close the connection once data
transmission is complete.
"""

# In server.py

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()

print("Server is listening for incoming connections")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")
conn.send(b'Hello, client!')
conn.close()


# In client.py

import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))
data = client_socket.recv(1024)
print(data.decode())
client_socket.close()
