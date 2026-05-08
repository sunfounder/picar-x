from .get_hat import is_fusion_hat
if is_fusion_hat:
    from fusion_hat.motor import Motor
else:
    from robot_hat.motor import Motor

import math

class Motors():
    LEFT_MOTOR = 'M2'
    RIGHT_MOTOR = 'M1'

    # Minimum power to prevent the motor from not turning
    MIN_POWER = 30
    # Maximum power
    MAX_POWER = 100

    def __init__(self,
        left_motor: str = LEFT_MOTOR,
        right_motor: str = RIGHT_MOTOR,
        left_reversed: bool = False,
        right_reversed: bool = False
    ):
        """ Initialize motors with fusion_hat.motor.Motor

        Args:
            left_motor (str, optional): left motor. Defaults to LEFT_MOTOR.
            right_motor (str, optional): right motor. Defaults to RIGHT_MOTOR.
            left_reversed (bool, optional): left motor is reversed or not. Defaults to False.
            right_reversed (bool, optional): right motor is reversed or not. Defaults to False.
        """
        self.left = Motor(left_motor, min=self.MIN_POWER, max=self.MAX_POWER)
        self.right = Motor(right_motor, min=self.MIN_POWER, max=self.MAX_POWER)
        self.power = 0
        self.wheel_base = 0
        self.track_width = 0
        self.differential_drive_enabled = False
        self.set_left_reverse(left_reversed)
        self.set_right_reverse(right_reversed)

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
        # Filp the direction as the motor is mounted in reverse
        is_reversed = not is_reversed
        self.left.set_is_reverse(is_reversed)
        self.left_reversed = is_reversed

    def set_right_reverse(self, is_reversed: bool):
        """ Set right motor reverse

        Args:
            is_reversed (bool): True for reverse, False for forward
        """
        # Filp the direction as the motor is mounted in reverse
        is_reversed = not is_reversed
        self.right.set_is_reverse(is_reversed)
        self.right_reversed = is_reversed

    def set_power(self, power: float, angle: float = 0):
        """ Set power for both motors
        
        Args:
            power (float): power for both motors (-100.0~100.0)
        """
        if self.differential_drive_enabled:
            left, right = self.differential_drive(angle, power)
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
        right_radius = radius - self.track_width / 2
        left_radius = radius + self.track_width / 2

        # calculate the ratio of the left and right wheel
        ratio = right_radius / left_radius

        # Check which is the outer and which is the inner wheel
        if ratio > 1: # turn left, left wheel is inner wheel
            left_power = power / ratio
            right_power = power
        else: # turn right, right wheel is inner wheel
            left_power = power
            right_power = power * ratio
        
        # constraint the power to -100 ~ 100
        max_power = max(abs(left_power), abs(right_power))
        if max_power > 100:
            scale = 100 / max_power
            left_power *= scale
            right_power *= scale
        return left_power, right_power
