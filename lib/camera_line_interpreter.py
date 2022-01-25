import logging
import numpy as np

class CameraLineInterpreter(object):
    def __init__(self) -> None:
        pass

    def build_state(self, raw_reading: np.array)->float:
        # Positive output indicates line is to the left of robot
        # Negative output indicates line is to the right of robot
        # Output is bounded from [-1,1]

        state = 0
        return state
