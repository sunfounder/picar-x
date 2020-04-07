from ezblock.pin import Pin
from ezblock.pwm import PWM

class LED(Pin):
    def __init__(self):
        super().__init__()
        self._pwm_on = False

    def on(self):
        super().on()
        self._intensity_value = 100

    def off(self):
        super().off()
        self._intensity_value = 0
        self.pwm_off()

    def pwm_on(self):
        if not self._pwm_on:
            self.pwm = PWM(self._pin)
            self.pwm.frequency(50)
            self._pwm_on = True

    def pwm_off(self):
        if self._pwm_on:
            self.pwm.off()
            self._pwm_on = False

    def intensity(self, *value):
        if len(value) == 0:
            return self._intensity_value
        else:
            self.pwm_on()
            self._intensity_value = value[0]
            self.pwm.pulse_width(self._intensity_value)
