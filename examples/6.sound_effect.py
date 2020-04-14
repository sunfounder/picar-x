#!/usr/bin/python3
from ezblock import TTS
from Music import *

count = None

__tts__ = TTS()


def forever():
  global count
  __tts__.say('Ready')
  count = 3
  for count2 in range(3):
    __tts__.say(count)
    count = count - 1
  sound_effect_play('Weapon_Continue_Shooting.wav',50)

if __name__ == "__main__":
    while True:
        forever()  