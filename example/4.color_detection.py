#!/usr/bin/python3
from vilib import Vilib
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import WiFi

Vilib.camera_start(True)
Vilib.color_detect_switch(True)
Vilib.detect_color_name('red')
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')


def forever():
  pass

if __name__ == "__main__":
    while True:
        forever()
