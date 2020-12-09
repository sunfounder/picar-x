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
from picarmini import backward
from ezblock import delay
from ezblock import ADC



sta = None
value = None
direction = None
Ref = None
Left = None
Mid = None
Right = None
lastSta = None
currentSta = None

dir_servo_angle_calibration(0)
Ref = 950

"""Describe this function...
"""
def getDirection():
  global sta, value, direction, Ref, Left, Mid, Right, lastSta, currentSta
  value = getGrayscaleValue()
  if value == [0, 1, 0] or value == [1, 1, 1]:
    direction = 'FORWERD'
  elif value == [1, 0, 0] or value == [1, 1, 0]:
    direction = 'RIGHT'
  elif value == [0, 0, 1] or value == [0, 1, 1]:
    direction = 'LEFT'
  elif value == [0, 0, 0]:
    direction = 'OUT'
  return direction

"""Describe this function...
"""
def outHandle():
  global sta, value, direction, Ref, Left, Mid, Right, lastSta, currentSta
  if lastSta == 'LEFT':
    set_dir_servo_angle((-30))
    backward(10)
  elif lastSta == 'RIGHT':
    set_dir_servo_angle(30)
    backward(10)
  while True:
    currentSta = getDirection()
    if currentSta != lastSta:
      break
  delay(1)

adc_A0=ADC("A0")

adc_A1=ADC("A1")

adc_A2=ADC("A2")

"""Describe this function...
"""
def getGrayscaleValue():
  global sta, value, direction, Ref, Left, Mid, Right, lastSta, currentSta
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
  global sta, value, direction, Ref, Left, Mid, Right, lastSta, currentSta
  sta = getDirection()
  if sta != 'OUT':
    lastSta = sta
  if sta == 'FORWERD':
    set_dir_servo_angle(0)
    forward(10)
  elif sta == 'LEFT':
    set_dir_servo_angle(20)
    forward(10)
  elif sta == 'RIGHT':
    set_dir_servo_angle((-20))
    forward(10)
  elif sta == 'OUT':
    outHandle()

if __name__ == "__main__":
    while True:
        forever()  