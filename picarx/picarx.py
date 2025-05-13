from robot_hat import Pin, ADC, PWM, Servo, fileDB
from robot_hat import Grayscale_Module, Ultrasonic, utils
import time
import os


def constrain(x, min_val, max_val):
    '''
    Constrains value to be within a range.
    '''
    return max(min_val, min(max_val, x))

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

    # servo_pins: camera_pan_servo, camera_tilt_servo, direction_servo
    # motor_pins: left_swicth, right_swicth, left_pwm, right_pwm
    # grayscale_pins: 3 adc channels
    # ultrasonic_pins: trig, echo2
    # config: path of config file
    def __init__(self, 
                servo_pins:list=['P0', 'P1', 'P2'], 
                motor_pins:list=['D4', 'D5', 'P13', 'P12'],
                grayscale_pins:list=['A0', 'A1', 'A2'],
                ultrasonic_pins:list=['D2','D3'],
                config:str=CONFIG,
                ):

        # reset robot_hat
        utils.reset_mcu()
        time.sleep(0.2)

        # --------- config_file ---------
        self.config_file = fileDB(config, 777, os.getlogin())

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
        self.cali_dir_value = self.config_file.get("picarx_dir_motor", default_value="[1, 1]")
        self.cali_dir_value = [int(i.strip()) for i in self.cali_dir_value.strip().strip("[]").split(",")]
        self.cali_speed_value = [0, 0]
        self.steering_angle = 0
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

    def set_motor_power(self, motor, power):
        ''' set motor power
        
        param motor: motor index, 1 means left motor, 2 means right motor
        type motor: int
        param power: power
        type power: int      
        '''
        power = constrain(power, -100, 100)
        motor -= 1
        if power >= 0:
            direction = 1 * self.cali_dir_value[motor]
        elif power < 0:
            direction = -1 * self.cali_dir_value[motor]
        power = abs(power)
        # print(f"direction: {direction}, power: {power}")
        if power != 0:
            power = int(power /2 ) + 50
        power = power - self.cali_speed_value[motor]
        if direction < 0:
            self.motor_direction_pins[motor].high()
            self.motor_speed_pins[motor].pulse_width_percent(power)
        else:
            self.motor_direction_pins[motor].low()
            self.motor_speed_pins[motor].pulse_width_percent(power)

    def set_motor_power_offset(self, value):
        ''' set motor power offset'''
        self.cali_speed_value = value
        if value < 0:
            self.cali_speed_value[0] = 0
            self.cali_speed_value[1] = abs(self.cali_speed_value)
        else:
            self.cali_speed_value[0] = abs(self.cali_speed_value)
            self.cali_speed_value[1] = 0

    def motor_direction_calibrate(self, motor, value):
        ''' set motor direction calibration value
        
        param motor: motor index, 1 means left motor, 2 means right motor
        type motor: int
        param value: speed
        type value: int
        '''      
        motor -= 1
        if value == 1:
            self.cali_dir_value[motor] = 1
        elif value == -1:
            self.cali_dir_value[motor] = -1
        self.config_file.set("picarx_dir_motor", self.cali_dir_value)

    def set_steering_angle(self, value):
        ''' set steering angle'''
        self.steering_angle = constrain(value, self.DIR_MIN, self.DIR_MAX)
        angle_value  = self.steering_angle + self.steering_offset
        self.steering_servo.angle(angle_value)

    def set_camera_pan_angle(self, value):
        ''' set camera pan servo angle'''
        value = constrain(value, self.CAM_PAN_MIN, self.CAM_PAN_MAX)
        self.camera_pan_servo.angle(-(value - self.camera_pan_offset))

    def set_camera_tilt_angle(self, value):
        value = constrain(value, self.CAM_TILT_MIN, self.CAM_TILT_MAX)
        self.camera_tilt_servo.angle(-(value + self.camera_tilt_offset))

    def set_steering_offset(self, value):
        ''' set steering offset'''
        self.steering_offset = value
        self.config_file.set("steering_offset", "%s"%value)
        self.set_steering_angle(0)

    def set_camera_pan_offset(self, value):
        ''' set camera pan servo offset'''
        self.camera_pan_offset = value
        self.config_file.set("camera_pan_offset", "%s"%value)
        self.set_camera_pan_angle(0)

    def set_camera_tilt_offset(self, value):
        ''' set camera tilt servo offset'''
        self.camera_tilt_offset = value
        self.config_file.set("camera_tilt_offset", "%s"%value)
        self.set_camera_tilt_angle(0)

    def set_motor_powers(self, left_speed, right_speed):
        ''' set motor powers'''
        self.set_motor_power(1, left_speed)
        self.set_motor_power(2, right_speed)

    def backward(self, speed):
        ''' backward '''
        current_angle = self.steering_angle
        if current_angle != 0:
            abs_current_angle = abs(current_angle)
            if abs_current_angle > self.DIR_MAX:
                abs_current_angle = self.DIR_MAX
            power_scale = (100 - abs_current_angle) / 100.0 
            if (current_angle / abs_current_angle) > 0:
                self.set_motor_powers(1*speed, speed * power_scale)
            else:
                self.set_motor_powers(1*speed * power_scale, speed)
        else:
            self.set_motor_powers(1*speed, speed)

    def forward(self, speed):
        ''' forward '''
        current_angle = self.steering_angle
        if current_angle != 0:
            abs_current_angle = abs(current_angle)
            if abs_current_angle > self.DIR_MAX:
                abs_current_angle = self.DIR_MAX
            power_scale = (100 - abs_current_angle) / 100.0
            if (current_angle / abs_current_angle) > 0:
                self.set_motor_powers(speed * power_scale, speed) 
            else:
                self.set_motor_powers(speed, speed * power_scale)
        else:
            self.set_motor_powers(speed, speed)



    def stop(self):
        '''
        Execute twice to make sure it stops
        '''
        for _ in range(2):
            self.motor_speed_pins[0].pulse_width_percent(0)
            self.motor_speed_pins[1].pulse_width_percent(0)
            time.sleep(0.002)

    def get_distance(self):
        return self.ultrasonic.read()

    def set_grayscale_reference(self, value):
        if isinstance(value, list) and len(value) == 3:
            self.line_reference = value
            self.grayscale.reference(self.line_reference)
            self.config_file.set("line_reference", self.line_reference)
        else:
            raise ValueError("grayscale reference must be a 1*3 list")

    def get_grayscale_data(self):
        return list.copy(self.grayscale.read())

    def get_line_status(self,gm_val_list):
        return self.grayscale.read_status(gm_val_list)

    def set_line_reference(self, value):
        self.set_grayscale_reference(value)

    def get_cliff_status(self,gm_val_list):
        for i in range(0,3):
            if gm_val_list[i]<=self.cliff_reference[i]:
                return True
        return False

    def set_cliff_reference(self, value):
        if isinstance(value, list) and len(value) == 3:
            self.cliff_reference = value
            self.config_file.set("cliff_reference", self.cliff_reference)
        else:
            raise ValueError("grayscale reference must be a 1*3 list")

    def reset(self):
        self.stop()
        self.set_steering_angle(0)
        self.set_camera_tilt_angle(0)
        self.set_camera_pan_angle(0)


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
            direction = 1 * self.cali_dir_value[motor]
        elif speed < 0:
            direction = -1 * self.cali_dir_value[motor]
        speed = abs(speed)
        # print(f"direction: {direction}, speed: {speed}")
        if speed != 0:
            speed = int(speed /2 ) + 50
        speed = speed - self.cali_speed_value[motor]
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


if __name__ == "__main__":
    px = PiCarX()
    px.forward(50)
    time.sleep(1)
    px.stop()
