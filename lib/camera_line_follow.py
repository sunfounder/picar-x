import sys
import select
import tty
import termios
import numpy as np

from picarx_improved import Picarx
from camera_line_interpreter import CameraLineInterpreter
from camera_line_follow_controller import CameraLineFollowController

def isData():
    # https://stackoverflow.com/questions/2408560/non-blocking-console-input
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def main():
    # Setup picar and line following classes
    px = Picarx()
    interpreter = CameraLineInterpreter()
    controller = CameraLineFollowController(interpreter=interpreter, drivetrain=px.drivetrain, low_kp=10.0, high_kp=50.0)

    # Start moving forward
    px.drivetrain.set_speed(30)

    # Line follow until a shutdown command is recieved
    px.camera.control_based_on_camera(controller.control_func, display=True)

if __name__ == "__main__":
    main()
