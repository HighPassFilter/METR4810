#Testing for adding frequent looping to state machine for interrupt capability

from time import sleep
import time
import sys, select
  
class StateMachine():
    CONNECT = 7
    RESET_SERVO = 1
    ATTACH_SERVO = 2
    ARM = 3
    DISARM = 4
    DESCEND = 5
    ABORT = 0
    SHUTDOWN = 6

    state_options = [[ATTACH_SERVO, SHUTDOWN],                                     # Connect
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

    def close_servo(self):
        print("Setting servo to close position")
        # Code to move servo slowly to closed position
        for i in range(10, 1500):
            # Update the channel
            print(i)
            sleep(0.01)

    def change_state(self):
        while True:
            #Get input if any
            Timeout = 0.1
            end_time = time.time() + Timeout
            while time.time() < end_time:
                res = input('What is your input: ')
                try:
                    self.current_state = res
                except SomeException:
                    print('There was an error, try again.')
                else:
                    break
            #self.current_state = input("Please provide command input or h for help: ")
            # process = connecting -> connected -> reset_servo -> attach_servo -> arm_motors -> Descend -> Landing
            if self.current_state == str(self.RESET_SERVO):
                print(self.current_state + " Reset Servo")
            elif self.current_state == str(self.ATTACH_SERVO):
                print(self.current_state + " Attach Servo")
                self.close_servo()
            elif self.current_state == str(self.ARM):
                print(self.current_state + " ARM")
            elif self.current_state == str(self.DISARM):
                print(self.current_state + " Disarm")
            elif self.current_state == str(self.ABORT):
                print(self.current_state + " ABORT")
            elif self.current_state == str(self.DESCEND):
                print(self.current_state + " Descend")
            elif self.current_state == str(self.SHUTDOWN):
                print(self.current_state + " Shutdown")
            elif self.current_state == "h":
                self.option_string_builder()

    def option_string_builder(self):
        msg = ""
        for option in self.state_options_helper:
             msg += option[0] + "\n"

        msg += ":"
        print(msg)
    

if __name__ == "__main__":
    machine = StateMachine()
    machine.change_state()

