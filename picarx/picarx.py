from robot_hat import Pin, ADC, Servo
from robot_hat import Grayscale_Module, Ultrasonic, utils
from .motors import Motors
from .music import Music, SoundFiles
from .utils import Config, constrain
import os
import json

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
        grayscale_pins: list = ['A0', 'A1', 'A2'],
        motor_pins: list = ['P13', 'D4', 'P12', 'D5'],
        ultrasonic_pins: list = ['D2', 'D3'],  # 添加空格
        config_file: str = CONFIG,
    ):
        '''
        Initializes the PiCarX object.

        param servo_pins: list of servo pins. camera_pan_servo, camera_tilt_servo, direction_servo, Default is ['P0', 'P1', 'P2'].
        type servo_pins: list of str
        param motor_pins: list of motor pins. left_swicth, right_swicth, left_pwm, right_pwm, Default is ['D4', 'D5', 'P13', 'P12'].
        type motor_pins: list of str
        param grayscale_pins: list of grayscale pins. Default is ['A0', 'A1', 'A2'].
        type grayscale_pins: list of str
        param ultrasonic_pins: list of ultrasonic pins. trig, echo, Default is ['D2','D3'].
        type ultrasonic_pins: list of str
        param config_file: path of config_file file. Default is '/opt/picar-x/picar-x.conf'.
        type config_file: str
        '''
        # reset robot_hat
        utils.reset_mcu()
        sleep(0.2)

        # --------- config_file ---------
        self.config = Config(config_file)

        # --------- servos init ---------
        # get calibration values
        steering_offset = self.config.get("steering_offset", default_value=0.0)
        camera_pan_offset = self.config.get("camera_pan_offset", default_value=0.0)
        camera_tilt_offset = self.config.get("camera_tilt_offset", default_value=0.0)
        self.camera_pan_servo = Servo(servo_pins[0], offset=camera_pan_offset)
        self.camera_tilt_servo = Servo(servo_pins[1], offset=camera_tilt_offset)   
        self.steering_servo = Servo(servo_pins[2], offset=steering_offset)
        # set servos to init angle
        self.set_steering_angle(0)
        self.set_camera_pan_angle(0)
        self.set_camera_tilt_angle(0)

        # --------- motors init ---------
        left_motor_reversed = self.config.get("left_motor_reversed", default_value=False)
        right_motor_reversed = self.config.get("right_motor_reversed", default_value=True)
        self.motors = Motors(*motor_pins, left_reversed=left_motor_reversed, right_reversed=right_motor_reversed)
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

    def set_steering_angle(self, angle):
        ''' Set steering angle
        
        param value: angle value
        type value: int
        '''
        angle = constrain(angle, self.DIR_MIN, self.DIR_MAX)
        self.steering_servo.angle(angle)
        self.motors.set_power(self.motors.power, angle)

    def set_camera_pan_angle(self, angle):
        ''' Set camera pan servo angle
        
        param angle: angle angle
        type angle: int
        '''
        angle = constrain(angle, self.CAM_PAN_MIN, self.CAM_PAN_MAX)
        self.camera_pan_servo.angle(angle)

    def set_camera_tilt_angle(self, angle):
        ''' Set camera tilt servo angle

        param angle: angle angle
        type angle: int
        '''
        angle = constrain(angle, self.CAM_TILT_MIN, self.CAM_TILT_MAX)
        self.camera_tilt_servo.angle(angle)

    # Calibration functions
    def set_motor_reverse(self, motor, value):
        ''' Set if a motor is reversed.
        
        param motor: motor index, 1 means left motor, 2 means right motor
        type motor: int
        param value: speed
        type value: int
        '''
        if motor == 1:
            self.motors.set_left_reverse(value)
            self.config.set("left_motor_reversed", value)
        elif motor == 2:
            self.motors.set_right_reverse(value)
            self.config.set("right_motor_reversed", value)

    def set_steering_offset(self, offset):
        ''' Set steering offset
        
        param offset: offset offset
        type offset: int
        '''
        self.config.set("steering_offset", offset)
        self.steering_servo.offset(offset)

    def set_camera_pan_offset(self, value):
        ''' Set camera pan servo offset
        
        param value: offset value
        type value: int
        '''
        self.config_file.set("camera_pan_offset", value)
        self.camera_pan_servo.offset(value)

    def set_camera_tilt_offset(self, value):
        ''' Set camera tilt servo offset
        
        param value: offset value
        type value: int
        '''
        self.config_file.set("camera_tilt_offset", "%s"%value)
        self.camera_tilt_servo.offset(value)

    def backward(self, power):
        ''' Backward
        
        param power: power
        type power: int'''
        self.motors.set_power(-power, self.steering_servo.angle())

    def forward(self, power):
        ''' Forward
        
        param power: power
        type power: int
        '''
        self.motors.set_power(power, self.steering_servo.angle())

    def stop(self):
        ''' Stop motors '''
        self.set_motor_powers(0)

    def get_distance(self):
        ''' Get distance from ultrasonic sensor '''
        return self.ultrasonic.read()

    def set_grayscale_reference(self, value):
        ''' Set grayscale reference

        param value: reference value
        type value: list
        '''
        if isinstance(value, list) and len(value) == 3:
            self.line_reference = value
            self.grayscale.reference(self.line_reference)
            self.config_file.set("line_reference", self.line_reference)
        else:
            raise ValueError("grayscale reference must be a 1*3 list")

    def get_grayscale_data(self):
        ''' Get grayscale data '''
        return list.copy(self.grayscale.read())

    def get_line_status(self, gm_val_list):
        ''' Get line status
        
        param gm_val_list: grayscale value list
        type gm_val_list: list
        '''
        return self.grayscale.read_status(gm_val_list)

    def set_line_reference(self, value):
        ''' Set line reference
        
        param value: reference value
        type value: list
        '''
        self.set_grayscale_reference(value)

    def get_cliff_status(self,gm_val_list):
        ''' Get cliff status

        param gm_val_list: grayscale value list
        type gm_val_list: list
        '''
        for i in range(0,3):
            if gm_val_list[i]<=self.cliff_reference[i]:
                return True
        return False

    def set_cliff_reference(self, value):
        ''' Set cliff reference

        param value: reference value
        type value: list
        '''
        if isinstance(value, list) and len(value) == 3:
            self.cliff_reference = value
            self.config_file.set("cliff_reference", self.cliff_reference)
        else:
            raise ValueError("grayscale reference must be a 1*3 list")

    def get_battery_voltage(self):
        ''' Get battery voltage '''
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

    def start_engine(music):
        ''' Start engine '''
        self.music.play_sound_background(SoundFiles.START_ENGINE, volume=50)

    # DEPRECATED function
    
    def set_motor_speed(self, motor, speed):
        ''' DEPRECATED
        set motor speed
        
        param motor: motor index, 1 means left motor, 2 means right motor
        type motor: int
        param speed: speed
        type speed: int      
        '''
        speed = constrain(speed, -100, 100)
        motor -= 1
        if speed >= 0:
            direction = 1 * self.motor_reverses[motor]
        elif speed < 0:
            direction = -1 * self.motor_reverses[motor]
        speed = abs(speed)
        # print(f"direction: {direction}, speed: {speed}")
        if speed != 0:
            speed = int(speed /2 ) + 50
        speed = speed - self.motor_power_offset[motor]
        if direction < 0:
            self.motor_direction_pins[motor].high()
            self.motor_speed_pins[motor].pulse_width_percent(speed)
        else:
            self.motor_direction_pins[motor].low()
            self.motor_speed_pins[motor].pulse_width_percent(speed)

    def set_dir_servo_angle(self, value):
        ''' DEPRECATED set direction servo angle'''
        self.set_steering_angle(value)

    def dir_servo_calibrate(self, value):
        ''' DEPRECATED set direction servo calibration value'''
        self.set_steering_offset(value)

    def cam_pan_servo_calibrate(self, value):
        ''' DEPRECATED set camera pan servo calibration value'''
        self.set_camera_pan_offset(value)

    def cam_tilt_servo_calibrate(self, value):
        ''' DEPRECATED set camera tilt servo calibration value'''
        self.set_camera_tilt_offset(value)

    def set_cam_pan_angle(self, value):
        ''' DEPRECATED set camera pan servo angle'''
        self.set_camera_pan_angle(value)

    def set_cam_tilt_angle(self,value):
        ''' DEPRECATED set camera tilt servo angle'''
        self.set_camera_tilt_angle(value)

    def set_power(self, speed):
        ''' DEPRECATED set motor power'''
        self.set_motor_powers(speed, speed)

    def motor_speed_calibration(self, value):
        ''' DEPRECATED set motor speed calibration value'''
        self.set_motor_power_offset(value)

    def motor_direction_calibrate(self, motor, value):
        ''' DEPRECATED set motor direction calibration value'''
        self.set_motor_reverse(motor, value)

