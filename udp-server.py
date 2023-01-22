import socket
import sys

HOST = "127.0.0.1"
PORT = 5555

# Bind UDP socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((HOST, PORT))
print("UDP: Bound to:", str(HOST)+":"+str(PORT))


# Constantly listen and recieve packets
while True:
    try:  # hang here until data Received from socket
        data, client = client_socket.recvfrom(1024)  # blocking
        print("Received:", data.decode("utf-8"))


    # Close the socket if the server is stopped
    except KeyboardInterrupt:
        print("\nClosing socket")
        client_socket.close()
        sys.exit()
