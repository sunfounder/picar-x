import sys
import select
import tty
import termios
import atexit
from time import sleep
import logging

from bus import Bus

class TerminalMonitor():
    def __init__(self) -> None:
        # Setup terminal so we can recieve shutdown command via keyboard
        self._old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())
        # Setup cleanup command to restore terminal upon shutdown
        atexit.register(self._cleanup)

    def _isData(self):
        # https://stackoverflow.com/questions/2408560/non-blocking-console-input
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def _cleanup(self):
        # Restore terminal
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._old_settings)

    def continuous_monitor_shutdown(self, shutdown_bus: Bus, time_delay: float):
        shutdown = False
        while not shutdown:
            sleep(time_delay)
            if self._isData():
                shutdown = True
        shutdown_bus.write(shutdown)

    def __call__(self):
        d = self._isData()
        logging.debug(f"TerminalMonitor returned {d} for termination.")
        return d
