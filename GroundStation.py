# Telemetry libraries
from WiFi import Client

# Threading libraries
from queue import Queue
from threading import Thread
from multiprocessing import Process, Pipe
class GroundStation():
    def __init__(self, host):
        # Initialise class methods
        self.releaseFlag = 0
        self.isShutDown = 0
        self.main_pipe, self.tele_pipe = Pipe()

        # Setup new process
        self.process = Process(target=telemetryProcess, args=(self))
        self.process.start()

    def shutDown(self):
        self.client.closeConnection()
        self.isShutDown = 1
        self.process.join()

    def command(self, option):
        if option == 1:
            # Abort
            print("Abort!")
            self.client.sendData("abort")
            self.shutDown()

        elif option == 2:
            # Release
            print("Release!")
            self.client.sendData("release")

        elif option == 3:
            # Shutdown
            print("Shutting system down")
            self.client.sendData("shutdown")
            self.shutDown()

            # Plot the data

    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)

def telemetryProcess(groundStation):
    try:
        while groundStation.isShutDown == 0:
            # Stage 1: Setup
            # ----------------------------------------------------
            # Setup user listener
            
            # Wait for IP address from user listener

            # Setup client connection to robot
            self.client = Client(host)

            # Wait for release command from user listener

            # Stage 2: Descent
            # ----------------------------------------------------
            # Check for user inputs
            
            # 
            

    except Exception as e:
        print(e)


def controller():
    if keyboard.is_pressed("1") and keyboard.is_pressed("="):
        print("Please enter your command: ")
        return 1
    if keyboard.is_pressed("2") and keyboard.is_pressed("="):
        print("Please enter your command: ")
        return 2
    if keyboard.is_pressed("3") and keyboard.is_pressed("="):
        print("Please enter your command: ")
        return 3
    return 0


def commsUnit():
    while True:


