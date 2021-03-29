#!/usr/bin/env python
import time
import serial

class TelemetryPacket:
	accel_x = None #0x24
	accel_y = None #0x25
	accel_z = None #0x26
	vert_speed = None #0x30
	alt_bp = None #0x10
	alt_ap = None #0x21
	temp = None #0x02
	rpm = None #0x03
	volt = None #0x06
	voltage_amp_bp = None #0x3A
	voltage_amp_ap = None #0x3B
	current = None #0x28
	fuel_level = None #0x04

	def process_packet(self, packet):
		count = 1
		print(int((len(packet)-1)/4))

		for i in range(int((len(packet)-1)/4)):
			data_id = packet[1+i*4]
			data_h = packet[2+i*4]
			data_l = packet[3+i*4]
			data = 256*data_h + data_l

			if(data_id == 0x24):
				self.accel_x = data
			if(data_id == 0x25):
				self.accel_y = data
			if(data_id == 0x26):
				self.accel_z = data
			if(data_id == 0x30):
				self.vert_speed = data
			if(data_id == 0x10):
				self.alt_bp = data
			if(data_id == 0x21):
				self.alt_bp = data
			if(data_id == 0x02):
				self.temp = data
			if(data_id == 0x03):
				self.rpm = data
			if(data_id == 0x06):
				self.volt = data
			if(data_id == 0x3A):
				self.voltage_amp_bp = data
			if(data_id == 0x3B):
				self.voltage_amp_ap = data
			if(data_id == 0x28):
				self.current = data
			if(data_id == 0x04):
				self.fuel_level = data
	
	def print_data(self):
		print("Accel: ", self.accel_x, self.accel_y, self.accel_z)
		print("Alt  : ", self.alt_bp, self.alt_ap)
		print("Vert : ", self.vert_speed)
		print("Temp : ", self.temp)


ser = serial.Serial(
        port='/dev/serial0',
        baudrate = int(9600*1.57),
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        #xonxoff = True,
        timeout=0
)

count = 0
ser.reset_input_buffer()
result_list = []
telem = TelemetryPacket

while 0:
	x = None
	time.sleep(10/9600)
	try:
		x=ser.read()
#		print(x, count)
	except:
		break

	if(x != None and x != b''):
		x = int.from_bytes(x,"little")
		count = 0
		result_list.append(x)
	else:
		count += 1

	if(count == 5):
		#print(result_list)
		telem.process_packet(telem,result_list)
		telem.print_data(telem)
		
		result_list = []
		ser.reset_input_buffer()
		print("")

# sample_packet = [94, 36, 0, 0, 94, 37, 0, 0, 94, 38, 0, 0, 94, 48, 0, 0, 94, 16, 0, 0, 94, 33, 34, 0, 94, 2, 0, 0, 94, 3, 0, 0, 94, 6, 0, 0, 94, 58, 0, 0, 94, 59, 1, 0, 94, 40, 0, 0, 94, 4, 0, 0, 94]
# telem = TelemetryPacket
# telem.process_packet(telem, sample_packet)
# telem.print_data(telem)






