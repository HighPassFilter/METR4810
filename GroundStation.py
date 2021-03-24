# Telemetry libraries
from WiFi import Client

# Threading libraries
from StateMachine import States
from queue import Queue
from threading import Thread
from multiprocessing import Process, Pipe
class GroundStation():
    def __init__(self, pipe):
        # Initialise class methods
        self.state = States()
        self.client = ""
        self.tele_pipe = pipe
        self.guiListener = ""

        # Setup new process
        self.process = Process(target=telemetryProcess, args=(self,))
        self.process.start()

    def shutDown(self):
        self.client.closeConnection()
        self.process.join()

    def command(self, option, available):
        # Verify that the available options was selected
        if available.count(option) == 1:
            if option == 1:
                # Lock in
                self.state.lockIn = 1
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

    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)

    def stateHardSetup(self):
        print("Please press 1 to lock in the servo or 4 to shutdown: ")

        while self.state.notReady():
            # Handle option and commands from user
            self.optionHandler(self.state.setupOptions)        

        # Move to ready state
        self.stateReady()

    def stateReady(self):
        print("Please press 2 to release the robot, 3 to abort or 4 to shutdown: ")
        while self.state.notDescent():
            self.optionHandler(self.state.readyOptions)

        # Move to descent state
        if self.state.shutDown == 1:
            return
        elif self.state.descent == 1:
            self.stateDescent()
        elif self.state.abortOptions == 1:
            self.stateAbort()

    def stateDescent(self):
        print("Please press 3 to abort, 4 to shutdown or wait for robot to touchdown to restart: ")

        while self.state.toDescent(): 
            self.optionHandler(self.state.descentOptions)
            # Keep sending data received from the robot
            self.tele_pipe.send(self.receiveRobotData())
            
        # Move to ready state # Need to properly trigger switch as well
        self.state.descent = 0
        self.stateReady()

    def stateAbort(self):
        # Command the Atmega128 to abort
        print("Please press 4 to shutdown or wait for robot to touchdown to restart: ")
        while self.toStopAbort():
            # Do we want to continue plotting data here?
            # Check for touchdown status being received
            self.optionHandler(self.state.abortOptions)

        # Move to Hardware Setup State
        self.state.lockIn = 0
        self.state.abort = 0
        self.stateHardSetup()

    def stateReset(self):
        # System in reset
        # Try to reconnect to the client
        pass

    def stateShutDown(self):
        # Close all processes and threads
        pass

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
        groundStation.stateHardSetup()

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
       
        

