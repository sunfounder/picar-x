import sys
import select
import tty
import termios
from time import sleep
import concurrent.futures
import logging

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
    controller_delay = 0.1

    # Start up processes to line follow until a shutdown command is recieved
    logging.info("Starting threads.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        eShutdown = executor.submit(terminal.continuous_monitor_shutdown, shutdown_bus, shutdown_delay)
        eSensor = executor.submit(px.ir_sensors.continuous_write_to_bus, sensor_values_bus, shutdown_bus, sensor_delay)
        eInterpreter = executor.submit(interpreter.continuous_bus_read_write, sensor_values_bus, state_value_bus, shutdown_bus, interpreter_delay)
        eController = executor.submit(controller.continuous_bus_control, px.drivetrain, state_value_bus, shutdown_bus, controller_delay)

    # Notification of shutdown
    logging.info("Shutting down.")
    
    # Display any exceptions
    eShutdown.result()
    eSensor.result()
    eInterpreter.result()
    eController.result()
 

if __name__ == "__main__":
    main()
