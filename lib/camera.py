from servo import Servo
from pwm import PWM

class Camera(object):
    def __init__(self, config_file) -> None:
        # Grab config file
        self.config_file = config_file

        # Setup camera pins
        self.camera_servo_pin1 = Servo(PWM('P0'))
        self.camera_servo_pin2 = Servo(PWM('P1'))

        # Setup camera calibration values
        self.cam_cal_value_1 = int(self.config_file.get("picarx_cam_pan_servo", default_value=0))
        self.cam_cal_value_2 = int(self.config_file.get("picarx_cam_tilt", default_value=0))

        # Set camera pins to calibrated values
        self.camera_servo_pin1.angle(self.cam_cal_value_1)
        self.camera_servo_pin2.angle(self.cam_cal_value_2)

    def write_camera_servo1_angle_calibration(self,value):
        self.cam_cal_value_1 = value
        self.config_file.set("picarx_cam_pan_servo", "%s"%value)

    def write_camera_servo2_angle_calibration(self,value):
        self.cam_cal_value_2 = value
        self.config_file.set("picarx_cam_tilt_servo", "%s"%value)

    def set_camera_pan_angle(self,value):
        self.camera_servo_pin1.angle(-1*(value + -1*self.cam_cal_value_1))

    def set_camera_tilt_angle(self,value):
        self.camera_servo_pin2.angle(-1*(value + -1*self.cam_cal_value_2))
