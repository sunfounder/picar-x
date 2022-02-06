from typing import List
from time import sleep
from rossros import Bus

class IRSensors(object):
    def __init__(self) -> None:
        pass

    def _read(self)->List[int]:
        # return [0,0,0]
        return [2,2,0]

    def continuous_write_to_bus(self, ir_sensor_bus: Bus, shutdown_bus: Bus, time_delay: float):
        while not shutdown_bus.message:
            self.values = self._read()
            ir_sensor_bus.write(self.values)
            sleep(time_delay)

    def __call__(self):
        return self._read()
