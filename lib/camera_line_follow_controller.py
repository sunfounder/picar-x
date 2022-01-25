from lib2to3.pgen2 import driver
from typing import Optional
import numpy as np
import sys
import select
import tty
import termios
import atexit

from line_follow_controller import LineFollowController
from camera_line_interpreter import CameraLineInterpreter
from drivetrain import DriveTrain

class CameraLineFollowController(LineFollowController):
    def __init__(self, interpreter: CameraLineInterpreter, drivetrain: DriveTrain, low_kp: Optional[float] = None, high_kp: Optional[float] = None) -> None:
        if low_kp is not None and high_kp is not None:
            super().__init__(low_kp, high_kp)
        elif low_kp is not None:
            super().__init__(low_kp)
        elif high_kp is not None:
            super().__init__(high_kp)
        else:
            super().__init__()
        self.interpreter = interpreter
        self.drivetrain = drivetrain

        # Setup terminal for controller shutdown via keyboard
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        atexit.register(self._cleanup)

    def control_func(self, raw_reading: np.array):
        # Turn the raw reading into some useful state we can control
        state = self.interpreter(raw_reading)
        # Calculate a steering angle based on that state
        steer_angle = self.calculate_steering_angle(state)
        # Send steering angle to motors
        self.drivetrain.set_angle(steer_angle)
        # Check for any terminal input indicating a requested shutdown
        return self._isData()

    def _isData():
        # https://stackoverflow.com/questions/2408560/non-blocking-console-input
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def _cleanup(self):
        # Restore terminal
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)
