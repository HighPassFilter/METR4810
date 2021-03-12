''' This library provides the Robot and Ground Station class with the ability to communicate with each other'''

import socket
from queue import Queue
import logging
import threading

# Data logger setup
logging.basicConfig(filename='example.log', level=logging.WARNING)

class WiFi():
    def __init__(self, identity, host, port=7777):
        # Class methods
        self.host = host
        self.port = port
        self.listener = None
        self.sender = None
        self.identity = identity

        # Initialise socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Socket created")
            self.socket = s

    def setupAgents(self, socket=None):
        # Assign socket connection
        if socket != None:
            conn = socket
        else:
            conn = self.socket

        # Setup a thread for Listener and Sender
        self.listener = Listener(conn)
        self.sender = Sender(conn)

    def sendData(self, data):
        self.listener.queue.put(data)

    def receiveData(self, data):
        self.listener.queue.get(data)

class Server(WiFi):
    def __init__(self, port=7777):
        # Initialise class attributes
        super().__init__("server", "", port)

        # Bind the socket
        self.socket.bind((self.host, port))
        print("Socket bind complete")

        # Listen for a connection
        self.socket.listen()

        # Accept the connection from client
        conn, addr = self.socket.accept()
        logging.info("Server connected to %s", addr)

        # Setup Listener and Sender 
        super().setupAgents(conn)

    def packData(self, dataType, data):
        if dataType == "Sensor":
            temperature = data[0]
            orientation = data[1]
            acceleration = data[2]
            pressure = data[3]
            return dataType + ":" + str(temperature) + "," + str(orientation) + "," + str(acceleration) + "," + str(pressure)
        else:
            return dataType + ":" + data

class Client(WiFi):
    def __init__(self, host, port):
        super().__init__("client", host, port)

        # Connect to the Server
        self.socket.connect(self.host, self.port)

        # Setup Listener and Sender
        super().setupAgents()

    def unpackData(self, data):
        dataType, data = data.split(":")
        if dataType == "sensor":
            return data.split(",")
        else:
            return data

class Agent(threading.Thread):
    def __init__(self, socket):
        self.socket = socket
        self.queue = Queue()
        threading.Thread.__init__(self)

    def run(self):
        while True:
            # Wait for data from server
            data = self.queue.get()

            # Send the data out via the socket
            self.socket.sendall(data)

            #data = self.socket.recv(1024)
            #print(data)
        # logging.info("")
        
class Listener(Agent):
    def __init__(self, conn):
        super().__init__(conn)

class Sender(Agent):
    def __init__(self, conn):
        super().__init__(conn)




        
