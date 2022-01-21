import logging
from servo import Servo
from pwm import PWM
from pin import Pin

class DriveTrain(object):
    PERIOD = 4095
    PRESCALER = 10

    def __init__(self, config_file) -> None:
        # Grab config file
        self.config_file = config_file

        # Setup steering servo
        self.steer_cal_value = int(self.config_file.get("picarx_steer_servo", default_value=0))
        self.steer_servo_pin = Servo(PWM('P2'))
        self.steer_servo_pin.angle(self.steer_cal_value)

        # Setup rear motors
        self.left_rear_pwm_pin = PWM("P13")
        self.right_rear_pwm_pin = PWM("P12")
        self.left_rear_dir_pin = Pin("D4")
        self.right_rear_dir_pin = Pin("D5")
        self.motor_direction_pins = [self.left_rear_dir_pin, self.right_rear_dir_pin]
        self.motor_speed_pins = [self.left_rear_pwm_pin, self.right_rear_pwm_pin]
        for pin in self.motor_speed_pins:
            pin.period(self.PERIOD)
            pin.prescaler(self.PRESCALER)
        # Setup variables to write motor calibration variables to config file later on
        self.cali_dir_value = self.config_file.get("picarx_dir_motor", default_value="[1,1]")
        self.cali_dir_value = [int(i.strip()) for i in self.cali_dir_value.strip("[]").split(",")]

        # Setup variables for tracking angle and speed
        self.steer_current_angle = 0
        self.current_speed = 0

    def _set_motor_speed(self, motor, speed):
        """ Set the speed of specified rear motor
        """
        motor -= 1
        # Set direction
        if speed < 0:
            self.motor_direction_pins[motor].high()
        else:
            self.motor_direction_pins[motor].low()
        # Set speed
        self.motor_speed_pins[motor].pulse_width_percent(abs(speed))

    def _set_steer_servo_angle(self, value):
        """ Set the angle of the steering servo
        """
        self.steer_current_angle = value
        angle_value  = value + self.steer_cal_value
        self.steer_servo_pin.angle(angle_value)

    def _backward(self, speed):
        """ Set rear wheels speed in backward direction with
        differential compensation
        """
        current_angle = self.steer_current_angle
        if current_angle != 0:
            abs_current_angle = abs(current_angle)
            if abs_current_angle > 40:
                abs_current_angle = 40
            power_scale = (100 - abs_current_angle) / 100.0
            if (current_angle / abs_current_angle) > 0:
                self.set_motor_speed(1, -1*speed)
                self.set_motor_speed(2, speed * power_scale)
            else:
                self.set_motor_speed(1, -1*speed * power_scale)
                self.set_motor_speed(2, speed )
        else:
            self.set_motor_speed(1, -1*speed)
            self.set_motor_speed(2, speed)

    def _forward(self, speed):
        """ Set rear wheels speed in forward direction with
        differential compensation
        """
        current_angle = self.steer_current_angle
        if current_angle != 0:
            abs_current_angle = abs(current_angle)
            if abs_current_angle > 40:
                abs_current_angle = 40
            power_scale = (100 - abs_current_angle) / 100.0
            if (current_angle / abs_current_angle) > 0:
                self.set_motor_speed(1, speed)
                self.set_motor_speed(2, -1*speed * power_scale)
            else:
                self.set_motor_speed(1, speed * power_scale)
                self.set_motor_speed(2, -1*speed )
        else:
            self.set_motor_speed(1, speed)
            self.set_motor_speed(2, -1*speed)

    def write_motor_dir_calibration(self, motor: int, value: int)->None:
        """ Write new motor calibration value out to config file
        for rear motor direction
        """
        # 0: positive direction
        # 1: negative direction
        motor -= 1
        if value == 1:
            self.cali_dir_value[motor] = -1 * self.cali_dir_value[motor]
        self.config_file.set("picarx_dir_motor", self.cali_dir_value)

    def write_steer_servo_calibration(self, value: int)->None:
        """ Write new steering servo calibration value out to config file
        """
        self.steer_cal_value = value
        self.config_file.set("picarx_steer_servo", "%s"%value)

    def stop(self)->None:
        """ Stop the rear motors
        """
        self.set_motor_speed(1, 0)
        self.set_motor_speed(2, 0)

    def set_angle(self, angle: int)->None:
        """ Set angle for steering servo
        """
        # Enforce angle boundaries
        max_angle = 30
        if angle > max_angle:
            logging.warning(f"Requested steering angle ({angle}) greater than max angle ({max_angle}). Setting steering angle to max angle.")
            angle = max_angle
        elif angle < -max_angle:
            logging.warning(f"Requested steering angle ({angle}) lower than min angle ({max_angle}). Setting steering angle to min angle.")
            angle = -max_angle

        # Send steering command to drivetrain
        self._set_steer_servo_angle(angle)
        if self.current_speed >= 0:
            self._forward(self.current_speed)
        else:
            self._backward(abs(self.current_speed))

    def set_speed(self, speed: int)->None:
        """ Set speed for rear wheels
        """
        # Enforce speed boundaries
        max_speed = 100
        if speed > max_speed:
            logging.warning(f"Requested speed ({speed}) greater than max speed ({max_speed}). Set speed to max speed.")
            speed = max_speed
        elif speed < -max_speed:
            logging.warning(f"Requested speed ({speed}) lower than min speed ({-max_speed}). Set speed to min speed.")
            speed = -max_speed

        # Send speed command to drivetrain
        self.current_speed = speed
        if self.current_speed >= 0:
            self._forward(speed)
        else:
            self._backward(abs(speed))
