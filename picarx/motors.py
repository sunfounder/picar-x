
from robot_hat import Motor, Pin, PWM
import math

class Motors():
    LEFT_PWM = 'P13'
    LEFT_DIR = 'D4'
    RIGHT_PWM = 'P12'
    RIGHT_DIR = 'D5'

    # Minimum power to prevent the motor from not turning
    MIN_POWER = 20

    def __init__(self,
        left_pwm: PWM = LEFT_PWM,
        left_dir: Pin = LEFT_DIR,
        right_pwm: PWM = RIGHT_PWM,
        right_dir: Pin = RIGHT_DIR,
        left_reversed: bool = False,
        right_reversed: bool = False
    ):
        """ Initialize motors with robot_hat.motor.Motor

        Args:
            left_pwm (PWM, optional): left motor pwm pin. Defaults to LEFT_PWM.
            left_dir (Pin, optional): left motor dir pin. Defaults to LEFT_DIR.
            right_pwm (PWM, optional): right motor pwm pin. Defaults to RIGHT_PWM.
            right_dir (Pin, optional): right motor dir pin. Defaults to RIGHT_DIR.
            left_reversed (bool, optional): left motor is reversed or not. Defaults to False.
            right_reversed (bool, optional): right motor is reversed or not. Defaults to False.
        """
        self.left = Motor(PWM(left_pwm), Pin(left_dir), is_reversed=left_reversed, min_power=self.MIN_POWER)
        self.right = Motor(PWM(right_pwm), Pin(right_dir), is_reversed=right_reversed, min_power=self.MIN_POWER)
        self.left_reversed = left_reversed
        self.right_reversed = right_reversed
        self.power = 0
        self.wheel_base = 0
        self.track_width = 0
        self.differential_drive_enabled = False

    def init_differential_drive(self, wheel_base: float, track_width: float):
        """ Initialize differential drive for both motors

        Args:
            wheel_base (float): distance between the two wheels (mm)
            track_width (float): distance between the two wheels (mm)
        """
        self.wheel_base = wheel_base
        self.track_width = track_width
        self.differential_drive_enabled = True

    def set_left_reverse(self, is_reversed: bool):
        """ Set left motor reverse
        
        Args:
            is_reversed (bool): True for reverse, False for forward
        """
        self.left.set_is_reverse(is_reversed)
        self.left_reversed = is_reversed

    def set_right_reverse(self, is_reversed: bool):
        """ Set right motor reverse

        Args:
            is_reversed (bool): True for reverse, False for forward
        """
        self.right.set_is_reverse(is_reversed)
        self.right_reversed = is_reversed

    def set_power(self, power: float, angle: float = 0):
        """ Set power for both motors
        
        Args:
            power (float): power for both motors (-100.0~100.0)
        """
        if self.differential_drive_enabled:
            left, right = self.differential_drive(power, angle)
        else:
            left = right = power
        self.left.power(left)
        self.right.power(right)
        self.power = power

    def differential_drive(self, angle, power):
        ''' calculate the differential drive power of the two motors.

        Args:
            angle (float): angle of the turn (-180.0~180.0)
            power (float): power of the turn (-100.0~100.0)

        Returns:
            tuple: left power, right power (-100.0~100.0)
        '''
        # if go straight, both motors have the same power
        if angle == 0:
            return power, power
        
        # calculate the radius of the turn
        steering_angle_rad = angle / 180 * math.pi
        radius = self.wheel_base / math.tan(steering_angle_rad)

        # calculate the radius of the left and right wheel
        left_radius = radius - self.track_width / 2
        right_radius = radius + self.track_width / 2

        # calculate the ratio of the left and right wheel
        ratio = left_radius / right_radius

        # Check which is the outer and which is the inner wheel
        if ratio > 1: # turn left, left wheel is inner wheel
            left_power = power
            right_power = power / ratio
        else: # turn right, right wheel is inner wheel
            left_power = power * ratio
            right_power = power
        
        # constraint the power to -100 ~ 100
        max_power = max(abs(left_power), abs(right_power))
        if max_power > 100:
            scale = 100 / max_power
            left_power *= scale
            right_power *= scale
        return left_power, right_power
