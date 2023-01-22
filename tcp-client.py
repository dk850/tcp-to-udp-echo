import socket

HOST = '127.0.0.1'
PORT = 5555

# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Send data over the socket
message = (b"TCP: Client here")  # byte stream
print("Sending :", message.decode("utf-8"))
client_socket.send(message)

# Check for a response
response = client_socket.recv(4096)
print("Received:", response.decode("utf-8"))