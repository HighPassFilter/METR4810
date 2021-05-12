from WiFi import Server
import sys
import time
import datetime
import numpy as np
import pandas as pd
from Telemetry import Telemetry
from StateMachine import States
from PiSBUS.SBUS import Controller



class Robot():
    def __init__(self, experiment=False):
        # Flag setup
        self.experiment = experiment
        self.state = States()
        # Setup server
        self.server = Server()

        # Setup navigation

        # Setup pilot
        
        # Setup Flight controller
        self.controller = Controller()

        # Setup sensors
        self.tele = Telemetry()
        self.data_storage = [[],[],[],[]]
    
    def stateReady(self):
        # Obtain flat orientation
        self.oriWorld = self.tele.getOrientation()
        while self.oriWorld[0] == None:
            self.oriWorld = self.tele.getOrientation()

        print("Robot ready for descent")
        while self.state.notDescent():
            # Listen to commands
            self.receiveData()
            
        # Execute commands
        # Control the servo to release the craft

        # Obtain the global frame of reference

        # Go to the next state
        if self.state.shutDown == 1:
            self.shutDown()

        elif self.state.reset == 1:
            self.reset()

        elif self.state.abort == 1:
            self.stateAbort()
            
        elif self.state.descent == 1:
            self.stateDescent()
        
    def stateDescent(self):
        print("Robot in descent mode")
        # Turn on the thrusters?

        # Generate dummy data
        start = time.time()
        prev_print = start

        self.controller.update_channel(4, 1300)

        while self.state.toDescent():
            # Collect data from sensors
            linAcc = self.tele.getLinearAcceleration()

            ori = (0,0,0)
            if self.experiment:
                
                ori = self.tele.getGravity()
            else:
                ori = self.tele.getOrientation()

            temp = self.tele.getTemperature()
            pres = self.tele.getPressure()
            TOF = time.time() - start
            
            if linAcc[0] != None and ori[0] != None:
                # Store inflight acceleration data
                self.data_storage[0].append(TOF)
                self.data_storage[1].append(linAcc[0])
                self.data_storage[2].append(linAcc[1])
                self.data_storage[3].append(linAcc[2])
            
            # Send the data to the ground station (Every 0.2 seconds?)
            if time.time() - prev_print > 0.1:
                if linAcc[0] != None and ori[0] != None and temp != None and pres != None:
                    self.sendData("Sensor", [TOF, np.round(linAcc[0], 2), np.round(linAcc[1], 2), np.round(linAcc[2], 2), np.round(ori[0], 2), np.round(ori[1], 2), np.round(ori[2], 2), np.round(temp, 2), np.round(pres, 2)])
                    prev_print = time.time()

            # Update robot state estimate

            # Check touchdown

            # Process the image

            # Update the flight controller commands            

            # Listen to commands
            self.receiveData()
            
        # Execute commands
        # Save the data (To be removed during actual flight)
        df = pd.DataFrame(self.data_storage)
        df = df.T
        date = datetime.datetime.now()
        filename = "sensor_" + str(date.month) + "_" + str(date.day) + "_" + str(date.hour) + "_" +str(date.minute) + "_" + str(date.second) + ".csv"
        df.to_csv(filename, index=False)
        
        # Go to the next state
        self.state.descent = 0
        if self.state.shutDown == 1:
            self.shutDown()

        elif self.state.reset == 1:
            self.reset()

        elif self.state.abort == 1:
            self.stateAbort()
            
        elif self.state.touchdown == 1:
            self.stateReady()

    def stateAbort(self):
        print("Robot in abort mode")
        # Generate dummy data (to be removed)
        t = 0
        y1 = 0
        y2 = 0
        # Control the servo to unleash the parachute

        self.controller.update_channel(4, 200)

        while self.state.toAbort():
            # Collect data from sensors(?)
            t += 0.05
            y1 += 0.01
            y2 += 0.02

            # Send the data to the ground station (?)
            #self.sendData("Sensor", [np.round(t, 2), np.round(y1, 2), np.round(y2, 2), 1.01])
            # Update the robot state estimate (?)

            # Receive commands
            self.receiveData()

        # Go to the next state
        self.state.abort = 0
        if self.state.shutDown == 1:
            self.shutDown()

        elif self.state.reset == 1:
            self.reset()

        elif self.state.touchdown == 1:
            self.stateReady()
        
    def receiveData(self):
        try:
            message = self.server.receiveData()
            #print(message)
            if message == "abort":
                print("Robot received abort command!")
                self.state.abort = 1
            if message == "release":
                print("Robot received release command!")
                self.state.descent = 1
            if message == "shutdown":
                print("Robot received shutdown command!")
                self.state.shutDown = 1
            if message == "reset":
                print("Robot received reset command!")
                self.state.reset = 1

            #return message
        except:
            pass

    def sendData(self, dataType, data):
        data = self.server.packData(dataType, data)
        #print(data)
        self.server.sendData(data)       

    def shutDown(self):
        # TODO: Shut everything down
        print("Robot shutting down")
        self.controller.shutdown()
        self.server.closeConnection()
    
    def reset(self):
        print("Robot resetting")
        # Shutdown the wifi connection
        self.server.closeConnection()
        # Send the command to the pilot to reset


def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < 1000:
        cnt+=1
        t += 0.05
        y1 = np.sin(2*np.pi*t) * np.exp(-t/10.)
        y2 = np.cos(2*np.pi*t) * np.exp(-t/10.)
        # adapted the data generator to yield both sin and cos
        yield t, y1, y2



# Global variables
data_gen.t = 0


