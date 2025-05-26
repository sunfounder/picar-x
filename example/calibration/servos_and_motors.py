#!/usr/bin/env python3
from picarx import PiCarX
from time import sleep
import readchar 

POWER = 30
SERVO_STEP = 0.1
MOTOR_RUNS_FOR = 2

usage = '''
------------------- Picar-X Calibration Helper ---------------------

- Use W/A/S/D to adjust the up/down/left/right offsets of the camera
  pan-tilt servos.
- Use Q/E to adjust the left/right offsets of steering servo.
- Use Z/C to adjust the up/down offsets of the direction servo.
Press [Ctrl] + [C] to quit.

                                              ┌─────┐
              [W]                             └┌───┐┘
               ▲                           ┌─┐ │   │ ┌─┐
             ├───┤                    [Q]◀ │ │=│   │=│ │ ▶[E]
        [A]◀ │ O │ ▶[S]                    └─┘ │   │ └─┘
             └┬─┬┘                         ┌─┐/     \┌─┐
               ▼                      [Z]⇅ │ ││     ││ │ ⇅[C]
              [D]                          └─┘│     │└─┘
                                              └─────┘

'''    

car = PiCarX()

def show_info():
    print("\033[H\033[J", end='')  # clear terminal windows
    print(usage)
    print(f"     Steering Servo Offset: {car.steering_servo.offset()}")
    print(f"   Camera Pan Servo Offset: {car.camera_pan_servo.offset()}")
    print(f"  Camera Tilt Servo Offset: {car.camera_tilt_servo.offset()}")
    print(f"       Left Motor Reversed: {car.motors.left_reversed}")
    print(f"      Right Motor Reversed: {car.motors.right_reversed}")

def main(): 
    motor_runs = False
    # show_info 
    show_info()

    # key control
    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # select the servo 
        if key in ('wasdzcqe'):
            if key == 'w':
                new_offset = car.camera_tilt_servo.offset() - SERVO_STEP
                new_offset = round(new_offset, 2)
                car.set_camera_tilt_offset(new_offset)
            elif key == 's':
                new_offset = car.camera_tilt_servo.offset() + SERVO_STEP
                new_offset = round(new_offset, 2)
                car.set_camera_tilt_offset(new_offset)
            elif key == 'a':
                new_offset = car.camera_pan_servo.offset() - SERVO_STEP
                new_offset = round(new_offset, 2)
                car.set_camera_pan_offset(new_offset)
            elif key == 'd':
                new_offset = car.camera_pan_servo.offset() + SERVO_STEP
                new_offset = round(new_offset, 2)
                car.set_camera_pan_offset(new_offset)
            elif key == 'q':
                new_offset = car.steering_servo.offset() - SERVO_STEP
                new_offset = round(new_offset, 2)
                car.set_steering_offset(new_offset)
            elif key == 'e':
                new_offset = car.steering_servo.offset() + SERVO_STEP
                new_offset = round(new_offset, 2)
                car.set_steering_offset(new_offset)
            elif key == 'z':
                reversed = not car.motors.left_reversed
                car.set_left_motor_reverse(reversed)
                motor_runs = True
            elif key == 'c':
                reversed = not car.motors.right_reversed
                car.set_right_motor_reverse(reversed)
                motor_runs = True

        # quit
        elif key == readchar.key.CTRL_C or key in readchar.key.ESC:
            print('quit')
            break 

        sleep(0.01)
        show_info()
        if motor_runs:
            car.forward(POWER)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('quit')
    except Exception as e:
        print(e)
    finally:
        car.stop()
