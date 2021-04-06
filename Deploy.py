from piservo import Servo

import time

myservo = Servo(12)

myservo.write(180)
time.sleep(3)
myservo.write(0)
time.sleep(3)
myservo.stop()

class DeploymentServo:
    def __init__(self):
        self.servo = Servo(12)
        # Set initial position

    def parachute(self):
        pass

    def robot(self):
        # Move the servo to release
        pass