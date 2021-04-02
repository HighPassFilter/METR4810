import serial
import time

port = serial.Serial('/dev/ttyAMA0', baudrate=int(115200))

port.write("#\r\n".encode())
time.sleep(.500)
port.write("save\r\n".encode())
