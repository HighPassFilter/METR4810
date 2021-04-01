import serial

port = serial.Serial('/dev/ttyAMA0', baudrate=int(100000),
                            parity=serial.PARITY_EVEN,
                            stopbits=serial.STOPBITS_TWO)
data = bytearray(25)

print(len(data))

for byte in range(len(data)):
    data[byte] = 0xFF

print(data)

port.write(bytes([data]))
