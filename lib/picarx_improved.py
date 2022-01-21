import time
import atexit
from os.path import realpath
import pkg_resources
import logging
from sys import exit

# Setup logging format
logging_format = "%(asctime)s [%(levelname)s] %(funcName)s(): %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO,
    datefmt="%H:%M:%S")

def on_raspi()->bool:
    """ Return True if running on a raspberry pi
    and False if running on workstation
    """
    installed_libraries = {pkg.key for pkg in pkg_resources.working_set}
    if 'RPi' in installed_libraries:
        return True
    else:
        return False

# Check if on picar or on workstation
if on_raspi():
    try:
        from drivetrain import DriveTrain
        from servo import Servo
        from pwm import PWM
        from pin import Pin
        from adc import ADC
        from filedb import fileDB
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
    from servo_sim import Servo
    from pwm_sim import PWM
    from pin_sim import Pin
    from adc_sim import ADC
    from filedb_sim import fileDB

class Picarx(object):
    TIMEOUT = 0.02

    def __init__(self):
        # Config
        config_dir = '/'.join(realpath(__file__).split('/')[:-1])
        self.config_file = fileDB(config_dir+'/.config')

        # Camera info
        self.camera_servo_pin1 = Servo(PWM('P0'))
        self.camera_servo_pin2 = Servo(PWM('P1'))
        self.cam_cal_value_1 = int(self.config_file.get("picarx_cam1_servo", default_value=0))
        self.cam_cal_value_2 = int(self.config_file.get("picarx_cam2_servo", default_value=0))
        self.camera_servo_pin1.angle(self.cam_cal_value_1)
        self.camera_servo_pin2.angle(self.cam_cal_value_2)

        # IR Sensors
        self.S0 = ADC('A0')
        self.S1 = ADC('A1')
        self.S2 = ADC('A2')

        # Setup drivetrain
        self.drivetrain = DriveTrain(self.config_file)

        # Register exit command
        atexit.register(self.cleanup)

    def camera_servo1_angle_calibration(self,value):
        self.cam_cal_value_1 = value
        self.config_file.set("picarx_cam1_servo", "%s"%value)
        print("cam_cal_value_1:",self.cam_cal_value_1)
        self.camera_servo_pin1.angle(value)

    def camera_servo2_angle_calibration(self,value):
        self.cam_cal_value_2 = value
        self.config_file.set("picarx_cam2_servo", "%s"%value)
        print("picarx_cam2_servo:",self.cam_cal_value_2)
        self.camera_servo_pin2.angle(value)

    def set_camera_servo1_angle(self,value):
        self.camera_servo_pin1.angle(-1*(value + -1*self.cam_cal_value_1))
        print((value + self.cam_cal_value_1))

    def set_camera_servo2_angle(self,value):
        self.camera_servo_pin2.angle(-1*(value + -1*self.cam_cal_value_2))
        print((value + self.cam_cal_value_2))

    def get_adc_value(self):
        adc_value_list = []
        adc_value_list.append(self.S0.read())
        adc_value_list.append(self.S1.read())
        adc_value_list.append(self.S2.read())
        return adc_value_list

    def Get_distance(self):
        timeout=0.01
        trig = Pin('D8')
        echo = Pin('D9')

        trig.low()
        time.sleep(0.01)
        trig.high()
        time.sleep(0.000015)
        trig.low()
        pulse_end = 0
        pulse_start = 0
        timeout_start = time.time()
        while echo.value()==0:
            pulse_start = time.time()
            if pulse_start - timeout_start > timeout:
                return -1
        while echo.value()==1:
            pulse_end = time.time()
            if pulse_end - timeout_start > timeout:
                return -2
        during = pulse_end - pulse_start
        cm = round(during * 340 / 2 * 100, 2)
        return cm

    def cleanup(self):
        self.drivetrain.stop()

if __name__ == "__main__":
    px = Picarx()
    px.drivetrain.set_speed(100)
    time.sleep(1)
