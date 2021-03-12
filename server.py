import socket
import logging

# Data logger setup
logging.basicConfig(filename='example.log', level=logging.WARNING)

storedValue = "Yo, What's up?"
HOST = ''  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply

def dataTransfer(conn):
    while True:
        # Loop that sends/receive data until told not to.
        data = conn.recv(1024)
        data = data.decode('utf-8')
        
        # Split the data such that  you separate from the rest of the data
        dataMessage = data.split(" ", 1)
        command = dataMessage[0]

        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client has left us <:")
            break
        elif command == 'KILL':
            print("Server shutting down..")
        else:
            reply = 'Unknown Command'
        
        # Send the reply back to the Client
        conn.sendall(str.encode(reply))
        print("Data has been sent")



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created")
    s.bind((HOST, PORT))
    print("Socket bind complete")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)
