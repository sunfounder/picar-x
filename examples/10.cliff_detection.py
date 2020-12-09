#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from picarmini import dir_servo_angle_calibration
from picarmini import backward
from ezblock import delay
from picarmini import set_dir_servo_angle
from picarmini import forward
from ezblock import ADC



Ref = None
Left = None
Mid = None
Right = None

dir_servo_angle_calibration(0)
Ref = 110

adc_A0=ADC("A0")

adc_A1=ADC("A1")

adc_A2=ADC("A2")

"""Describe this function...
"""
def getGrayscaleValue():
  global Ref, Left, Mid, Right
  if (adc_A0.read()) <= Ref:
    Left = 1
  else:
    Left = 0
  if (adc_A1.read()) <= Ref:
    Mid = 1
  else:
    Mid = 0
  if (adc_A2.read()) <= Ref:
    Right = 1
  else:
    Right = 0
  return [Left, Mid, Right]


def forever():
  global Ref, Left, Mid, Right
  if getGrayscaleValue() != [0, 0, 0]:
    backward(50)
    delay(500)
    set_dir_servo_angle(30)
    forward(30)
    delay(500)
    set_dir_servo_angle(0)
  else:
    forward(20)

if __name__ == "__main__":
    while True:
        forever()  