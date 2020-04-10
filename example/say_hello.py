#!/usr/bin/python3
from ezblock import Remote
from vilib import Vilib
from picarmini import set_camera_servo2_angle
from ezblock import delay
from ezblock import TTS
from picarmini import forward
from ezblock import mapping
from picarmini import set_dir_servo_angle
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import WiFi

__RM_OBJECT__ = Remote()

__tts__ = TTS()

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')


def forever():
  __RM_OBJECT__.read()
  if (Vilib.human_detect_object(('number'))) >= 1:
    set_camera_servo2_angle(30)
    delay(150)
    set_camera_servo2_angle((-30))
    delay(150)
    set_camera_servo2_angle(0)
    delay(150)
    __tts__.say('Hello,nice to meet you!')
  forward(__RM_OBJECT__.get_joystick_value("A", "Y"))
  set_dir_servo_angle((mapping(__RM_OBJECT__.get_joystick_value("A", "X"), (-100), 100, (-45), 45)))

if __name__ == "__main__":
    while True:
        forever()  

