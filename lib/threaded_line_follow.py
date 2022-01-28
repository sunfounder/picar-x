import sys
import select
import tty
import termios
from time import sleep
import concurrent.futures

from picarx_improved import Picarx
from line_interpreter import DARKLINE, LineInterpreter
from line_follow_controller import LineFollowController
from terminal_monitor import TerminalMonitor
from bus import Bus

def main():
    # Setup terminal for easy shutdown
    terminal = TerminalMonitor()

    # Setup picar and line following classes
    px = Picarx()
    interpreter = LineInterpreter(sensitivity_threshold=100, polarity=DARKLINE)
    controller = LineFollowController(low_kp=10.0, high_kp=50.0)

    # Setup message busses with default messages
    sensor_values_bus = Bus([0,0,0])
    state_value_bus = Bus(0)
    shutdown_bus = Bus(False)

    # Setup time delays
    sensor_delay = 0.1
    interpreter_delay = 0.1
    shutdown_delay = 0.1

    # Start up processes to line follow until a shutdown command is recieved
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        eShutdown = executor.submit(terminal.continuous_monitor_shutdown, shutdown_bus, shutdown_delay)
        eSensor = executor.submit(px.ir_sensors.continuous_write_to_bus, sensor_values_bus, shutdown_bus, sensor_delay)
        eInterpreter = executor.submit(interpreter.continuous_bus_read_write, sensor_values_bus, state_value_bus, interpreter_delay)

    print("hello")
    # Start moving forward
    # px.drivetrain.set_speed(30)



    # # Line follow until a shutdown command is recieved
    # shutdown = False
    # while not shutdown:
    #     # Calculate steering angle through control loop
    #     ir_reading = px.ir_sensors.read()
    #     state = interpreter.build_state(ir_reading)
    #     steer_angle = controller.calculate_steering_angle(state)

    #     # Send commands to motors
    #     px.drivetrain.set_angle(steer_angle)

    #     # Shutdown with any keyboard input
    #     if isData():
    #         shutdown = True

    # # Restore terminal
    # termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


if __name__ == "__main__":
    main()
