import smbus, math
from ezblock.basic import _Basic_class

class Timer(_Basic_class):
    REG_PSC = 0x28
    REG_ARR = 0x2A
    ADDR = 0x14

    PRECISION = 4095
    CLOCK = 72000000

    def __init__(self, channel):
        super().__init__()
        if isinstance(channel, str):
            if channel.startswith("P"):
                channel = int(channel[1:])
            else:
                raise ValueError("PWM channel should be between [P1, P8], not {0}".format(channel))
        self.channel = channel + 0x20
        self.bus = smbus.SMBus(1)
        self._pulse_width = 0
        self._freq = 50
        self.freq(50)

    def i2c_write(self, reg, value):
        value_h = value >> 8
        value_l = value & 0xff
        self.bus.write_byte(self.ADDR, reg)
        self.bus.write_byte(self.ADDR, value_h)
        self.bus.write_byte(self.ADDR, value_l)
        self._debug("i2c write: [0x%02X, 0x%02X, 0x%02X, 0x%02X]"%(self.ADDR, reg, value_h, value_l))

    def freq(self, *freq):
        if len(freq) == 0:
            return self._freq
        else:
            self._freq = freq[0]
            # [prescaler,arr] list
            result_ap = []
            # accuracy list
            result_acy = []
            # middle value for equal arr prescaler
            st = int(math.sqrt(self.CLOCK/self._freq))
            # get -5 value as start
            st -= 5
            # prevent negetive value
            if st <= 0:
                st = 1
            for psc in range(st,st+10):
                arr = int(self.CLOCK/self._freq/psc)     # 72000000/50/
                result_ap.append([psc, arr])
                result_acy.append(abs(self._freq-self.CLOCK/psc/arr))
            i = result_acy.index(min(result_acy))
            psc = result_ap[i][0]
            arr = result_ap[i][1]
            self._debug("prescaler: %s, period: %s"%(psc, arr))
            self.prescaler(psc)
            self.period(arr)
    
    def prescaler(self, *prescaler):
        if len(prescaler) == 0:
            return self._prescaler
        else:
            self._prescaler = prescaler[0]
            self._debug("Set prescaler to: %s"%self._prescaler)
            self.i2c_write(self.REG_PSC, self._prescaler)

    def period(self, *arr):
        if len(arr) == 0:
            return self._arr
        else:
            self._arr = arr[0]
            self._debug("Set arr to: %s"%self._arr)
            self.i2c_write(self.REG_ARR, self._arr)

    def pulse_width(self, *pulse_width):
        if len(pulse_width) == 0:
            return self._pulse_width
        else:
            self._pulse_width = pulse_width[0]
            CCR = int(self._pulse_width/self.PRECISION * self._arr) # 4095 / 4095 * period(周期默认)
            # print("CCR: %s"%CCR)
            self.i2c_write(self.channel, CCR)

    def pulse_width_percent(self, *pulse_width_percentage):
        if len(pulse_width_percentage) == 0:
            return self._pulse_width_percentage
        else:
            self._pulse_width_percentage = pulse_width_percentage[0] / 100.0
            pulse_width = self._pulse_width_percentage * self._arr
            self.pulse_width(pulse_width)


def test():
    import time
    p = Timer(5)
    # p.debug = 'debug'
    p.period(1000)
    p.prescaler(10)
    # p.pulse_width(2048)
    while True:
        for i in range(0, 4095, 10):
            p.pulse_width(i)
            print(i)
            time.sleep(1/4095)
        time.sleep(1)
        for i in range(4095, 0, -10):
            p.pulse_width(i)
            print(i)
            time.sleep(1/4095)
        time.sleep(1)

if __name__ == '__main__':
    test()