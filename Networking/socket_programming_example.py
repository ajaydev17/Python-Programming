"""
Socket programming in Python allows communication between devices over a network. A
socket is an endpoint in communication between two devices. Python’s socket library
enables developers to establish these connections using TCP (Transmission Control Protocol)
or UDP (User Datagram Protocol). TCP is connection-oriented, providing reliability by
confirming message delivery, while UDP is connectionless, prioritizing speed over reliability.
"""

import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()

print("Server is listening for incoming connections")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)

    client_socket.close()
    print(f"Connection with {client_address} closed")