import time
import serial
import serial.tools.list_ports
from config import THT_UNIT_PORT_ADDR

class SerialCom():
    def __init__(self):
        self.com = None

    def connect(self):
        setup = False
        prev = time.time()
        while(not setup):
            try:
                self.com = serial.Serial(THT_UNIT_PORT_ADDR, 115200, timeout=1)
            except:
                if(time.time() - prev > 2):
                    print("No serial detected, please plug your Controller")
                    break

            if(self.com is not None): # We're connected
                setup = True


    # read one char (default)
    def read_serial(self, num_char = 1):
        if self.com is not None:
            string = self.com.read(num_char)
            return string.decode()


    # Write whole strings
    def write_serial(self, cmd):
        if self.com is not None:
            cmd = cmd + '\n'
            self.com.write(cmd.encode())