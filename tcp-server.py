import socket
import sys
from time import sleep

HOST = "127.0.0.1"
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        server_socket.bind((HOST, PORT))
        break
    except:
        SLEEP_TIME=5
        print("Failed to connect. Sleeping for", str(SLEEP_TIME))
        sleep(SLEEP_TIME)
    
server_socket.listen(1)
print("TCP: Listening on:", str(HOST)+":"+str(PORT))

while True:
    try:
        client_socket, address = server_socket.accept()
    except KeyboardInterrupt:
        print("\nClosing server socket")
        server_socket.close()
        sys.exit()

    print("New connection established from:", str(address[0])+":"+str(address[1]))

    request = client_socket.recv(1024)
    print("Received:", request.decode("utf-8"))

    client_socket.send(b"TCP: Server response")
    client_socket.close()
    print()
