#!/usr/bin/python3
from ezblock import Pin
from ezblock import Ultrasonic
from ezblock import print
from ezblock import delay

distance = None

pin_D0=Pin("D0")

pin_D1=Pin("D1")


def forever():
  global distance
  distance = Ultrasonic(pin_D0, pin_D1).read()
  print("%s"%distance)
  delay(100)

if __name__ == "__main__":
    while True:
        forever()