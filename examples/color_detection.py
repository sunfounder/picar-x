#!/usr/bin/python3
from vilib import Vilib
from ezblock import WiFi

Vilib.camera_start(True)
Vilib.color_detect_switch(True)
Vilib.detect_color_name('red')
WiFi().write('CN', 'MakerStarsHall', 'sunfounder')


def forever():
  pass

if __name__ == "__main__":
    while True:
        forever()
