from WiFi import Server
import time
import numpy as np
from Telemetry import Telemetry
from PiSBUS.SBUS import Controller
import sys, select
import RPi.GPIO as GPIO

class StateMachine():
    RESET = 7
    RESET_SERVO = 1
    ATTACH_SERVO = 2
    ARM = 3
    DISARM = 4
    DESCEND = 5
    ABORT = 0
    SHUTDOWN = 6

    current_state = 0
    previous_state = 0

    centre_pos = 1025
    RESET_PIN = 22

    #Variables for interuptable functions
    servo_pos = 10

    state_options = [[ATTACH_SERVO, SHUTDOWN],                                       # Connect
                          [ATTACH_SERVO, SHUTDOWN],                                  # Open servo
                          [RESET_SERVO, ARM, SHUTDOWN],                              # Close servo
                          [DISARM, RESET_SERVO, DESCEND, SHUTDOWN],                  # Arm the motors
                          [ARM, RESET_SERVO, SHUTDOWN],                              # Disarm the drone
                          [ABORT, SHUTDOWN],                                         # Descend
                          [SHUTDOWN]]                                                # Abort   

    state_options_helper = [
                            ["Abort: 0"],
                            ["Open servo: 1"],
                            ["Close servo: 2"],
                            ["Arm the motors: 3"],
                            ["Disarm the motors: 4"],
                            ["Descend: 5"],
                            ["Shutdown: 6"],
                            ["Reset: 7"]]

    def __init__(self):
        self.RELEASE_SERVO_CHANNEL = 7
        self.ARM_CHANNEL = 4
        self.THROTTLE_CHANNEL = 2
        self.PITCH_CHANNEL = 1 # To be changed
        self.ROLL_CHANNEL = 0 # To be changed
        self.server = Server()
        self.controller = Controller()
        self.tele = Telemetry()
        self.data_storage = [[],[],[],[]]
        self.initialOri = self.tele.getOrientation()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.RESET_PIN, GPIO.OUT)
    
    def sendData(self, dataType, data):
        data = self.server.packData(dataType, data)
        #print(data)
        self.server.sendData(data) 
    
    # def connect(self):
    #     print("connecting")
    #     # Code to connect to computer ready to send sensor data and connect to flight controller
    #     # Should also print if connection fails/retry connection
    #     print("connected")
    
    def open_servo(self):
        #One Time Function 
        print("Setting servo to open position")
        # Set the servo to open position
        self.servo_pos = 10
        self.controller.update_channel(self.RELEASE_SERVO_CHANNEL, self.servo_pos)
    
    def close_servo(self):
        #INTERRUPTABLE FUNCTION

        if(self.current_state != self.previous_state):
            print("Setting servo to close position")
        
        # Code to move servo slowly to closed position
        if(self.servo_pos < 1500):
            self.servo_pos = self.servo_pos + 50
            self.controller.update_channel(self.RELEASE_SERVO_CHANNEL, self.servo_pos)
            print("Setting Servo pos: ", self.servo_pos)
    
    def arm_motors(self):
        #One Time Function 
        print("Arming...")
        # Set the throttle to zero
        self.controller.update_channel(self.THROTTLE_CHANNEL, 10)
        # Arm motors
        self.controller.update_channel(self.ARM_CHANNEL, 1300)
    
    def disarm_motors(self):
        #One Time Function 
        if(self.current_state != self.previous_state):
            print("Disarming...")
            # Set the throttle to zero
            self.controller.update_channel(self.THROTTLE_CHANNEL, 10)
            # Disarm motors
            self.controller.update_channel(self.ARM_CHANNEL, 10)
    
    def descend(self):
        #INTERRUPTABLE STATE
        if(self.current_state != self.previous_state):
            print("Beginning descent")
            self.start = time.time()
            self.throttleLevel = 20
            self.open_servo()
        
        #Taking an image and finding target
        # t = time.time()
        # print("Starting Vision iteration")
        #print(self.tele.getOrientation()[1] - self.initialOri[1], self.tele.getOrientation()[2] - self.initialOri[2])
        linAcc = self.tele.getLinearAcceleration()
        ori = self.tele.getOrientation()
        temp = self.tele.getTemperature()
        pres = self.tele.getPressure()
        self.sendData("Sensor", [time.time() - self.start, np.round(linAcc[0], 2), np.round(linAcc[1], 2), np.round(linAcc[2], 2), np.round(ori[0], 2), np.round(ori[1], 2), np.round(ori[2], 2), np.round(temp, 2), np.round(pres, 2)])

        self.controller.update_channel(self.THROTTLE_CHANNEL, self.throttleLevel)
        if self.throttleLevel < 1500: #self.throttleLevel < 2000 and time.time() - self.start >= 0.5
            self.throttleLevel += 200
        else: # abs(self.tele.getOrientation()[1] - self.initialOri[1]) <= 8 and abs(self.tele.getOrientation()[2] - self.initialOri[2]) <= 8
            # If craft is level TODO calibrate levelness values
            # 0.621x + 883
            # print("hit")
            # self.start = time.time()
            centre = self.server.unpackData(self.server.receiveData())
            print(centre)
            if centre[0] != 0:
                self.controller.update_channel(self.PITCH_CHANNEL, self.centre_pos - int(0.5*centre[1]))
                self.controller.update_channel(self.ROLL_CHANNEL, self.centre_pos + int(0.5*centre[0]))
                time.sleep(0.2)
                self.controller.update_channel(self.PITCH_CHANNEL, self.centre_pos)
                self.controller.update_channel(self.ROLL_CHANNEL, self.centre_pos)

        # this section will slowly power motors up to required thrust, release the servo and drop
        # while descend:
        # navigation control will also go in this section
        # data also needs to be sent to the computer
        # This state will also trigger the landing state once the craft is close enough to the ground
        # abort mode must be able to be triggered in this state but I'll add that in later
    
    def landing_approach(self):
        print("Landing")
        # Code to run when the craft is landing, is kind of tba
    
    def abort(self):
        #One time function
        print("ABORT!")
        # Code to disarm the motors and trigger abort mode
        # Disarm motors
        self.disarm_motors()
        self.controller.shutdown()
        
    
    def shutdown(self):
        # Disarm motors
        self.disarm_motors()
        self.controller.shutdown()
        sys.exit(0)

    def reset(self):
        print("Power cycling")
        # Reboot the pi and trigger the power cycle pin
        GPIO.output(self.RESET_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(self.RESET_PIN, 0)
        import subprocess
        subprocess.Popen(['shutdown','-r','now'])


    def change_state(self, new_state):

        self.current_state = new_state
        
        # process = connecting -> connected -> reset_servo -> attach_servo -> arm_motors -> Descend -> Landing

        if self.current_state == str(self.RESET_SERVO) and self.current_state != self.previous_state:
            self.open_servo()
        elif self.current_state == str(self.ATTACH_SERVO):
            self.close_servo()
        elif self.current_state == str(self.ARM) and self.current_state != self.previous_state:
            self.arm_motors()
        elif self.current_state == str(self.DISARM) and self.current_state != self.previous_state:
            self.disarm_motors()
        elif self.current_state == str(self.ABORT) and self.current_state != self.previous_state:
            self.abort()
        elif self.current_state == str(self.DESCEND):
            self.descend()
        elif self.current_state == str(self.SHUTDOWN) and self.current_state != self.previous_state:
            self.shutdown()
        elif self.current_state == str(self.RESET) and self.current_state != self.previous_state:
            self.reset()
        elif self.current_state == "h" and self.current_state != self.previous_state:
            self.option_string_builder()
        
        #If the state has changed, do something about it
        if(self.current_state != self.previous_state):
            #Update the previous state
            self.previous_state = self.current_state
    
    def sendData(self, dataType, data):
        data = self.server.packData(dataType, data)
        #print(data)
        self.server.sendData(data) 
        
    def option_string_builder(self):
        msg = ""
        for option in self.state_options_helper:
            msg += option[0] + "\n"

        msg += ":"
        print(msg)

if __name__ == "__main__":

    machine = StateMachine()
    machine.change_state(0)

    #Always look for user inputs, with timeout of 0.02s (50Hz)
    # This enables aborting during long duration operations
    # However, all functions must be created with the intent on being called repeatedly
    # if they are to run for an extended duration
    while True:
        i, o, e = select.select( [sys.stdin], [], [], 0.02 )

        if (i):
            machine.change_state(sys.stdin.readline().strip())
        else:
            machine.change_state(machine.current_state)