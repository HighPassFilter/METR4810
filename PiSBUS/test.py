data = bytearray(25)

print(len(data))

for byte in range(len(data)):
    data[byte] = 0xFF

print(data)