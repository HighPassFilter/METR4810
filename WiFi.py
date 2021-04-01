''' This library provides the Robot and Ground Station class with the ability to communicate with each other'''
import logging
import socket
from queue import Queue, Empty
import threading

# Data logger setup
logging.basicConfig(level=logging.WARNING)

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

        except IOError:
            logging.error("Cannot create socket")
        

    def setupAgents(self, socket=None):
        # Make the socket non-blocking
        self.socket.settimeout(1)

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
        try:
            data =  self.listener.queue.get(False)
            return data

        except Exception:
            return ""

    def closeConnection(self):
        # Issue the command to shutdown agents
        self.listener.isShutDown = 1
        self.sender.isShutDown = 1

        # Wait for agents to shutdown
        self.listener.join()
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
            return dataType + ":" + str(temperature) + "," + str(orientation) + "," + str(acceleration) + "," + str(pressure)
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
        if dataType == "Sensor":
            data = data.split(",")

            # Ensure that data is in float format
            for i in range(len(data)):
                data[i] = float(data[i])

            return data
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
        msg = ""
        temp = ""
        bytesReceived = 0
        fragmented = 0
        frag_protocol = 0
        print("Listener here")
        while self.isShutDown == 0:

            try:
                # Receive data out via the socket
                data = self.socket.recv(4096)
                data = data.decode('UTF-8')
                
                # Check how many lines of messages have been sent
                lines = data.split(";")
                bytesReceived += len(lines)

                # Send the data to device
                for data in lines:
                    if fragmented == 0:
                        packet = data.split("_")
                        print(packet)
                        # Remove empty packet
                        if '' in packet:
                            pass
                        else:
                            # Check for data fragmentation
                            if len(packet) == 2:
                                msg = packet[1]
                                
                                # Check for data fragmentation
                                if int(packet[0]) != len(packet[1]):
                                    # Look for the next line and combine it with the current packet
                                    fragmented = 1
                                else:
                                    # Sent the message to the device
                                    self.queue.put(msg)
                            else:
                                temp = packet[0]
                                frag_protocol = 1
                                fragmented = 1

                    # Handle fragmentation
                    else:
                        if frag_protocol == 1:
                            # Second element will contain our message
                            msg = packet[1]
                            frag_protocol = 0
                            
                        else:
                            # Combine data fragments
                            msg += data
                            
                        self.queue.put(msg)
                        fragmented = 0

            except socket.timeout:
                pass
            except Exception as e:
                # Report any errors and exit
                print(e)
                self.isShutDown = 1

        print("Listener shutting down")

class Sender(Agent):
    def __init__(self, conn):
        super().__init__(conn)

        # Start listening
        self.start()

    def run(self):
        data = ""
        print("Sender here")
        while self.isShutDown == 0:

            try:
                # Wait for data from 
                data = self.queue.get()

                # Add length of message and delimitter
                data = str(len(data)) + "_" + data + ";"

                # Send the data out via the socket
                self.socket.sendall(str.encode(data))
            except Empty:
                pass
            except Exception as e:
                # Report any errors and exit
                print(e)
                self.isShutDown = 1

        print("Sender shutting down")




        
