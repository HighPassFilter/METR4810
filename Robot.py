from WiFi import Server
import sys
import numpy as np



class Robot():
    def __init__(self):
        # Flag setup
        self.abortFlag = 0
        self.deployFlag = 0
        self.touchdownFlag = 0

        # Setup server
        self.server = Server()

        # Setup navigation

        # Setup pilot
        

        # Setup sensors

        

    def receiveData(self):
        try:
            message = self.server.receiveData()
            #print(message)
            if message == "abort":
                self.abort()
            if message == "release":
                self.release()
            if message == "shutdown":
                self.shutDown()

            return message
        except:
            pass

    def sendData(self, dataType, data):
        data = self.server.packData(dataType, data)
        print(data)
        #server.sendData(data)

        

    def shutDown(self):
        # TODO: Shut everything down
        print("Robot shutting down")
        #sys.exit()
        #self.server.closeConnection()

    def release(self):
        # TODO: Communicate with pilot to release the clamp
        print("Robot received release command!")

        # Start descending
        self.deployFlag = 1
        
        

    def abort(self):
        # TODO: Turn off the thrusters, camera, sensors 
        print("Robot received abort command!")
        self.abortFlag = 1

    def start(self):

        while self.deployFlag == 0:
            # Keep listening for commands
            self.receiveData()

        print("Robot starting to descent")
        # Generate dummy data
        gen = data_gen()

        while self.touchdownFlag == 0:
            # Listen to command from computer
            
            self.receiveData()
            
            # Abort if the abort command is given
            if self.abortFlag == 1:
                break
                print("Robot aborted")


            # Start collecting data from sensors
            (t, y1, y2) = next(gen)

            # Start sending robot data to computer
            self.sendData("Sensor", [t, y1, y2, 1])

        # Perform navigation computations?

        # Send navigation output to pilot?

        # 

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


