
import socket

HOST = "127.0.0.1"
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Message: ")
    if message == "exit":
        break

    client.sendto(message.encode(), (HOST, PORT))
    response, addr = client.recvfrom(1024)
    print(f"Server: {response.decode()}")

client.close()
