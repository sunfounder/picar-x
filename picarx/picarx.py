from .get_hat import is_fusion_hat
if is_fusion_hat:
    from fusion_hat.pin import Pin
    from fusion_hat.adc import ADC
    from fusion_hat.servo import Servo
    from fusion_hat.modules.grayscale_module import LineTracker
    from fusion_hat.modules.ultrasonic import Ultrasonic
    from fusion_hat.device import get_usr_btn, set_led, get_battery_voltage, get_charge_state
    from fusion_hat.config import Config
else:
    from robot_hat.pin import Pin
    from robot_hat.adc import ADC
    from robot_hat.servo import Servo
    from robot_hat.modules import LineTracker
    from robot_hat.modules import Ultrasonic
    from robot_hat.device import get_usr_btn, set_led, get_battery_voltage
    from robot_hat.config import Config

from .motors import Motors
from .music import Music, SoundFiles
from .utils import LazyReader

from time import sleep

class PiCarX(object):
    CONFIG = '/opt/picar-x/picar-x.json'

    DEFAULT_LINE_REF = [1000, 1000, 1000]
    DEFAULT_CLIFF_REF = [500, 500, 500]

    DIR_MIN = -30
    DIR_MAX = 30
    CAM_PAN_MIN = -90
    CAM_PAN_MAX = 90
    CAM_TILT_MIN = -35
    CAM_TILT_MAX = 65

    # Distance between the front wheels and the rear wheels, in centimeters.
    WHEEL_BASE = 8.724
    # Distance between the left wheels and the right wheels, in centimeters.
    TRACK_WIDTH = 11.665

    def __init__(
        self,
        pan_servo: str = 'P0',
        tilt_servo: str = 'P1',
        steering_servo: str = 'P2',
        left_motor: str = 'M2',
        right_motor: str = 'M1',
        grayscale_pins: list = ['A0', 'A1', 'A2'],
        ultrasonic_pins: list = [27, 22],
        config_path: str = CONFIG,
        enable_differential_drive: bool = True
    ):
        '''
        Initializes the PiCarX object.

        Args:
            pan_servo (str): Pan servo pin. Defaults to 'P0'.
            tilt_servo (str): Tilt servo pin. Defaults to 'P1'.
            steering_servo (str): Steering servo pin. Defaults to 'P2'.
            left_motor (str): Left motor pin. Defaults to 'M2'.
            right_motor (str): Right motor pin. Defaults to 'M1'.
            grayscale_pins (list): List of grayscale sensor pin for left, middle and right. Defaults to ['A0', 'A1', 'A2'].
            ultrasonic_pins (list): List of ultrasonic sensor pin for trigger and echo. Defaults to [27, 22].
            config (str): Path to the configuration file. Defaults to CONFIG.
        '''
        self.power = 0
        self.steering_angle = 0

        # --------- config_path ---------
        self.config = Config(config_file=config_path)
        self.name = self.config.get("name", default_value="PiCar-X")

        # --------- camera mount init ---------
        # get calibration values
        camera_pan_offset = self.config.get("camera_pan_offset", default_value=0.0)
        camera_tilt_offset = self.config.get("camera_tilt_offset", default_value=0.0)
        self.camera_pan_servo = Servo(pan_servo, offset=camera_pan_offset, min=self.CAM_PAN_MIN, max=self.CAM_PAN_MAX)
        self.camera_tilt_servo = Servo(tilt_servo, offset=camera_tilt_offset, min=self.CAM_TILT_MIN, max=self.CAM_TILT_MAX)
        # set servos to init angle
        self.camera_pan_servo.angle(0)
        self.camera_tilt_servo.angle(0)

        # --------- chassis init ---------
        steering_offset = self.config.get("steering_offset", default_value=0.0)
        left_motor_reversed = self.config.get("left_motor_reversed", default_value=False)
        right_motor_reversed = self.config.get("right_motor_reversed", default_value=False)
        self.steering_servo = Servo(steering_servo, offset=steering_offset, min=self.DIR_MIN, max=self.DIR_MAX)
        self.motors = Motors(
            left_motor=left_motor,
            right_motor=right_motor,
            left_reversed=left_motor_reversed,
            right_reversed=right_motor_reversed)

        if enable_differential_drive:
            self.motors.init_differential_drive(self.WHEEL_BASE, self.TRACK_WIDTH)
        self.steering_servo.angle(0)

        # --------- grayscale module init ---------
        self.gs_slopes = self.config.get("grayscale_slopes", default_value=[1.0, 1.0, 1.0])
        self.gs_offsets = self.config.get("grayscale_offsets", default_value=[0.0, 0.0, 0.0])
        self.gs_cliff_threshold = self.config.get("grayscale_cliff_threshold", default_value=120)

        adc0, adc1, adc2 = [ADC(pin) for pin in grayscale_pins]
        self.grayscale = LineTracker(adc0, adc1, adc2)
        self.grayscale.set_calibration_data(self.gs_slopes, self.gs_offsets)
        self.grayscale.set_cliff_threshold(self.gs_cliff_threshold)

        # --------- ultrasonic init ---------
        trig, echo= ultrasonic_pins
        self.ultrasonic = Ultrasonic(Pin(trig), Pin(echo, mode=Pin.IN, pull=Pin.PULL_DOWN))

        # --------- battery voltage ---------
        if is_fusion_hat:
            self.battery_reader = LazyReader(get_battery_voltage, 60)
            self.charge_state_reader = LazyReader(get_charge_state, 5)
        else:
            self.battery_reader = None
            self.charge_state_reader = None

        # --------- music init ---------
        self.music = Music()
        self.music.set_volume(100)

        # --------- Actions ---------
        self.actions = {
            "wave hands": self.wave_hands,
            "resist": self.resist,
            "act cute": self.act_cute,
            "rub hands": self.rub_hands,
            "think": self.think,
            "keep think": self.keep_think,
            "shake head": self.shake_head,
            "nod": self.nod,
            "depressed": self.depressed,
            "twist body": self.twist_body,
            "celebrate": self.celebrate,
        }

        self.sounds_dict = {
            "honking": self.honking,
            "start engine": self.start_engine,
        }

    def get_usr_btn(self):
        return get_usr_btn()

    def set_led(self, value: int):
        set_led(value)

    def get_charge_state(self):
        ''' Get charge state
        
        Returns:
            bool: True if charging
        '''
        if is_fusion_hat:
            return self.charge_state_reader.read()
        else:
            print("Warning: charge state reader is not supported.")
            return None

    def get_battery_voltage(self):
        ''' Get battery voltage
        
        Returns:
            float: battery voltage value, range from 0 to 3.3.
        '''
        if is_fusion_hat:
            return self.battery_reader.read()
        else:
            print("Warning: battery reader is not supported.")
            return None


    def set_steering_angle(self, angle:float):
        ''' Set steering angle
        
        Args:
            angle (float): angle value, range from -30 to 30.
        '''
        self.steering_angle = angle
        self.steering_servo.angle(self.steering_angle)
        self.motors.set_power(self.power, self.steering_angle)

    def set_camera_pan_angle(self, angle:float):
        ''' Set camera pan servo angle
        
        Args:
            angle (float): angle value, range from -90 to 90.
        '''
        self.camera_pan_servo.angle(-angle)

    def set_camera_tilt_angle(self, angle:float):
        ''' Set camera tilt servo angle

        Args:
            angle (float): angle value, range from -35 to 65.
        '''
        self.camera_tilt_servo.angle(-angle)

    def backward(self, power:float):
        ''' Backward
        
        Args:
            power (float): power value, range from 0 to 100.
        '''
        self.power = -power
        self.motors.set_power(self.power, self.steering_angle)

    def forward(self, power:float):
        ''' Forward
        
        Args:
            power (float): power value, range from 0 to 100.
        '''
        self.power = power
        self.motors.set_power(self.power, self.steering_angle)

    def stop(self):
        ''' Stop motors '''
        self.power = 0
        self.motors.set_power(0)

    def get_distance(self):
        ''' Get distance from ultrasonic sensor
        
        Returns:
            int: distance value, range from 0 to 500.
        '''
        if not self.ultrasonic.thread_started:
            self.ultrasonic.start_thread()
        return self.ultrasonic.read()

    def get_grayscale_data(self, raw=False):
        ''' Get grayscale data
        
        Returns:
            list: grayscale data, range from 0 to 1023.
        '''
        return self.grayscale.read(raw=raw)

    def get_line_position(self, data: list = None):
        ''' Get line position

        Args:
            data (list): grayscale data, range from 0 to 1023. If None, use get_grayscale_data() to get data.

        Returns:
            float: line position value, range from -1.0 to 1.0.
        '''
        return self.grayscale.get_line_position(data=data)

    def is_on_cliff(self, data: list = None):
        ''' Detect if on cliff

        Args:
            data (list): grayscale data, range from 0 to 1023. If None, use get_grayscale_data() to get data.

        Returns:
            bool: True means on cliff, False means not on cliff.
        '''
        return self.grayscale.is_on_cliff(data=data)

    def is_on_line(self, data: list = None):
        ''' Detect if on line

        Args:
            data (list): grayscale data, range from 0 to 1023. If None, use get_grayscale_data() to get data.

        Returns:
            bool: True means on line, False means not on line.
        '''
        return self.grayscale.is_on_line(data=data)

    def reset(self):
        ''' Reset robot '''
        self.set_steering_angle(0)
        self.set_camera_tilt_angle(0)
        self.set_camera_pan_angle(0)
        self.stop()
        self.music.stop()
        self.set_led(0)

    def set_name(self, name:str):
        ''' Set robot name
        
        Args:
            name (str): robot name.
        '''
        self.name = name
        self.config.set("name", name)

    # Calibration functions
    def set_left_motor_reverse(self, reversed:bool):
        ''' Set if left motor is reversed
        
        Args:
            reversed (bool): True for reversed, False for not reversed.
        '''
        self.motors.set_left_reverse(reversed)
        self.config.set("left_motor_reversed", reversed)

    def set_right_motor_reverse(self, reversed:bool):
        ''' Set if right motor is reversed

        Args:
            reversed (bool): True for reversed, False for not reversed.
        '''
        self.motors.set_right_reverse(reversed)
        self.config.set("right_motor_reversed", reversed)

    def set_steering_offset(self, offset:float):
        ''' Set steering offset
        
        Args:
            offset (float): offset value, range from -20.0 to 20.0.
        '''
        offset = round(offset, 2)
        self.config.set("steering_offset", offset)
        self.steering_servo.offset(offset)
        self.steering_servo.angle(0)

    def set_camera_pan_offset(self, offset:float):
        ''' Set camera pan servo offset
        
        Args:
            offset (float): offset value, range from -20.0 to 20.0.
        '''
        offset = round(offset, 2)
        self.config.set("camera_pan_offset", offset)
        self.camera_pan_servo.offset(offset)
        self.camera_pan_servo.angle(0)

    def set_camera_tilt_offset(self, offset:float):
        ''' Set camera tilt servo offset
        
        Args:
            offset (float): offset value, range from -20.0 to 20.0.
        '''
        offset = round(offset, 2)
        self.config.set("camera_tilt_offset", offset)
        self.camera_tilt_servo.offset(offset)
        self.camera_tilt_servo.angle(0)

    def set_cliff_threshold(self, threshold: int):
        ''' Set grayscale cliff threshold
        
        Args:
            threshold (int): threshold value, range from 0 to 1023.
        '''
        self.config.set("grayscale_cliff_threshold", threshold)
        self.grayscale.set_cliff_threshold(threshold)

    def set_grayscale_calibration_data(self, slopes: list, offsets: list):
        '''
        Set the calibration values for the grayscale sensors.

        slopes: list - Grayscale sensor slopes.
        offsets: list - Grayscale sensor offsets.
        '''
        self.grayscale.set_calibration_data(slopes, offsets)
        self.config.set("grayscale_slopes", slopes)
        self.config.set("grayscale_offsets", offsets)

    def get_grayscale_calibration_data(self):
        ''' Get the calibration values for the grayscale sensors. '''
        return self.grayscale.get_calibration_data()

    def calibrate_grayscale(self, light: list, dark: list):
        ''' Calibrate grayscale sensors

        Args:
            light (list): light values, range from 0 to 4095.
            dark (list): dark values, range from 0 to 4095.
        '''
        slopes, offsets = self.grayscale.calibrate(light, dark)
        self.set_grayscale_calibration_data(slopes, offsets)

    def close(self):
        ''' Close robot '''
        self.reset()
        self.ultrasonic.stop_thread()

    # Actions
    def wave_hands(self):
        ''' Wave hands '''
        self.reset()
        self.set_camera_tilt_angle(20)
        for _ in range(2):
            self.set_steering_angle(-25)
            sleep(.1)
            self.set_steering_angle(25)
            sleep(.1)
        self.set_steering_angle(0)

    def resist(self):
        ''' Resist '''
        self.reset()
        self.set_camera_tilt_angle(10)
        for _ in range(3):
            self.set_steering_angle(-15)
            self.set_camera_pan_angle(15)
            sleep(.1)
            self.set_steering_angle(15)
            self.set_camera_pan_angle(-15)
            sleep(.1)
        self.stop()
        self.set_steering_angle(0)
        self.set_camera_pan_angle(0)

    def act_cute(self):
        ''' Act cute '''
        self.reset()
        self.set_camera_tilt_angle(-20)
        for i in range(15):
            self.forward(5)
            sleep(0.02)
            self.backward(5)
            sleep(0.02)
        self.set_camera_tilt_angle(0)
        self.stop()

    def rub_hands(self):
        ''' Rub hands '''
        self.reset()
        for i in range(5):
            self.set_steering_angle(-6)
            sleep(.5)
            self.set_steering_angle(6)
            sleep(.5)
        self.reset()

    def think(self):
        ''' Think '''
        self.reset()

        for i in range(11):
            self.set_camera_pan_angle(i*3)
            self.set_camera_tilt_angle(-i*2)
            self.set_steering_angle(i*2)
            sleep(.05)
        sleep(1)
        self.set_camera_pan_angle(15)
        self.set_camera_tilt_angle(-10)
        self.set_steering_angle(10)
        sleep(.1)
        self.reset()

    def keep_think(self):
        ''' Keep thinking '''
        self.reset()
        for i in range(11):
            self.set_camera_pan_angle(i*3)
            self.set_camera_tilt_angle(-i*2)
            self.set_steering_angle(i*2)
            sleep(.05)

    def shake_head(self):
        ''' Shake head '''
        # self.stop()
        self.set_camera_pan_angle(0)
        self.set_camera_pan_angle(60)
        sleep(.2)
        self.set_camera_pan_angle(-50)
        sleep(.1)
        self.set_camera_pan_angle(40)
        sleep(.1)
        self.set_camera_pan_angle(-30)
        sleep(.1)
        self.set_camera_pan_angle(20)
        sleep(.1)
        self.set_camera_pan_angle(-10)
        sleep(.1)
        self.set_camera_pan_angle(10)
        sleep(.1)
        self.set_camera_pan_angle(-5)
        sleep(.1)
        self.set_camera_pan_angle(0)

    def nod(self):
        ''' Nod '''
        self.reset()
        self.set_camera_tilt_angle(0)
        self.set_camera_tilt_angle(5)
        sleep(.1)
        self.set_camera_tilt_angle(-30)
        sleep(.1)
        self.set_camera_tilt_angle(5)
        sleep(.1)
        self.set_camera_tilt_angle(-30)
        sleep(.1)
        self.set_camera_tilt_angle(0)

    def depressed(self):
        ''' Depressed '''
        self.reset()
        self.set_camera_tilt_angle(0)
        self.set_camera_tilt_angle(20)
        sleep(.22)
        self.set_camera_tilt_angle(-22)
        sleep(.1)
        self.set_camera_tilt_angle(10)
        sleep(.1)
        self.set_camera_tilt_angle(-22)
        sleep(.1)
        self.set_camera_tilt_angle(0)
        sleep(.1)
        self.set_camera_tilt_angle(-22)
        sleep(.1)
        self.set_camera_tilt_angle(-10)
        sleep(.1)
        self.set_camera_tilt_angle(-22)
        sleep(.1)
        self.set_camera_tilt_angle(-15)
        sleep(.1)
        self.set_camera_tilt_angle(-22)
        sleep(.1)
        self.set_camera_tilt_angle(-19)
        sleep(.1)
        self.set_camera_tilt_angle(-22)
        sleep(.1)

        sleep(1.5)
        self.reset()

    def twist_body(self):
        ''' Twist body '''
        self.reset()
        for _ in range(3):
            self.forward(20)
            self.set_camera_pan_angle(-20)
            self.set_steering_angle(-10)
            sleep(.1)
            self.stop()
            self.set_camera_pan_angle(0)
            self.set_steering_angle(0)
            sleep(.1)
            self.backward(20)
            self.set_camera_pan_angle(20)
            self.set_steering_angle(10)
            sleep(.1)
            self.stop()
            self.set_camera_pan_angle(0)
            self.set_steering_angle(0)

            sleep(.1)

    def celebrate(self):
        ''' Celebrate '''
        self.reset()
        self.set_camera_tilt_angle(20)

        self.set_steering_angle(30)
        self.set_camera_pan_angle(60)
        sleep(.3)
        self.set_steering_angle(10)
        self.set_camera_pan_angle(30)
        sleep(.1)
        self.set_steering_angle(30)
        self.set_camera_pan_angle(60)
        sleep(.3)
        self.set_steering_angle(0)
        self.set_camera_pan_angle(0)
        sleep(.2)

        self.set_steering_angle(-30)
        self.set_camera_pan_angle(-60)
        sleep(.3)
        self.set_steering_angle(-10)
        self.set_camera_pan_angle(-30)
        sleep(.1)
        self.set_steering_angle(-30)
        self.set_camera_pan_angle(-60)
        sleep(.3)
        self.set_steering_angle(0)
        self.set_camera_pan_angle(0)
        sleep(.2)

    def honking(self):
        ''' Honking '''
        self.music.play_sound_background(SoundFiles.DOUBLE_HORN, volume=100)

    def start_engine():
        ''' Start engine '''
        self.music.play_sound_background(SoundFiles.START_ENGINE, volume=50)

