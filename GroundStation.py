# Telemetry libraries
from WiFi import Client

# Threading libraries
import keyboard
import cv2

# Camera library
from Vision import Vision 
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
        self.vision = Vision()

        # Setup new process
        # self.process = Process(target=telemetryProcess, args=(self,))
        # self.process.start()
        telemetryProcess(self)
    
    def collect_data(self):
        # Main loop for collecting telemetry data from the robot
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

            # Get centre of image
            centre_data = self.vision.get_centre()
            cv2.imshow("image", centre_data[0])
            self.client.sendData(self.client.packData("Vision", (centre_data[1], centre_data[2], centre_data[3])))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    def receiveRobotData(self):
        data = self.client.receiveData()
        return self.client.unpackData(data)