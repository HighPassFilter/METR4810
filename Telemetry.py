
import time
import numpy as np
import adafruit_bno055
from busio import I2C
from board import SDA, SCL

# Note: The interface for the telemetry class should be the same even if we're using the same sensor
class Telemetry():
    def __init__(self):
        # Setup the IMU sensor
        i2c = I2C(SCL, SDA)
        self.sensor = adafruit_bno055.BNO055_I2C(i2c)

    def getLinearAcceleration:
        return self.sensor.linear_acceleration # Do we need raw acceleration or linear acceleration for the final demo?
    
    def getOrientation:
        return self.sensor.euler


