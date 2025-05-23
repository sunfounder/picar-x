from robot_hat import Pin, ADC, PWM, Servo, fileDB
from robot_hat import Grayscale_Module, Ultrasonic, utils
from .music import Music, SoundFiles
from .utils import constrain, with_robot_hat_i2c_lock
import time

from time import sleep

class PiCarX(object):
    CONFIG = '/opt/picar-x/picar-x.conf'

    DEFAULT_LINE_REF = [1000, 1000, 1000]
    DEFAULT_CLIFF_REF = [500, 500, 500]

    DIR_MIN = -30
    DIR_MAX = 30
    CAM_PAN_MIN = -90
    CAM_PAN_MAX = 90
    CAM_TILT_MIN = -35
    CAM_TILT_MAX = 65

    PERIOD = 4095
    PRESCALER = 10
    TIMEOUT = 0.02

    LEFT_MOTOR = 1
    RIGHT_MOTOR = 0

    def __init__(
        self,
        servo_pins: list = ['P0', 'P1', 'P2'],
        motor_pins: list = ['D4', 'D5', 'P13', 'P12'],
        grayscale_pins: list = ['A0', 'A1', 'A2'],
        ultrasonic_pins: list = ['D2', 'D3'],  # 添加空格
        config: str = CONFIG,
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
        time.sleep(0.2)

        # --------- config_file ---------
        self.config_file = fileDB(config, 777, 1000)

        # --------- servos init ---------
        self.camera_pan_servo = Servo(servo_pins[0])
        self.camera_tilt_servo = Servo(servo_pins[1])   
        self.steering_servo = Servo(servo_pins[2])
        # get calibration values
        self.steering_offset = float(self.config_file.get("steering_offset", default_value=0))
        self.camera_pan_offset = float(self.config_file.get("camera_pan_offset", default_value=0))
        self.camera_tilt_offset = float(self.config_file.get("camera_tilt_offset", default_value=0))
        # set servos to init angle
        self.set_steering_angle(0)
        self.set_camera_pan_angle(0)
        self.set_camera_tilt_angle(0)

        # --------- motors init ---------
        self.left_rear_dir_pin = Pin(motor_pins[0])
        self.right_rear_dir_pin = Pin(motor_pins[1])
        self.left_rear_pwm_pin = PWM(motor_pins[2])
        self.right_rear_pwm_pin = PWM(motor_pins[3])
        self.motor_direction_pins = [self.left_rear_dir_pin, self.right_rear_dir_pin]
        self.motor_speed_pins = [self.left_rear_pwm_pin, self.right_rear_pwm_pin]
        # get calibration values
        self.motor_reverses = self.config_file.get("motor_reverses", default_value="[1, -1]")
        self.motor_reverses = [int(i.strip()) for i in self.motor_reverses.strip().strip("[]").split(",")]
        self.motor_power_offset = [0, 0]
        # init pwm
        for pin in self.motor_speed_pins:
            pin.period(self.PERIOD)
            pin.prescaler(self.PRESCALER)

        # --------- grayscale module init ---------
        adc0, adc1, adc2 = [ADC(pin) for pin in grayscale_pins]
        self.grayscale = Grayscale_Module(adc0, adc1, adc2, reference=None)
        # get reference
        self.line_reference = self.config_file.get("line_reference", default_value=str(self.DEFAULT_LINE_REF))
        self.line_reference = [float(i) for i in self.line_reference.strip().strip('[]').split(',')]
        self.cliff_reference = self.config_file.get("cliff_reference", default_value=str(self.DEFAULT_CLIFF_REF))
        self.cliff_reference = [float(i) for i in self.cliff_reference.strip().strip('[]').split(',')]
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

    @with_robot_hat_i2c_lock
    def set_motor_power(self, motor, power):
        ''' Set a single motor power

        Args:
            motor (int): motor index, 1 means left motor, 2 means right motor.
            power (int): power value, range from -100 to 100.
        '''
        power = constrain(power, -100, 100)
        motor -= 1
        if power >= 0:
            direction = 1 * self.motor_reverses[motor]
        elif power < 0:
            direction = -1 * self.motor_reverses[motor]
        power = abs(power)
        # print(f"direction: {direction}, power: {power}")
        if power != 0:
            power = int(power /2 ) + 50
        power = power - self.motor_power_offset[motor]

        if direction < 0:
            self.motor_direction_pins[motor].high()
            self.motor_speed_pins[motor].pulse_width_percent(power)
        else:
            self.motor_direction_pins[motor].low()
            self.motor_speed_pins[motor].pulse_width_percent(power)

    def set_motor_power_offset(self, value):
        ''' Set motor power offset to even the speed of the two motors.

        Args:
            value (int): offset value, range from -100 to 100.
        '''
        self.motor_power_offset = value
        if value < 0:
            self.motor_power_offset[0] = 0
            self.motor_power_offset[1] = abs(self.motor_power_offset)
        else:
            self.motor_power_offset[0] = abs(self.motor_power_offset)
            self.motor_power_offset[1] = 0

    def set_motor_reverse(self, motor, value):
        ''' Set if a motor is reversed.
        
        Args:
            motor (int): motor index, 1 means left motor, 2 means right motor.
            value (int): 1 means forward, -1 means reverse.
        '''      
        motor -= 1
        self.motor_reverses[motor] = value
        self.config_file.set("picarx_dir_motor", self.motor_reverses)

    @with_robot_hat_i2c_lock
    def set_steering_angle(self, value):
        ''' Set steering angle
        
        Args:
            value (int): angle value, range from -30 to 30.
        '''
        self.steering_angle = constrain(value, self.DIR_MIN, self.DIR_MAX)
        angle_value  = self.steering_angle + self.steering_offset
        self.steering_servo.angle(angle_value)

    @with_robot_hat_i2c_lock
    def set_camera_pan_angle(self, value):
        ''' Set camera pan servo angle
        
        Args:
            value (int): angle value, range from -90 to 90.
        '''
        value = constrain(value, self.CAM_PAN_MIN, self.CAM_PAN_MAX)
        self.camera_pan_servo.angle(-(value - self.camera_pan_offset))

    @with_robot_hat_i2c_lock
    def set_camera_tilt_angle(self, value):
        ''' Set camera tilt servo angle

        Args:
            value (int): angle value, range from -35 to 65.
        '''
        value = constrain(value, self.CAM_TILT_MIN, self.CAM_TILT_MAX)
        self.camera_tilt_servo.angle(-(value + self.camera_tilt_offset))

    def set_steering_offset(self, value):
        ''' Set steering offset
        
        Args:
            value (int): offset value, range from -30 to 30.
        '''
        self.steering_offset = value
        self.config_file.set("steering_offset", "%s"%value)
        self.set_steering_angle(0)

    def set_camera_pan_offset(self, value):
        ''' Set camera pan servo offset
        
        Args:
            value (int): offset value, range from -90 to 90.
        '''
        self.camera_pan_offset = value
        self.config_file.set("camera_pan_offset", "%s"%value)
        self.set_camera_pan_angle(0)

    def set_camera_tilt_offset(self, value):
        ''' Set camera tilt servo offset
        
        Args:
            value (int): offset value, range from -35 to 65.
        '''
        self.camera_tilt_offset = value
        self.config_file.set("camera_tilt_offset", "%s"%value)
        self.set_camera_tilt_angle(0)

    def set_motor_powers(self, power):
        ''' Set motor powers
        
        Args:
            power (int): power value, range from -100 to 100.
        '''
        self.set_motor_power(1, power)
        self.set_motor_power(2, power)

    def backward(self, power):
        ''' Backward
        
        param power: power
        type power: int'''
        self.set_motor_powers(-power)

    def forward(self, power):
        ''' Forward
        
        param power: power
        type power: int
        '''
        self.set_motor_powers(power)

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

    @with_robot_hat_i2c_lock
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

    @with_robot_hat_i2c_lock
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

if __name__ == "__main__":
    px = PiCarX()
    px.forward(50)
    time.sleep(1)
    px.stop()
