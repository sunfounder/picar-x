#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from vilib import Vilib
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import WiFi
from ezblock import print

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')


def forever():
  print("%s"%(''.join([str(x) for x in ['There are ', Vilib.human_detect_object('number'), ' people']])))

if __name__ == "__main__":
    while True:
        forever()  