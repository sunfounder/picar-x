import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import atexit
import numpy as np
import os
from servo import Servo
from pwm import PWM

# Setup display variable so cv2.imshow doesn't throw errors
os.environ['DISPLAY'] = 0

class Camera(object):
    def __init__(self, config_file) -> None:
        # Grab config file
        self.config_file = config_file

        # Setup servo pins
        self.camera_servo_pin1 = Servo(PWM('P0'))
        self.camera_servo_pin2 = Servo(PWM('P1'))

        # Setup servo calibration values
        self.cam_cal_value_1 = int(self.config_file.get("picarx_cam_pan_servo", default_value=0))
        self.cam_cal_value_2 = int(self.config_file.get("picarx_cam_tilt", default_value=0))

        # Set servo pins to calibrated values
        self.camera_servo_pin1.angle(self.cam_cal_value_1)
        self.camera_servo_pin2.angle(self.cam_cal_value_2)

        # Setup picamera
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 24
        self.raw_capture = PiRGBArray(self.camera, size=self.camera.resolution)

        atexit.register(self.cleanup())

    def write_camera_servo1_angle_calibration(self,value):
        self.cam_cal_value_1 = value
        self.config_file.set("picarx_cam_pan_servo", "%s"%value)

    def write_camera_servo2_angle_calibration(self,value):
        self.cam_cal_value_2 = value
        self.config_file.set("picarx_cam_tilt_servo", "%s"%value)

    def set_pan_angle(self,value):
        self.camera_servo_pin1.angle(-1*(value + -1*self.cam_cal_value_1))

    def set_tilt_angle(self,value):
        self.camera_servo_pin2.angle(-1*(value + -1*self.cam_cal_value_2))

    def control_based_on_camera(self, control_func, display_img: bool = False)->None:
        # control_func is the control function that will take in np array of current image
        # and somehow control the steering angle based on just that np array as input
        # All parameters must be contained within the control_func
        # Control func must return a boolean value where True indicates that
        # it's time for the control loop to be shutdown
        for frame in self.camera.capture_continuous(self.raw_capture, format="bgr", use_video_port=True):
            img = frame.array
            if display_img:
                cv2.imshow(img)
            if control_func():
                break

    def get_camera_img(self)->np.array:
        # Grab latest frame from continuous camera stream
        *_, img = self.camera.capture_continuous(self.raw_capture, format="bgr", use_video_port=True)
        # Release cache (not actually sure why this is necessary)
        self.raw_capture.truncate(0)
        return img

    def display(self, img: np.array)->None:
        cv2.imshow("Display", img)

    def cleanup(self)->None:
        self.camera.close()