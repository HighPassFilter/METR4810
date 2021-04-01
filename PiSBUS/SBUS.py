#-------------------------------------------------------------------------------
# Author: Lukasz Janyst <lukasz@jany.st>
# Date:   06.03.2018
#-------------------------------------------------------------------------------
# This file is part of PiPilot.
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
class Controller:

    #---------------------------------------------------------------------------
    def __init__(self):
        #-----------------------------------------------------------------------
        # Configuration
        #-----------------------------------------------------------------------
        tty_file = '/dev/serial0'

        #-----------------------------------------------------------------------
        # Set up the SBUS encoder and open the serial port
        #-----------------------------------------------------------------------
        self.encoder = SBUSEncoder()
        self.port = serial.Serial(tty_file, baudrate=int(100000*1.57),
                                  parity=serial.PARITY_EVEN,
                                  stopbits=serial.STOPBITS_TWO,
                                  rtscts = True)
    # #---------------------------------------------------------------------------
    # def startService(self):
    #     self.log.info('Starting controller')
    #     self.sbus_loop.start(0.07)

    # #---------------------------------------------------------------------------
    # def stopService(self):
    #     self.log.info('Stopping controller')
    #     self.sbus_loop.stop()

    #---------------------------------------------------------------------------
    def send_sbus_msg(self):
        self.port.write(self.encoder.get_data())

    #---------------------------------------------------------------------------
    def update_channel(self, channel, value):
        scale = value + 100.
        scale /= 200
        self.encoder.set_channel(channel, int(scale * 2047))

controller = Controller()

while 1:

    for i in range(25):
        #controller.send_sbus_msg()
        controller.port.write(b'\x0F')
        while(controller.port.out_waiting != 0):
            pass
        #controller.port.write(b'\x0F')
    time.sleep(0.07)
