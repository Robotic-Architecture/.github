
import socket

HOST = "0.0.0.0"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print(f"UDP server listening on {PORT}")

while True:
    data, addr = server.recvfrom(1024)

    message = data.decode()
    print(f"Received from {addr}: {message}")

    server.sendto("Message received".encode(), addr)
