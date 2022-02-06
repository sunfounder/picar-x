import time
import atexit
from os.path import realpath
import pkg_resources
import logging
from sys import exit
from filedb import fileDB

# Setup logging format
logging_format = "%(asctime)s [%(levelname)s] %(funcName)s(): %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO,
    datefmt="%H:%M:%S")

def on_raspi()->bool:
    """ Return True if running on a raspberry pi
    and False if running on workstation
    """
    installed_libraries = {pkg.key for pkg in pkg_resources.working_set}
    if 'rpi.gpio' in installed_libraries:
        return True
    else:
        return False

# Check if on picar or on workstation
if on_raspi():
    try:
        from drivetrain import DriveTrain
        from ir_sensors import IRSensors
        from distance_sensor import DistanceSensor
        from camera import Camera
        from utils import reset_mcu
        reset_mcu()
    except ImportError:
        logging.error("Found RPi library, implying this computer is a" \
            "PiCar-X system. However, failed to import picarx" \
            "libraries. Investigate ImportError.")
        exit()
else:
    logging.warning("This computer does not appear to be a PiCar-X system " \
        "(cannot import picarx libraries). Shadowing hardware class with " \
        "substitue functions.")
    from drivetrain_sim import DriveTrain
    from ir_sensors_sim import IRSensors
    from distance_sensor_sim import DistanceSensor
    from camera_sim import Camera

class Picarx(object):
    TIMEOUT = 0.02

    def __init__(self):
        # Config
        config_dir = '/'.join(realpath(__file__).split('/')[:-1])
        self.config_file = fileDB(config_dir+'/.config')

        # Setup sensors
        self.ir_sensors = IRSensors()
        self.distance_sensor = DistanceSensor()
        self.camera = Camera(self.config_file)

        # Setup drivetrain
        self.drivetrain = DriveTrain(self.config_file)

        # Register exit command
        atexit.register(self.cleanup)

    def cleanup(self):
        self.drivetrain.stop()

if __name__ == "__main__":
    px = Picarx()
    px.drivetrain.set_speed(100)
    time.sleep(1)
