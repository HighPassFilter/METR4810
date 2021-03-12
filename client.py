import socket
import logging

# Details about server
host = "192.168.0.3" # To be obtained dynamically?
port = 65432

# Create INET socket and stream data 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    while True:
        command = input("Enter your command: ")

        if command == 'EXIT':
            # Send exit request to the other end
            s.send(str.encode(command))
            break
        else:
            s.send(str.encode(command))
            reply = s.recv(1024)
            print(reply.decode("utf-8"))





