import sys
import select
import tty
import termios

from picarx_improved import Picarx
from line_interpreter import DARKLINE, LineInterpreter
from line_follow_controller import LineFollowController

def isData():
    # https://stackoverflow.com/questions/2408560/non-blocking-console-input
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def main():
    # Setup terminal so we can recieve shutdown command via keyboard
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())

    # Setup picar and line following classes
    px = Picarx()
    interpreter = LineInterpreter(sensitivity_threshold=120, polarity=DARKLINE)
    controller = LineFollowController(kp=2.0)

    # Start moving forward
    px.drivetrain.set_speed(40)

    # Line follow until a shutdown command is recieved
    shutdown = False
    while not shutdown:
        # Calculate steering angle through control loop
        ir_reading = px.ir_sensors.read()
        state = interpreter.build_state(ir_reading)
        steer_angle = controller.calculate_steering_angle(state)

        # Send commands to motors
        px.drivetrain.set_angle(steer_angle)

        # Shutdown with any keyboard input
        if isData():
            shutdown = True

    # Restore terminal
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


if __name__ == "__main__":
    main()