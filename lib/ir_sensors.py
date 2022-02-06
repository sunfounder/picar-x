from time import sleep
from typing import List
from adc import ADC
from bus import Bus

class IRSensors(object):
    def __init__(self) -> None:
        # Initialize IR sensor pins
        self.S0 = ADC('A0')
        self.S1 = ADC('A1')
        self.S2 = ADC('A2')

        self.values = [0, 0, 0]

    def _read(self)->List[int]:
        """ Read IR sensor array
        """
        adc_value_list = []
        adc_value_list.append(self.S0.read())
        adc_value_list.append(self.S1.read())
        adc_value_list.append(self.S2.read())
        return adc_value_list

    def continuous_write_to_bus(self, ir_sensor_bus: Bus, shutdown_bus: Bus, time_delay: float):
        """ Continuously write new sensor readings to bus
        ir_sensor_bus: Bus for writing out sensor values
        shutdown_bus: Bus that holds True if a shutdown has been requested
        time_delay: seconds to wait before reading sensors and writing out
            new values
        """
        while not shutdown_bus.message:
            self.values = self._read()
            ir_sensor_bus.write(self.values)
            sleep(time_delay)
   
    def __call__(self):
        return self._read()

