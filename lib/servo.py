# from .basic import _Basic_class
import time

class Servo(object):
    MAX_PW = 2500
    MIN_PW = 500
    _freq = 50
    def __init__(self, pwm):
        super().__init__()
        self.pwm = pwm
        self.pwm.period(4095)
        prescaler = int(float(self.pwm.CLOCK) /self.pwm._freq/self.pwm.period())
        self.pwm.prescaler(prescaler)
        # self.angle(90)

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        
    # angle ranges -90 to 90 degrees
    def angle(self, angle):
        if not (isinstance(angle, int) or isinstance(angle, float)):
            raise ValueError("Angle value should be int or float value, not %s"%type(angle))
        if angle < -90:
            angle = -90
        if angle > 90:
            angle = 90
        High_level_time = self.map(angle, -90, 90, self.MIN_PW, self.MAX_PW)
        # self._debug("High_level_time: %f" % High_level_time)
        pwr =  High_level_time / 20000
        # self._debug("pulse width rate: %f" % pwr)
        value = int(pwr*self.pwm.period())
        # self._debug("pulse width value: %d" % value)
        self.pwm.pulse_width(value)

def test():
    from ezblock import PWM
    print("Test")
    p = PWM("P0")
    s0 = Servo(p)
    s0.debug = "debug"
    s0.angle(90)
    
if __name__ == "__main__":
    test()