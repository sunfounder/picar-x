#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from vilib import Vilib
from picarmini import dir_servo_angle_calibration
from picarmini import set_camera_servo2_angle
from ezblock import delay
from ezblock import TTS
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import WiFi


__tts__ = TTS()

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
dir_servo_angle_calibration(0)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')

def forever():
  if (Vilib.human_detect_object(('number'))) >= 1:
    set_camera_servo2_angle(30)
    delay(150)
    set_camera_servo2_angle((-30))
    delay(150)
    set_camera_servo2_angle(0)
    delay(150)
    __tts__.say('Hello,nice to meet you!')

if __name__ == "__main__":
    while True:
        forever()  

