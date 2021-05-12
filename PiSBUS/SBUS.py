#-------------------------------------------------------------------------------
# Author: Connor Raggatt    
# Date:   1/04/2021
#-------------------------------------------------------------------------------
# Code is based on source from PiPilot by Lukasz Janyst <lukasz@jany.st>
#
# PiPilot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PiPilot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PiPilot.  If not, see <http://www.gnu.org/licenses/>.
#-------------------------------------------------------------------------------

import readline
import serial
import ctypes
import time
from threading import Thread
from queue import Queue


#-------------------------------------------------------------------------------
def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


#-------------------------------------------------------------------------------
class SBUSEncoder:
    #---------------------------------------------------------------------------
    def __init__(self):
        self.channels = [1024] * 16

    #---------------------------------------------------------------------------
    def set_channel(self, channel, data):
        self.channels[channel] = data & 0x07ff

    #---------------------------------------------------------------------------
    def get_data(self):
        #-----------------------------------------------------------------------
        # Create the header
        #-----------------------------------------------------------------------
        data = bytearray(25)
        data[0] = 0x0f # start byte

        #-----------------------------------------------------------------------
        # Encode channels
        #-----------------------------------------------------------------------
        current_byte = 1
        available_bits  = 8
        for ch in self.channels:
            ch &= 0x7ff
            remaining_bits = 11
            while remaining_bits:
                mask = bit_not(0xffff >> available_bits << available_bits, 16)
                enc = (ch & mask) << (8 - available_bits)
                data[current_byte] |= enc

                encoded_bits = 0
                if remaining_bits < available_bits:
                    encoded_bits = remaining_bits
                else:
                    encoded_bits = available_bits

                remaining_bits -= encoded_bits
                available_bits -= encoded_bits
                ch >>= encoded_bits

                if available_bits == 0:
                    current_byte += 1
                    available_bits = 8

        #-----------------------------------------------------------------------
        # Ignore the flags and end byte
        #-----------------------------------------------------------------------
        data[23] = 0
        data[24] = 0

        return data

#-------------------------------------------------------------------------------
class Controller(Thread):

    #---------------------------------------------------------------------------
    def __init__(self):
        self.queue = Queue()
        self.duration = 0.007
        self.isShutDown = False
        Thread.__init__(self)
        self.start()
        
    #---------------------------------------------------------------------------
    def send_sbus_msg(self):
        #-----------------------------------------------------------------------
        # Get the data to send
        #-----------------------------------------------------------------------
        data = self.encoder.get_data()
        print(len(data), data)
        # Send it line by line so that serial doesn't overlap
        #-----------------------------------------------------------------------
        self.port.write(data)

    #---------------------------------------------------------------------------
    def update_channel(self, channel, value):
        # scale = value + 100.
        # scale /= 200
        # self.encoder.set_channel(channel, int(scale * 2047))
        self.queue.put("channel;"+str(channel) + ";" + str(value))

    def shutdown(self):
        self.queue.put("shutdown;0;0")

    def run(self):
        #-----------------------------------------------------------------------
        # Configuration
        #-----------------------------------------------------------------------
        tty_file = '/dev/ttyAMA0'
        #tty_file = '/dev/ttyS0'

        #-----------------------------------------------------------------------
        # Set up the SBUS encoder and open the serial port
        #-----------------------------------------------------------------------
        self.encoder = SBUSEncoder()
        self.port = serial.Serial(tty_file, baudrate=int(100000),
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_TWO)

        #-----------------------------------------------------------------------
        # Continuously send SBUS message to the flight controller
        #-----------------------------------------------------------------------
        start = time.time() # Seconds
        while not self.isShutDown:
            # Check for queue messages
            if not self.queue.empty():
                # Get data from the queue
                data = self.queue.get_nowait()
                data = data.split(";")
                if data[0] == "shutdown":
                    self.isShutDown = True
                else:
                    print("Channel updated")
                    channel = int(data[1])
                    value = int(data[2])
                # Update the channels
                self.encoder.set_channel(channel,value)
            
            # Check if time has passed
            if time.time() - start > self.duration:
                # Send the SBUS message
                self.send_sbus_msg()
                start = time.time()
controller = Controller()
controller.update_channel(10,2000)
controller.shutdown()
# while True:
#     for channel in range(0,16):
#         for i in range(600,1500):
#             controller.update_channel(channel,i)
#             controller.send_sbus_msg()
#             time.sleep(0.001)


# for byte in range(len(data)-1):
#     print(data[byte])
#     controller.port.write(bytes([data[byte]]))
#     while(controller.port.out_waiting != 0):
#         pass

# while 1:
#     controller.port.write(b'\xFF')
#     #controller.send_sbus_msg()
#     time.sleep(0.07)
