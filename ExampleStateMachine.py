from WiFi import Server
import time
import numpy as np
from Telemetry import Telemetry
from PiSBUS.SBUS import Controller
import keyboard

class StateMachine():
    CONNECT = 7
    RESET_SERVO = 1
    ATTACH_SERVO = 2
    ARM = 3
    DISARM = 4
    DESCEND = 5
    ABORT = 0
    SHUTDOWN = 6

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
                            ["Shutdown: 6"]]

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
        print("Setting servo to open position")
        # Set the servo to open position
        self.controller.update_channel(self.RELEASE_SERVO_CHANNEL, 10)
    
    def close_servo(self):
        print("Setting servo to close position")
        # Code to move servo slowly to closed position
        for i in range(10, 1500):
            # Update the channel
            self.controller.update_channel(self.RELEASE_SERVO_CHANNEL, i)
            # TODO add in cancelling
            try:
                if keyboard.is_pressed('q'):
                    break
            except:
                pass
    
    def arm_motors(self):
        print("Arming...")
        # Set the throttle to zero
        self.controller.update_channel(self.THROTTLE_CHANNEL, 10)
        # Arm motors
        self.controller.update_channel(self.ARM_CHANNEL, 1300)
    
    def disarm_motors(self):
        print("Disarming...")
        # Set the throttle to zero
        self.controller.update_channel(self.THROTTLE_CHANNEL, 10)
        # Disarm motors
        self.controller.update_channel(self.ARM_CHANNEL, 10)
    
    def descend(self):
        print("Beginning descent")
        # Power up the motors
        for i in range(10, 1501):
            self.controller.update_channel(2, i)
        # Release
        self.open_servo()

        start = time.time()
        prev_print = start
        if True:
            # Descending
            # Abort is possible 
            try:
                if keyboard.is_pressed('q'):
                    self.abort()
            except:
                pass
            # Collect data from sensors
            linAcc = self.tele.getLinearAcceleration()
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
        print("ABORT!")
        # Code to disarm the motors and trigger abort mode
        # Disarm motors
        self.disarm_motors()
    
    def shutdown(self):
        print("Shutting down")
        # Disarm motors
        self.disarm_motors()
        self.controller.shutdown()

    def reset(self):
        print("Power cycling")
        # code to shut down the pi after disarming motors
    
    def new_state(self, next_state):
        change_state = False
        # Check if command given is valid for certain state
        if self.state_options[self.current_state].count(next_state) == 1:
            self.current_state = next_state
            change_state = True
        else:
            print("Invalid command! Please try again.")

        # Provide user with available state options
        self.option_string_builder()
        return change_state

    def change_state(self):
        while True:
            self.current_state = input("Please provide command input or h for help: ")
            # process = connecting -> connected -> reset_servo -> attach_servo -> arm_motors -> Descend -> Landing
            if self.current_state == str(self.RESET_SERVO):
                self.open_servo()
            elif self.current_state == str(self.ATTACH_SERVO):
                self.close_servo()
            elif self.current_state == str(self.ARM):
                self.arm_motors()
            elif self.current_state == str(self.DISARM):
                self.disarm_motors()
            elif self.current_state == str(self.ABORT):
                self.abort()
            elif self.current_state == str(self.DESCEND):
                self.descend()
            elif self.current_state == str(self.SHUTDOWN):
                self.shutdown()
            elif self.current_state == "h":
                self.option_string_builder()
        
    def option_string_builder(self):
        msg = ""
        for option in self.state_options_helper:
             msg += option[0] + "\n"

        msg += ":"
        print(msg)
    
    

# def static_abort():
#     controller = Controller()
#     print("ABORT!")
#     # Set the throttle to zero
#     controller.update_channel(2, 10)
#     # Disarm motors
#     controller.update_channel(4, 10)

if __name__ == "__main__":
    # keyboard.on_press_key("a", static_abort())
    machine = StateMachine()
    machine.change_state()
