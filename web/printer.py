#########################################################
#
# This file is part of:
# Sounding Poetry of Perception
#
# Purpose:  communication with Thermal Printer Cashino
#           from sparkfun.com - COM-10438
#           baudrate: 19200 / character code table: CP437
#
#########################################################

from serial import Serial
from serial import *

class Printer():
    # main printer class
    def __init__(self, serialPort='/dev/ttyUSB0', baudRate='19200'):
        self.status = 'disconnected'
        self.port = serialPort
        self.baud = baudRate
        self.cp = 'cp437'   # printer code page
        self.term = '\r\n'   # termination character
        self.printer = None

    def connect(self):
        try:
            printer = Serial(self.port, self.baud, timeout=1)
            self.status = 'connected'
            self.printer = printer
        except SerialException:
            print('Port already open')
            self.status = 'port already open'
            self.printer = None

    def disconnect(self):
        if self.printer is not None:
            self.printer.close()
            self.status = 'disconnected'
            return True
        else:
            return False

    def print(self, message):
        if self.status is 'connected':
            msg = message + self.term
            self.printer.write(msg.encode(encoding=self.cp, errors='strict'))

def main():
    printer = Printer()
    printer.connect()
    printer.print('kiss my ass')
    printer.disconnect()



if __name__ == "__main__":
    main()
