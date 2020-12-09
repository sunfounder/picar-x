#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
from ezblock import ADC
from ezblock import print




my_3ch = None

adc_A0=ADC("A0")

adc_A1=ADC("A1")

adc_A2=ADC("A2")


def forever():
  global my_3ch
  my_3ch = [adc_A0.read(), adc_A1.read(), adc_A2.read()]
  print("%s"%my_3ch)

if __name__ == "__main__":
    while True:
        forever()  