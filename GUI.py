import matplotlib.pyplot as plt
import matplotlib.animation as animation
from threading import Thread
from queue import Queue
import time

# Setup the graph GUI
# create a figure with two subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2)

# intialize two line objects (one in each axes)
acc_x_line, = ax1.plot([], [], color='r')
acc_y_line, = ax1.plot([], [], color='b')
acc_z_line, = ax1.plot([], [], color='g')
ax1.set_title('Linear acceleration (m/s^2)')
yaw_line, = ax2.plot([], [], color='r')
pitch_line, = ax2.plot([], [], color='b')
roll_line, = ax2.plot([], [], color='g')
ax2.set_title('Orientation (degrees)')
temp_line, = ax3.plot([], [], color='tab:orange')
ax3.set_title('Temperature (degree Celsius)')
pres_line, = ax4.plot([], [], color = 'tab:cyan')
ax4.set_title('Pressure (hPa)')
line = [acc_x_line, acc_y_line, acc_z_line, yaw_line, pitch_line, roll_line, temp_line, pres_line]

# the same axes initalizations as before (just now we do it for both of them)
ax1.set_ylim(-10, 10)
ax2.set_ylim(-180, 360)
ax3.set_ylim(0, 50)
ax4.set_ylim(900, 1200)

for ax in [ax1, ax2, ax3, ax4]:
    ax.set_xlim(0, 10)

# initialize the data arrays 
xdata, acc_x_data, acc_y_data, acc_z_data, yaw_data, pitch_data, roll_data, temp_data, pres_data = [], [], [], [], [], [], [], [], []
max_y = 20
class UserInterface():
    def __init__(self, pipe):
       
        self.main_pipe = pipe

    def startGraph(self, groundStation):
        ani = animation.FuncAnimation(fig, run, fargs=(self.main_pipe,) ,interval=1, repeat=False, blit=True)
        plt.show()

def run(frame, pipe):
    data = ""
    global xdata, acc_x_data, acc_y_data, acc_z_data, yaw_data, pitch_data, roll_data, temp_data, pres_data, max_y
    while data == "":
        # make sure that data is not empty

        while pipe.poll() == 0:
            pass
        data = pipe.recv()
    
    # update the data
    xdata.append(data[0])

    # Reset the data after 20 seconds
    resetAxis = 0
    if data[0] == max_y:
        xdata, acc_x_data, acc_y_data, acc_z_data, yaw_data, pitch_data, roll_data, temp_data, pres_data = [], [], [], [], [], [], [], [], []
        resetAxis = 1
        max_y = data[0] + 20
    try:
        acc_x_data.append(data[1])
        acc_y_data.append(data[2])
        acc_z_data.append(data[3])
        yaw_data.append(data[4])
        pitch_data.append(data[5])
        roll_data.append(data[6])
        temp_data.append(data[7])
        pres_data.append(data[8])
    except Exception:
        print(data)
        print("Error in receiving packets")


    # axis limits checking. Same as before, just for both axes
    for ax in [ax1, ax2, ax3, ax4]:
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()
        if data[0] >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
        
        if resetAxis == 1:
            ax.set_xlim(data[0], data[0]+10)

    # update the data of both line objects
    line[0].set_data(xdata, acc_x_data)
    line[1].set_data(xdata, acc_y_data)
    line[2].set_data(xdata, acc_z_data)
    line[3].set_data(xdata, yaw_data)
    line[4].set_data(xdata, pitch_data)
    line[5].set_data(xdata, roll_data)
    line[6].set_data(xdata, temp_data)
    line[7].set_data(xdata, pres_data)

    return line
