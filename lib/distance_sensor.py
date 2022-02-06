from pin import Pin
import time

class DistanceSensor(object):
    def __init__(self) -> None:
        self.timeout = 0.1
        self.trigger_pin = Pin('D2')
        self.echo_pin = Pin('D3')

    def _read(self)->float:
        self.trigger_pin.low()
        time.sleep(0.01)
        self.trigger_pin.high()
        time.sleep(0.000015)
        #time.sleep(0.01)
        self.trigger_pin.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while self.echo_pin.value()==0:
            #print(1)
            pulse_start = time.time()
            if pulse_start - timeout_start > self.timeout:
                return -1
        while self.echo_pin.value()==1:
            #print(2)
            pulse_end = time.time()
            if pulse_end - timeout_start > self.timeout:
                return -2
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def __call__(self) -> float:
        return self._read()
