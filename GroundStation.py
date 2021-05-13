# Telemetry libraries
from WiFi import Client

# Threading libraries
from StateMachine import States
from queue import Queue
from threading import Thread
from multiprocessing import Process, Pipe
import pandas as pd
import datetime

class GroundStation():
    def __init__(self, pipe, experiment=False):
        # Initialise class methods
        self.experiment = experiment
        self.state = States()
        self.client = ""
        self.tele_pipe = pipe
        self.guiListener = ""
        self.sensorData = [[], [], [], [], [], [], []]

        # Setup new process
        self.process = Process(target=telemetryProcess, args=(self,))
        self.process.start()

    def shutDown(self):
        self.client.closeConnection()
        self.guiListener.shutDownGUIListener()

    def command(self, option, available):
        # Verify that the available options was selected
        if available.count(option) == 1:
            if option == 1:
                # Lock in
                self.state.lockIn = 1
                self.client.sendData("lockin")
                print("Servo lock in")

            elif option == 2:
                # Release
                print("Release!")
                self.client.sendData("release")
                self.state.descent = 1

                # Plot the data
            elif option == 3:
                # Abort
                print("Abort!")
                self.client.sendData("abort")
                self.state.abort = 1

            elif option == 4:
                # Shutdown
                print("Shutting system down")
                self.client.sendData("shutdown")
                self.state.shutDown = 1

            elif option == 5:
                print("Resetting the system")
                self.client.sendData("reset")
                self.state.reset = 1
            elif option == 6:
                print("Arming the system")
                self.client.sendData("ready")
                self.state.ready = 1
        else:
            print("Invalid command!")

    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)

    def stateSetup(self):
        print("Lock in: 1, Shutdown: 4, Reset: 5, Restart setup: r,:")

        while self.state.notSetup():
            # Handle option and commands from user
            self.optionHandler(self.state.setupOptions)       

        # Move to ready state
        self.stateReady()

    def stateReady(self):
        print("Abort: 3, Shutdown: 4, Reset: 5, Arm: 6, Restart setup: r,:")
        while self.state.notDescent():
            self.optionHandler(self.state.readyOptions)

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
        print("Wait for touchdown to restart, Abort: 3, Shutdown: 4, Reset: 5, :")

        while self.state.toDescent(): 
            self.optionHandler(self.state.descentOptions)
            # Receive data from the robot
            
            data = self.receiveRobotData()
            
            if data != "":
                # Timestamp the data
                self.sensorData[0].append(data[0])
                # Store the non empty data
                self.sensorData[1].append(data[1])
                self.sensorData[2].append(data[2])
                self.sensorData[3].append(data[3])
                self.sensorData[4].append(data[4])
                self.sensorData[5].append(data[5])
                self.sensorData[6].append(data[6])

            # Send the data to the GUI
            self.tele_pipe.send(data)

        # Save the sensor data as a csv file
        #print(self.sensorData)
        df = pd.DataFrame(self.sensorData)
        df = df.T
        df.columns = ["TS", "Lin_Acc_X", "Lin_Acc_Y", "Lin_Acc_Z", "Yaw", "Pitch", "Roll"]
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
        # Command the Atmega128 to abort
        print("Wait for touchdown to restart, Shutdown: 4, Reset: 5, :")
        while self.state.toAbort():
            # Do we want to continue plotting data here?
            # Check for touchdown status being received
            self.optionHandler(self.state.abortOptions)

        # Go to the next state
        self.state.abort = 0
        if self.state.shutDown == 1:
            self.shutDown()

        elif self.state.reset == 1:
            self.reset()

        elif self.state.touchdown == 1:
            self.stateReady()

    def reset(self):
        # System in reset
        self.shutDown()
        # Try to reconnect to the client
        

    def setupPipe(self, pipe):
        self.terminal.main_pipe = pipe

    def optionHandler(self, available):
        try:
            option =  int(self.guiListener.getInput(False))
            self.command(option, available)
        except Exception as e:
            pass

def telemetryProcess(groundStation):
    try:
        # Stage 1: Setup
        # ----------------------------------------------------
        # Setup user listener
        
        groundStation.guiListener = GUIListener(groundStation.tele_pipe)
        groundStation.guiListener.start()
        
        # Wait for IP address from user listener
        host = groundStation.guiListener.getInput()
        
        # Setup client connection to robot
        groundStation.client = Client(host)
        groundStation.state.connected = 1

        # Begin the state machine
        groundStation.stateSetup()

    except Exception as e:
        print(e)

class GUIListener(Thread):
    def __init__(self, pipe):
        self.tele_pipe = pipe
        self.shutDown = 0
        self.queue = Queue()
        Thread.__init__(self)

    def run(self):
        # Wait for inputs from the GUI
        while self.shutDown == 0: # To change condition to shutdown
            if self.tele_pipe.poll():
                msg = self.tele_pipe.recv()
                # Put item in queue upon receiving the item
                self.queue.put(msg)

    def getInput(self, blocking=True):
        msg = ""
        if blocking:
            msg = self.queue.get()
        else:
            try:
                msg = self.queue.get_nowait()
            except Exception as e:
                pass
        return msg
       
    def shutDownGUIListener(self):
        print("GUI Listener shutting down..")
        self.shutDown = 1

