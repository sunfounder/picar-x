import logging
import numpy as np
from typing import List
from time import sleep
from bus import Bus

DARKLINE = 0
LIGHTLINE = 1

class LineInterpreter(object):
    def __init__(self, sensitivity_threshold: int = 10, polarity: int = DARKLINE ) -> None:
        # Sensitivity threshold indicates the max difference between two sensor
        # readings that indicates that the robot is off the line
        self.sensitivity_threshold = sensitivity_threshold
        self.polarity = polarity

        self.state = 0

    def _build_state(self, raw_reading: List[int])->float:
        # Positive output indicates line is to the left of robot
        # Negative output indicates line is to the right of robot
        # Output is bounded from [-1,1]
        raw_reading_np = np.asarray(raw_reading)
        state = - np.average(np.diff(raw_reading_np)) / self.sensitivity_threshold
        if state > 1:
            state = 1.0
        elif state < -1:
            state = -1.0
        logging.info(f"Line interpreter state: {state}")
        return state

    def continuous_bus_read_write(self, ir_sensor_bus: Bus, state_bus: Bus, shutdown_bus: Bus, time_delay: float)->None:
        """ Continuously read sensor readings from sensor bus and write states to the state bus
        ir_sensor_bus: Bus for reading sensor values
        state_bus: Bus for writing state values
        shutdown_bus: Bus that holds True if a shutdown has been requested
        time_delay: seconds to wait before reading sensor bus and writing out
            new state
        """
        while not shutdown_bus.message:
            ir_values = ir_sensor_bus.message
            self.state = self._build_state(ir_values)
            state_bus.write(self.state)
            sleep(time_delay)

    def __call__(self, ir_sensor_values):
        return self._build_state(ir_sensor_values)
