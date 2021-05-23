# Telemetry libraries
from WiFi import Client

# Threading libraries
from multiprocessing import Process
import keyboard

def telemetryProcess(groundStation):
    try:
        ipAddress = "192.168.43.43"
        # ipAddress = input("Please enter IP address")
        # Setup client connection to robot
        groundStation.client = Client(ipAddress)
        groundStation.collect_data()

    except Exception as e:
        print(e)

class GroundStation():
    def __init__(self, pipe):
        # Initialise class methods
        self.client = ""
        self.tele_pipe = pipe
        self.sensorData = [[], [], [], [], [], [], []]

        # Setup new process
        self.process = Process(target=telemetryProcess, args=(self,))
        self.process.start()
    
    def collect_data(self):
        while True:
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    return  # finishing the loop
            except:
                pass
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
    
    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)