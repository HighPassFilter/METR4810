
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
        try:
            # Setup the IMU sensor
            self.bno055 = adafruit_bno055.BNO055_I2C(i2c)
            self.bno055_isPresent = True

        except Exception:
            self.bno055_isPresent = False
        
        try:
            # Setup the temp + pressure sensor
            self.bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address = 0x76)
            self.bmp280_isPresent = True
        except Exception:
            # Only IMU connected over I2C
            self.bmp280_isPresent = False

    def getLinearAcceleration(self):
        if self.bno055_isPresent:
            return self.bno055.linear_acceleration # Do we need raw acceleration or linear acceleration for the final demo?
        else:
            return [0, 0, 0]
    
    def getOrientation(self):
        if self.bno055_isPresent:
            return self.bno055.euler
        else:
            return [0, 0, 0]

    def getTemperature(self):
        if self.bmp280_isPresent:
            return self.bmp280.temperature
        else:
            return 18

    def getPressure(self):
        if self.bmp280_isPresent:
            return self.bmp280.pressure
        else:
            return 1021.05



