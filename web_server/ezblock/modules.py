from ezblock import I2C
import time

class Ultrasonic():
    def __init__(self, trig, echo, timeout=0.02):
        self.trig = trig
        self.echo = echo
        self.timeout = timeout

    def _read(self):
        self.trig.low()
        time.sleep(0.01)
        self.trig.high()
        time.sleep(0.00001)
        self.trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while self.echo.value()==0:
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while self.echo.value()==1:
            pulse_end = time.time()
            if pulse_end - timeout_start > self.timeout:
                return -1
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def read(self, times=10):
        for i in range(times):
            a = self._read()
            if a != -1:
                return a
        return -1
                

class DS18X20():
    def __init__(self, *args, **kargs):
        # self.pin = pin
        pass
    
    def scan(self):
        import os
        roms = []
        for rom in os.listdir('/sys/bus/w1/devices'):
            if rom.startswith('28-'):
                roms.append(rom)
        return roms

    def convert_temp(self):
        pass
    
    def read_temp(self, rom):
        location = '/sys/bus/w1/devices/' + rom + '/w1_slave'
        with open(location) as f:
            text = f.read()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature

    def read(self, unit=1):
        # unit=0:  Fahrenheit
        # unit=1:  degree Celsius
        self.roms = self.scan()
        self.convert_temp()
        temps = []
        for rom in self.roms:
            temp = self.read_temp(rom)
            if unit == 0:
                temp = 32 + temp * 1.8
            temps.append(temp)
        if len(temps) == 0:
            raise IOError("Cannot detect any DS18X20, please check the connection")
        elif len(temps) == 1:
            temps = temps[0]
        return temps

class ADXL345():
    X = 0
    Y = 1
    Z = 2
    _REG_DATA_X       = 0x32 # X-axis data 0 (6 bytes for X/Y/Z)
    _REG_DATA_Y       = 0x34 # Y-axis data 0 (6 bytes for X/Y/Z)
    _REG_DATA_Z       = 0x36 # Z-axis data 0 (6 bytes for X/Y/Z)
    _REG_POWER_CTL    = 0x2D # Power-saving features control
    _AXISES = [_REG_DATA_X, _REG_DATA_Y, _REG_DATA_Z]

    def __init__(self, address=0x53):  
        self.i2c = I2C()
        self.address = address

    def read(self, axis):
        result = self.i2c._i2c_read_byte(self.address)
        send = (0x08<< 8) + self._REG_POWER_CTL
        if result:
            self.i2c.send(send, self.address)
        self.i2c.mem_write(0, 0x53, 0x31, timeout=1000)
        self.i2c.mem_write(8, 0x53, 0x2D, timeout=1000)
        raw = self.i2c.mem_read(2, self.address, self._AXISES[axis])
        # 第一次读的值总是为0，所以多读取一次
        self.i2c.mem_write(0, 0x53, 0x31, timeout=1000)
        self.i2c.mem_write(8, 0x53, 0x2D, timeout=1000)
        raw = self.i2c.mem_read(2, self.address, self._AXISES[axis])
        if raw[1]>>7 == 1:
            raw[1] = -((((raw[1]^128)^127)+1))
        g = raw[1]<< 8 | raw[0]
        value = g / 256.0
        return value

class RGB_LED():
    def __init__(self, Rpin, Gpin, Bpin, common=1):
        self.Rpin = Rpin
        self.Gpin = Gpin
        self.Bpin = Bpin
        self.common = common
    
    def write(self, color):
        if isinstance(color, str):
            color = color.strip("#")
            color = int(color, 16)
        R_val = (color & 0xff0000) >> 16
        G_val = (color & 0x00ff00) >> 8
        B_val = (color & 0x0000ff) >> 0

        if self.common == 1: # common anode 
            R_val = 255-R_val
            G_val = 255-G_val
            B_val = 255-B_val
        
        R_val = R_val / 255.0 * 100.0
        G_val = G_val / 255.0 * 100.0
        B_val = B_val / 255.0 * 100.0

        self.Rpin.pulse_width_percent(R_val)
        self.Gpin.pulse_width_percent(G_val)
        self.Bpin.pulse_width_percent(B_val)

class Buzzer():
    def __init__(self, pwm):
        self.pwm = pwm
    
    def on(self):
        self.pwm.pulse_width_percent(50)
    
    def off(self):
        self.pwm.pulse_width_percent(0)
    
    def freq(self, freq):
        self.pwm.freq(freq)
    
    def play(self, *args):
        try:
            freq = args[0]
        except:
            raise ValueError("Buzzer must have freq argument")
        self.freq(freq)
        self.on()
        try:
            ms = args[1]
        except:
            return freq
        ms = int(ms)
        from ezblock import delay
        delay(ms)
        self.off()
        delay(ms)
        return freq

class Sound():
    def __init__(self, pin):
        self.pin = pin
    
    def read_raw(self):
        return self.pin.read()
    
    def read(self, times=50):
        value_list = []
        for _ in range(times):
            value = self.read_raw()
            value_list.append(value)
        value = sum(value_list)/times
        return value

class Joystick():
    import math
    THRESHOLD = 2047 / math.sqrt(2)
    def __init__(self, Xpin, Ypin, Btpin):
        self.pins = [Xpin, Ypin, Btpin]
        self.pins[2].init(self.pins[2].IN, pull=self.pins[2].PULL_UP,)

    def read(self, axis):
        pin = self.pins[axis]
        if axis == 2:
            value = pin.value()
        else:
            value = pin.read() - 2047
        return value

    def read_status(self):
        state = ['home', 'up', 'down', 'left', 'right', 'pressed']
        i = 0
        if self.read(1) < -self.THRESHOLD: # Y
            i = 1       #up
        elif self.read(1) > self.THRESHOLD: # Y
            i = 2       #down
        elif self.read(0) < -self.THRESHOLD: # X
            i = 3       #right
        elif self.read(0) > self.THRESHOLD: # X
            i = 4       #left
        elif self.read(2) == 0: # Bt
            i = 5       # Button pressed
        else:
            i = 0
        return state[i]


def test():
    # import time
    # adxl345 = ADXL345()
    # a1 = adxl345.read(0)
    # a2 = adxl345.read(1)
    # a3 = adxl345.read(2)
    # a = [a1, a2, a3]
    # print(a)
    print("%s"%ADXL345().read(0))
    time.sleep(1)

if __name__ == "__main__":
    while True:
        test()