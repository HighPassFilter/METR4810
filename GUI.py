import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread
from queue import Queue
import time

# Setup the graph GUI
# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2,1)

# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line = [line1, line2]

# the same axes initalizations as before (just now we do it for both of them)
for ax in [ax1, ax2]:
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 5)
    ax.grid()

# initialize the data arrays 
xdata, y1data, y2data = [], [], []
class UserInterface():
    def __init__(self, pipe):
       
        self.main_pipe = pipe

         # Setup terminal for receiving user inputs
        self.terminal = UserInput(self.main_pipe)
        self.terminal.start()

    def startGraph(self, groundStation):
        #while True:
        #    print(self.main_pipe.poll())
        #    time.sleep(0.5)
        ani = animation.FuncAnimation(fig, run, fargs=(self.main_pipe,) ,interval=1, repeat=False)
        plt.show()

def run(frame, pipe):
    data = ""
    while data == "":
        # make sure that data is not empty

        while pipe.poll() == 0:
            pass
        data = pipe.recv()
    
    # update the data
    xdata.append(data[0])
    y1data.append(data[1])
    y2data.append(data[2])

    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2]:
        xmin, xmax = ax.get_xlim()
        if data[0] >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()

    # update the data of both line objects
    line[0].set_data(xdata, y1data)
    line[1].set_data(xdata, y2data)

    return line

# This class controls the states of the user interface
class UserInput(Thread):
    # Requirements:
    # 1. A way to communicate with the groundstation -> Setup the process of the groundStation (pipe)
    def __init__(self, pipe):
        self.main_pipe = pipe
        Thread.__init__(self)

    def run(self):
        host = "192.168.137.208" #input("Please enter the robot's host ip address: ")
        
        # Return host
        self.main_pipe.send(host)
        #print(self.main_pipe.recv())
        while True:
            option = input("Please enter your command: ")
            # Return command
            self.main_pipe.send(int(option))
            if int(option) == 4:
                break