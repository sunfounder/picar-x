#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from Music import *

background_music('spry.mp3')

def forever():
  music_set_volume(50)

if __name__ == "__main__":
    while True:
        forever()  