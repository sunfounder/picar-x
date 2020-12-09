#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from picarmini import dir_servo_angle_calibration
from picarmini import set_dir_servo_angle
from picarmini import forward
from picarmini import stop
from ezblock import ADC



value = None
direction = None
status = None
Ref = None
Left = None
Mid = None
Right = None

"""Describe this function...
"""
def getDirection():
  global value, direction, status, Ref, Left, Mid, Right
  value = getGrayscaleValue()
  if value == [0, 1, 0] or value == [1, 1, 1]:
    direction = 'FORWARD'
  elif value == [1, 0, 0] or value == [1, 1, 0]:
    direction = 'RIGHT'
  elif value == [0, 0, 1] or value == [0, 1, 1]:
    direction = 'LEFT'
  elif value == [0, 0, 0]:
    direction = 'OUT'
  return direction

dir_servo_angle_calibration(0)
Ref = 950

adc_A0=ADC("A0")

adc_A1=ADC("A1")

adc_A2=ADC("A2")

"""Describe this function...
"""
def getGrayscaleValue():
  global value, direction, status, Ref, Left, Mid, Right
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
  global value, direction, status, Ref, Left, Mid, Right
  status = getDirection()
  if status == 'FORWARD':
    set_dir_servo_angle(0)
    forward(10)
  elif status == 'LEFT':
    set_dir_servo_angle(20)
    forward(10)
  elif status == 'RIGHT':
    set_dir_servo_angle((-20))
    forward(10)
  elif status == 'OUT':
    stop()

if __name__ == "__main__":
    while True:
        forever()  