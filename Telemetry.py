
import time
import numpy as np
import adafruit_bno055
import adafruit_bmp280
from busio import I2C
from board import SDA, SCL

# Note: The interface for the telemetry class should be the same even if we're using the same sensor
class Telemetry():
    def __init__(self):
        
        i2c = I2C(SCL, SDA)

        # Setup the IMU sensor
        self.bno055 = adafruit_bno055.BNO055_I2C(i2c)

        # Setup the temp + pressure sensor
        self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)

    def getLinearAcceleration(self):
        return self.bno055.linear_acceleration # Do we need raw acceleration or linear acceleration for the final demo?
    
    def getOrientation(self):
        return self.bno055.euler

    def getTemperature(self):
        return bmp280.temperature

    def getPressure(self):
        return bmp280.pressure


