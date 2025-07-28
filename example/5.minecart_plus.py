'''
    Line Tracking program for Picar-X:

    Pay attention to modify the reference value of the grayscale module 
    according to the practical usage scenarios.
    Auto calibrate grayscale values:
        Please run ./calibration/grayscale_calibration.py
    Manual modification:
        Use the tracking: 
            px.set_line_reference([1400, 1400, 1400])
        The reference value be close to the middle of the line gray value
        and the background gray value.

'''
from turtle import position
from picarx.picarx import PiCarX
from picarx.utils import print_line_position
from time import sleep

car = PiCarX()

# Please run ./calibration/grayscale.py to calibrate grayscale values
# or manual modify reference value by follow code
# car.set_line_reference([1400, 1400, 1400])

POWER = 30

position = 0

def main():
    global position

    while True:
        data = car.get_grayscale_data()

        if car.is_on_line(data=data):
            position = car.get_line_position(data=data)
            print_line_position(position)
            steering_angle = position * 30
            car.set_steering_angle(steering_angle)
            car.forward(POWER)
        else:
            if position < 0:
                car.set_steering_angle(30)
                car.backward(10)
            else:
                car.set_steering_angle(-30)
                car.backward(10)
                while True:
                    if car.is_on_line():
                        break


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        car.reset()
        print("Stop and exit")
        sleep(0.1)
