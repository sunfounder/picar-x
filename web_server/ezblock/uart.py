from serial import Serial

class UART(object):
    def __init__(self, device, baudrate=115200, tx=None, rx=None):
        self._port = device
        self._baudrate = baudrate
        self.ser = Serial(self._port, self._baudrate, timeout=1)

    def deinit(self):
        pass

    def read(self, num):
        buf = self.ser.read(num)
        # buf = buf.decode('utf-8')
        return buf

    def readinto(self, buf):
        buf = self.ser.read(len(buf))
        # pass

    def readline(self):
        pass

    def write(self, buf):
        # buf = buf.encode('utf-8')
        self.ser.write(buf)

    def inWaiting(self):
        return self.ser.inWaiting()