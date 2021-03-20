''' This library provides the Robot and Ground Station class with the ability to communicate with each other'''

import socket
from queue import Queue
import logging
import threading

# Data logger setup
logging.basicConfig(filename='example.log', level=logging.WARNING)

class WiFi():
    def __init__(self, identity, host, port=7777): # Tested
        # Class methods
        self.host = host
        self.port = port
        self.listener = None
        self.sender = None
        self.identity = identity

        # Initialise socket
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Socket created")
            #s.connect((self.host, self.port))
            #print("HI")
        except IOError:
            logging.error("Cannot create socket")
        

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
        self.sender.queue.put(data)

    def receiveData(self):
<<<<<<< HEAD
        try:
            data =  self.listener.queue.get(False)
            return data

        except Exception:
            return ""
=======
        return self.listener.queue.get(False)
>>>>>>> f4d9b8cc60bcd20b662b822151db12450fc8308c

    def closeConnection(self):
        # Issue the command to shutdown agents
        self.listener.isShutDown = 1
        self.sender.isShutDown = 1

        # Wait for agents to shutdown
        self.sender.join()

        # Close the socket
        self.socket.close()
        logging.info("Closing connection on %s", self.identity)

class Server(WiFi):
    def __init__(self, port=7777): # Tested
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

    @staticmethod
    def packData(dataType, data): 
        if dataType == "Sensor":
            temperature = data[0]
            orientation = data[1]
            acceleration = data[2]
            pressure = data[3]
            return dataType + ":" + str(temperature) + "," + str(orientation) + "," + str(acceleration) + "," + str(pressure)+ ";"
        else:
            return dataType + ":" + data

class Client(WiFi):
    def __init__(self, host, port=7777): # Tested
        super().__init__("client", host, port)
        # Connect to the Server
        self.socket.connect((self.host, self.port))

        # Setup Listener and Sender
        super().setupAgents()

    @staticmethod
    def unpackData(data):
        if data == "":
            return data
        dataType, data = data.split(":")
        if dataType == "sensor":
            return data.split(",")
        else:
            return data

class Agent(threading.Thread):
    def __init__(self, socket):
        self.socket = socket
        self.queue = Queue()
        self.isShutDown = 0
        threading.Thread.__init__(self)

    # Main loop for listening agent
    def run(self):
        print("Looking for the wrong agent!")
        
class Listener(Agent):
    def __init__(self, conn):
        super().__init__(conn)
        # Start listening
        self.start()

    def run(self):
        data = ""
        print("Listener here")
        while True:
            if self.isShutDown == 0:
                try:
                    # Receive data out via the socket
                    data = self.socket.recv(1024)
                    data = data.decode('UTF-8')
                    print(data)
                    # Send the data to the server
                    self.queue.put(data)
                except IOError:
                    print("Connection lost")
                except Exception:
                    pass

            else:
                print("Listener shutting down")
                break

class Sender(Agent):
    def __init__(self, conn):
        super().__init__(conn)

        # Start listening
        self.start()

    def run(self):
        data = ""
        print("Sender here")
        while True:
            if self.isShutDown == 0:
                try:
                    # Wait for data from 
                    data = self.queue.get(False)

                    # Send the data out via the socket
                    self.socket.sendall(str.encode(data))
                except IOError:
                    print("Connection lost")
                except Exception:
                    pass
            else:
                print("Sender shutting down")
                break




        
