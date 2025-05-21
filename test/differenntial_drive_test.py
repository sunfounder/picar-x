# Differential drive test

from picarx import PiCarX

car = PiCarX()

while True:
    car.forward(30)
    car.set_steering_angle(30)