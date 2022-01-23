import numpy as np
from typing import List

DARKLINE = 0
LIGHTLINE = 1

class LineInterpreter(object):
    def __init__(self, sensitivity_threshold: int = 100, polarity: int = DARKLINE ) -> None:
        # Sensitivity threshold indicates the max difference between two sensor
        # readings that indicates that the robot is off the line
        self.sensitivity_threshold = sensitivity_threshold
        self.polarity = polarity

    def build_state(self, raw_reading: List[int])->float:
        # Positive output indicates line is to the left of robot
        # Negative output indicates line is to the right of robot
        # Output is bounded from [-1,1]
        raw_reading_np = np.asarray(raw_reading)
        state = - np.average(np.diff(raw_reading_np)) / self.sensitivity_threshold
        if state > 1:
            state = 1.0
        elif state < -1:
            state = -1.0
        return state
