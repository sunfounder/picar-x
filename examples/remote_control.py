#!/usr/bin/python3
from picarmini import dir_servo_angle_calibration
from ezblock import Remote
from picarmini import forward
from ezblock import mapping
from picarmini import set_dir_servo_angle

dir_servo_angle_calibration(0)

__RM_OBJECT__ = Remote()


def forever():
  __RM_OBJECT__.read()
  forward(__RM_OBJECT__.get_joystick_value("A", "Y"))
  set_dir_servo_angle((mapping(__RM_OBJECT__.get_joystick_value("A", "X"), (-100), 100, (-45), 45)))

if __name__ == "__main__":
    while True:
        forever()  