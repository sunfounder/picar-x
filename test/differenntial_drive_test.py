# Differential drive test

from picarx.picarx import PiCarX
from time import sleep


# print("Differential drive disabled")
# car = PiCarX(enable_differential_drive=False)

print("Differential drive enabled")
car = PiCarX()

car.forward(30)
car.set_steering_angle(30)
sleep(5)

car.set_steering_angle(0)
car.stop()

