#!/usr/bin/python3
from Music import *
from ezblock import Remote

background_music('spry.mp3')

__RM_OBJECT__ = Remote()


def forever():
  __RM_OBJECT__.read()
  music_set_volume(__RM_OBJECT__.get_slider_value("A"))

if __name__ == "__main__":
    while True:
        forever()  