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
from picarx import PiCarX
from time import sleep

car = PiCarX()

# Please run ./calibration/grayscale_calibration.py to Auto calibrate grayscale values
# or manual modify reference value by follow code
# px.set_line_reference([1400, 1400, 1400])

POWER = 30
BIG_TURNING_ANGLE = 30
SMALL_TURNING_ANGLE = 15

direction = NotImplementedError
offset = 20
last_state = "stop"

def get_direction():
    data = car.get_grayscale_data()
    status = car.get_line_status(data)
    if status == [0, 0, 0]:
        return 'stop'
    elif status == [0, 1, 0]:
        return 'forward'
    elif status == [1, 0, 0]:
        return 'left'
    elif status == [1, 1, 0]:
        return 'little_left'
    elif status == [0, 0, 1]:
        return 'right'
    elif status == [0, 1, 1]:
        return 'little_right'

def outHandle():
    print("Run out of line")
    if direction in ['left', 'little_left']:
        print("Turn right")
        car.set_steering_angle(30)
        car.backward(10)
    elif direction in ['right', 'little_right']:
        print("Turn left")
        car.set_steering_angle(-30)
        car.backward(10)
    while True:
        new_direction = get_direction()
        if new_direction != direction:
            break
    print("Get back to line")

def main():
    while True:
        direction = get_direction()
        print(f"Direction: {direction}")

        if direction != "stop":
            direction = direction
        if direction == 'forward':
            car.set_steering_angle(0)
            car.forward(POWER) 
        elif direction == 'left':
            car.set_steering_angle(-BIG_TURNING_ANGLE)
            car.forward(POWER)
        elif direction == 'little_left':
            car.set_steering_angle(-SMALL_TURNING_ANGLE)
            car.forward(POWER)
        elif direction == 'right':
            car.set_steering_angle(BIG_TURNING_ANGLE)
            car.forward(POWER)
        elif direction == 'little_right':
            car.set_steering_angle(SMALL_TURNING_ANGLE)
            car.forward(POWER)
        else:
            outHandle()

if __name__=='__main__':
    try:
        main()
    finally:
        car.stop()
