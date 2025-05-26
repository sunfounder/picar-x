from robot_hat import Pin, ADC, Servo
from robot_hat import Grayscale_Module, Ultrasonic, utils
from .motors import Motors
from .music import Music, SoundFiles
from .utils import Config

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
        servo_pins: list = ['P0', 'P1', 'P2'],
        motor_pins: list = ['P13', 'D4', 'P12', 'D5'],
        grayscale_pins: list = ['A0', 'A1', 'A2'],
        ultrasonic_pins: list = ['D2', 'D3'],  # 添加空格
        config_file: str = CONFIG,
        enable_differential_drive: bool = True
    ):
        '''
        Initializes the PiCarX object.

        Args:
            servo_pins (list): List of servo pin names. Defaults to ['P0', 'P1', 'P2'].
            motor_pins (list): List of motor pin names. Defaults to ['D4', 'D5', 'P13', 'P12'].
            grayscale_pins (list): List of grayscale sensor pin names. Defaults to ['A0', 'A1', 'A2'].
            ultrasonic_pins (list): List of ultrasonic sensor pin names. Defaults to ['D2', 'D3'].
            config (str): Path to the configuration file. Defaults to CONFIG.
        '''
        # reset robot_hat
        utils.reset_mcu()
        sleep(0.2)
        self.power = 0
        self.steering_angle = 0

        # --------- config_file ---------
        self.config = Config(config_file)

        # --------- servos init ---------
        # get calibration values
        steering_offset = self.config.get("steering_offset", default_value=0.0)
        camera_pan_offset = self.config.get("camera_pan_offset", default_value=0.0)
        camera_tilt_offset = self.config.get("camera_tilt_offset", default_value=0.0)
        self.camera_pan_servo = Servo(servo_pins[0], offset=camera_pan_offset, min=self.CAM_PAN_MIN, max=self.CAM_PAN_MAX)
        self.camera_tilt_servo = Servo(servo_pins[1], offset=camera_tilt_offset, min=self.CAM_TILT_MIN, max=self.CAM_TILT_MAX)
        self.steering_servo = Servo(servo_pins[2], offset=steering_offset, min=self.DIR_MIN, max=self.DIR_MAX)
        print(f"steering_offset: {steering_offset}")
        print(f"camera_pan_offset: {camera_pan_offset}")
        print(f"camera_tilt_offset: {camera_tilt_offset}")
        # set servos to init angle
        self.camera_pan_servo.angle(0)
        self.camera_tilt_servo.angle(0)
        self.steering_servo.angle(0)

        # --------- motors init ---------
        left_motor_reversed = self.config.get("left_motor_reversed", default_value=True)
        right_motor_reversed = self.config.get("right_motor_reversed", default_value=False)
        self.motors = Motors(*motor_pins, left_reversed=left_motor_reversed, right_reversed=right_motor_reversed)
        if enable_differential_drive:
            self.motors.init_differential_drive(self.WHEEL_BASE, self.TRACK_WIDTH)

        # --------- grayscale module init ---------
        adc0, adc1, adc2 = [ADC(pin) for pin in grayscale_pins]
        self.grayscale = Grayscale_Module(adc0, adc1, adc2, reference=None)
        # get reference
        self.line_reference = self.config.get("line_reference", default_value=self.DEFAULT_LINE_REF)
        self.cliff_reference = self.config.get("cliff_reference", default_value=self.DEFAULT_CLIFF_REF)
        # transfer reference
        self.grayscale.reference(self.line_reference)

        # --------- ultrasonic init ---------
        trig, echo= ultrasonic_pins
        self.ultrasonic = Ultrasonic(Pin(trig), Pin(echo, mode=Pin.IN, pull=Pin.PULL_DOWN))
        self.usr_btn = Pin("USER", mode=Pin.IN, pull=Pin.PULL_UP)
        self.rst_btn = Pin("RST", mode=Pin.IN, pull=Pin.PULL_UP)
        self.led = Pin("LED", mode=Pin.OUT)

        # --------- music init ---------
        self.music = Music()
        self.music.set_music_volume(100)

        # --------- Actions ---------
        self.actions_dict = {
            "shake head": self.shake_head, 
            "nod": self.nod,
            "wave hands": self.wave_hands,
            "resist": self.resist,
            "act cute": self.act_cute,
            "rub hands": self.rub_hands,
            "think": self.think,
            "twist body": self.twist_body,
            "celebrate": self.celebrate,
            "depressed": self.depressed,
        }

        self.sounds_dict = {
            "honking": self.honking,
            "start engine": self.start_engine,
        }


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
        self.motors.set_power(0)

    def get_distance(self):
        ''' Get distance from ultrasonic sensor
        
        Returns:
            int: distance value, range from 0 to 500.
        '''
        return self.ultrasonic.read()

    def get_grayscale_data(self):
        ''' Get grayscale data
        
        Returns:
            list: grayscale value list, range from 0 to 1023.
        '''
        return list.copy(self.grayscale.read())

    def get_line_status(self, gm_val_list:list):
        ''' Get line status
        
        Args:
            gm_val_list (list): grayscale value list, range from 0 to 1023.
        Returns:
            list: line status list, 1 means on line, 0 means off line.
        '''
        return self.grayscale.read_status(gm_val_list)

    def get_cliff_status(self, gm_val_list:list):
        ''' Get cliff status

        Args:
            gm_val_list (list): grayscale value list, range from 0 to 1023.
        Returns:
            bool: True means on cliff, False means not on cliff.
        '''
        for i in range(0,3):
            if gm_val_list[i]<=self.cliff_reference[i]:
                return True
        return False

    def get_battery_voltage(self):
        ''' Get battery voltage
        
        Returns:
            float: battery voltage value, range from 0 to 3.3.
        '''
        return utils.get_battery_voltage()

    def reset_mcu(self):
        ''' Reset robot_hat '''
        return utils.reset_mcu()

    def reset(self):
        ''' Reset robot '''
        self.stop()
        self.set_steering_angle(0)
        self.set_camera_tilt_angle(0)
        self.set_camera_pan_angle(0)

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
        self.config.set("steering_offset", offset)
        self.steering_servo.offset(offset)
        self.steering_servo.angle(0)

    def set_camera_pan_offset(self, offset:float):
        ''' Set camera pan servo offset
        
        Args:
            offset (float): offset value, range from -20.0 to 20.0.
        '''
        self.config.set("camera_pan_offset", offset)
        self.camera_pan_servo.offset(offset)
        self.camera_pan_servo.angle(0)

    def set_camera_tilt_offset(self, offset:float):
        ''' Set camera tilt servo offset
        
        Args:
            offset (float): offset value, range from -20.0 to 20.0.
        '''
        self.config.set("camera_tilt_offset", offset)
        self.camera_tilt_servo.offset(offset)
        self.camera_tilt_servo.angle(0)

    def set_line_reference(self, value:list):
        ''' Set line reference
        
        Args:
            value (list): reference value, range from 0 to 1023.
        '''

        if isinstance(value, list) and len(value) == 3:
            self.line_reference = value
            self.grayscale.reference(self.line_reference)
            self.config.set("line_reference", self.line_reference)
        else:
            raise ValueError("grayscale reference must be a 1*3 list")

    def set_cliff_reference(self, value:list):
        ''' Set cliff reference

        Args:
            value (list): reference value, range from 0 to 1023.
        '''
        if isinstance(value, list) and len(value) == 3:
            self.cliff_reference = value
            self.config.set("cliff_reference", self.cliff_reference)
        else:
            raise ValueError("grayscale reference must be a 1*3 list")

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
        self.stop()
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

