
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

            # Set the BNO055 to IMUPlus Mode
            self.bno055.mode = adafruit_bno055.IMUPLUS_MODE

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
        for i in range(100):
            if self.bno055_isPresent:
                try:
                    output = self.bno055.linear_acceleration
                    if output[0] != None:
                        return output
                except:
                    continue
        print("Sensor read failed")
        return [0,0,0]
    
    def getOrientation(self):
        for i in range(100):
            if self.bno055_isPresent:
                try:
                    output = self.bno055.euler
                    if output[0] != None:
                        return output
                except:
                    continue
        print("Sensor read failed")
        return [0,0,0]

    def getGravity(self):
        for i in range(100):
            if self.bno055_isPresent:
                try:
                    output = self.bno055.gravity
                    if output[0] != None:
                        return output
                except:
                    continue
        print("Sensor read failed")
        return [0,0,0]

    def getTemperature(self):
        for i in range(100):
            if self.bmp280_isPresent:
                try:
                    output = self.bmp280.temperature
                    if output != None:
                        return output
                except:
                    continue
        print("Sensor read failed")
        return 0
    

    def getPressure(self):
        for i in range(100):
            if self.bmp280_isPresent:
                try:
                    output = self.bmp280.pressure
                    if output != None:
                        return output
                except:
                    continue
        print("Sensor read failed")
        return 0



