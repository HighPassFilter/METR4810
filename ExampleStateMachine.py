# from WiFi import Server
# import sys
# import time
# import datetime
# import numpy as np
# import pandas as pd
# from Telemetry import Telemetry
# from StateMachine import States
# from PiSBUS.SBUS import Controller

class StateMachine():
    CONNECTING = 1
    RESET_SERVO = 2
    ATTACH_SERVO = 3
    ARM = 4
    DISARM = 5
    DESCEND = 6
    ABORT = 0
    SHUTDOWN = 7

    # def __init__(self):
    #     self.state = 0
    
    def connect(self):
        print("connecting")
        # Code to connect to computer ready to send sensor data and connect to flight controller
        # Should also print if connection fails/retry connection
        print("connected")
    
    def open_servo(self):
        print("Setting servo to open position")
        # code to move servo to open position
    
    def close_servo(self):
        print("Setting servo to close position")
        # Code to move servo slowly to closed position
    
    def arm_motors(self):
        print("Arming...")
        # code to set thrust to zero then arm motors
    
    def disarm_motors(self):
        print("Disarming...")
        # code to disarm motors then set thrust to zero

    def descend(self):
        print("Beginning descent")
        # this section will slowly power motors up to required thrust, release the servo and drop
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
    
    def shutdown(self):
        print("Shutting down")
        # code to shut down the pi after disarming motors
    
    def new_state(self):
        # process = connecting -> connected -> reset_servo -> attach_servo -> arm_motors -> Descend -> Landing
        while True:
            state = input("Please input the state you would like to go in or type h for help: ")
            if state == str(self.CONNECTING):
                self.connect()
            elif state == str(self.RESET_SERVO):
                self.open_servo()
            elif state == str(self.ATTACH_SERVO):
                self.close_servo()
            elif state == str(self.ARM):
                self.arm_motors()
            elif state == str(self.DISARM):
                self.disarm_motors()
            elif state == str(self.ABORT):
                self.abort()
            elif state == str(self.DESCEND):
                self.descend()
            elif state == str(self.SHUTDOWN):
                self.shutdown()
            elif state == "h":
                print("Press 1 to connect to computer\nPress 2 to open the servo\nPress 3 to close the servo\nPress 4 to arm motors\nPress 5 to disarm motors\nPress 6 to descend\nPress 7 to abort\nPress 0 to shutdown")

if __name__ == "__main__":
    machine = StateMachine()
    machine.new_state()
