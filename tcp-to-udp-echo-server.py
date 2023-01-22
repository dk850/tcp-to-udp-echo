# Note this only works for small packets
import socket
import sys
from time import sleep

HOST = "127.0.0.1"
PORT = 5555

# Create TCP listening socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print("TCP: Listening on:", str(HOST)+":"+str(PORT))
        break
    except:
        SLEEP_TIME=5
        print("Failed to connect. Sleeping for", str(SLEEP_TIME))
        sleep(SLEEP_TIME)


# TCP listener to constantly wait for connections
while True:
    try:  # hang here until connection established
        client_socket, address = server_socket.accept()  # blocking
    
    # Close the socket if the server is stopped
    except KeyboardInterrupt:  
        print("\nClosing server socket")
        server_socket.close()
        sys.exit()


    # Process incoming packet
    print("New connection established from:", str(address[0])+":"+str(address[1]))
    request = client_socket.recv(1024)  # recieve data

    print("Recieved:", request.decode("utf-8"))  # process

    client_socket.send(b"TCP: Server recieved")  # respond to client
    client_socket.close()


    # Echo incoming data to UDP
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = (b"UDP CLIENT REPEAT: "+request)
    udp_client.sendto(message, (HOST, PORT))

    print()




# Code for multiple packets
"""
buffer = b''  # empty bytestream
while True:
    recieved_data = client_socket.recv(4096)
    if recieved_data:
        buffer += recieved_data
        # print(len(buffer))
    else:
        break  # no more data to buffer
    
    # Process buffer
    # use sendall method to echo it all to udp
"""