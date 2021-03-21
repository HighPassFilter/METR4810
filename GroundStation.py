import keyboard
from WiFi import Client
import matplotlib
from queue import Queue
from threading import Thread


class GroundStation():
    def __init__(self):
        # Setup user interface
        self.user = UserInterface()

        # Begin the user interface and retrieve host information
        self.user.start()
        host = self.user.queue.get()

        # Setup client connection to robot
        self.client = Client(host)

    def shutDown(self):
        self.client.closeConnection()

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
            self.trackRobot()

        elif option == 3:
            # Shutdown
            print("Shutting system down")
            self.client.sendData("shutdown")
            self.shutDown()
    
    def trackRobot(self):
        while True:
            # Check controller inputs
            try:
                option = self.user.queue.get(False)
                self.command(option)

            except IOError:
                # No commands given
                pass

            if option == 1 or option == 3:
                break

            # Receive data from robot
            data = self.receiveRobotData()

            # Plot the data

    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)

class UserInterface(Thread):
    def __init__(self):
        self.queue = Queue()
        Thread.__init__(self)

    def run(self):
        host = "192.168.137.184"#input("Please enter the robot's host ip address: ")
        
        # Return host 
        self.queue.put(host)

        while True:
            option = input("Please enter your command: ")

            # Return command
            self.queue.put(int(option))
            if int(option) == 3:
                break



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



