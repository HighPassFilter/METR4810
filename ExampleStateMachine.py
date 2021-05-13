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
    CONNECT = 0
    RESET_SERVO = 1
    ATTACH_SERVO = 2
    ARM = 3
    DISARM = 4
    DESCEND = 5
    ABORT = 6
    SHUTDOWN = 7
    RESET = 8
    current_state = CONNECT

    state_options = [[ATTACH_SERVO, SHUTDOWN, RESET],                                       # Connect
                          [ATTACH_SERVO, SHUTDOWN, RESET],                                  # Open servo
                          [RESET_SERVO, ARM, SHUTDOWN, RESET],                              # Close servo
                          [DISARM, RESET_SERVO, DESCEND, SHUTDOWN, RESET],                  # Arm the motors
                          [ARM, RESET_SERVO, SHUTDOWN, RESET],                              # Disarm the drone
                          [ABORT, SHUTDOWN, RESET],                                         # Descend
                          [SHUTDOWN, RESET]]                                                # Abort   

    state_options_helper = [[],
                            ["Open servo: 1"],
                            ["Close servo: 2"],
                            ["Arm the motors: 3"],
                            ["Disarm the motors: 4"],
                            ["Descend: 5"],
                            ["Abort: 6"],
                            ["Shutdown: 7"],
                            ["Abort: 8"]]

    # def __init__(self):
    #     self.
    
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
    
    def shutdown(self):
        print("Shutting down")
        # code to shut down the pi after disarming motors

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
        
    def option_string_builder(self):
        msg = ""
        for option in self.state_options[self.current_state]:
             msg += self.state_options_helper[option] + ", "

        msg += ":"
        print(msg)

if __name__ == "__main__":
    machine = StateMachine()
    machine.connect()
