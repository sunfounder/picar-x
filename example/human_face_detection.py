#!/usr/bin/python3
from vilib import Vilib
from picarmini import camera_servo1_angle_calibration
from picarmini import camera_servo2_angle_calibration
from ezblock import WiFi
from ezblock import Remote
from ezblock import mapping
from picarmini import set_camera_servo1_angle
from picarmini import set_camera_servo2_angle
from ezblock import print

Vilib.camera_start(True)
Vilib.human_detect_switch(True)
camera_servo1_angle_calibration(0)
camera_servo2_angle_calibration(0)
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')

__RM_OBJECT__ = Remote()


def forever():
  __RM_OBJECT__.read()
  set_camera_servo1_angle((mapping(__RM_OBJECT__.get_joystick_value("A", "X"), (-100), 100, (-45), 45)))
  set_camera_servo2_angle((mapping(__RM_OBJECT__.get_joystick_value("A", "Y"), (-100), 100, (-45), 45)))
  print("%s"%(''.join([str(x) for x in ['There are ', Vilib.human_detect_object(('number')), ' people']])))

if __name__ == "__main__":
    while True:
        forever()  