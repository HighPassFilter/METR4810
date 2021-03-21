# Telemetry libraries
from WiFi import Client



# Threading libraries
from queue import Queue
from threading import Thread
class GroundStation():
    def __init__(self):
        # Initialise class methods
        self.releaseFlag = 0
        # Setup user interface
        self.user = UserInterface()

        # Begin the user interface and retrieve host information
        self.user.start()
        host = self.user.queue.get()

        # Setup client connection to robot
        self.client = Client(host)

        # Request user for release command
        option = self.user.queue.get()
        while int(option) != 2:
            print("Please press 2 to release the robot")
            option = self.user.queue.get()
        
        self.command(option)

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

        elif option == 3:
            # Shutdown
            print("Shutting system down")
            self.client.sendData("shutdown")
            self.shutDown()

            # Plot the data

    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)

    def gen_wrapper(self):
        while True:
            data = self.receiveRobotData()
            yield data

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
    

def run(data):
    data = groundStation.re
    # update the data
    xdata.append(data[0])
    y1data.append(data[1])
    y2data.append(data[2])

    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2]:
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)

    return line

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



