#!/usr/bin/env python3
from picarx import PiCarX
from picarx.utils import print_line_position
import readchar 
from time import sleep
from statistics import median
from threading import Thread

usage = '''
---------------- Picar-X Grayscale Sensor Calibration Helper ----------------

- Put all 3 sensors over the Dark and press [Q] to get dark values
- Put all 3 sensors off the Light and press [W] to get light values

After all values are set, reference values will calculate automatically
And save to the config file.
Press [Ctrl] + [C] to quit.

                DARK                                     LIGHT
           ▓▓▓▓▓▓▓▓▓▓▓▓▓                             ┌───────────┐
           ▓▓▓┌─────┐▓▓▓                             │  ┌─────┐  │
           ▓▓▓└┌───┐┘▓▓▓                             └──└┌───┐┘──┘
           ┌─┐ │   │ ┌─┐                             ┌─┐ │   │ ┌─┐
           │ │=│   │=│ │                             │ │=│   │=│ │
           └─┘ │   │ └─┘                             └─┘ │   │ └─┘
                [Q]                                       [W]
'''

car = PiCarX()
dark_value = None
light_value = None
running = False
info_thread = None

def get_median_data(times=10, delay=0.001):
    left_datas = []
    middle_datas = []
    right_datas = []
    datas = []

    for _ in range(times):
        g0, g1, g2 = car.get_grayscale_data(raw=True)
        left_datas.append(g0)
        middle_datas.append(g1)
        right_datas.append(g2)
        if delay > 0:
            sleep(delay)
    
    datas = [left_datas, middle_datas, right_datas]

    median_data = [median(datas[i]) for i in range(3)]
    return median_data

def show_info():
    print("\033[H\033[J", end='')  # clear terminal windows
    print(usage)
    dark_value_string = "Not set" if dark_value is None else str(dark_value)
    light_value_string = "Not set" if light_value is None else str(light_value)
    dark_value_string = dark_value_string.center(25)
    light_value_string = light_value_string.center(25)
    print(f"     {dark_value_string}                 {light_value_string}")
    print(f"")
    print(f"")
    raw_data = car.get_grayscale_data(raw=True)
    calibrated_data = car.grayscale.calibrate_data(raw_data)
    print(f"         Raw value: {raw_data}")
    print(f"  Calibrated value: {calibrated_data}")
    if car.is_on_cliff(data=calibrated_data):
        print(f"            Status: On Cliff")
    elif car.is_on_line(data=calibrated_data):
        position = car.get_line_position(data=calibrated_data)
        print_line_position(position)
    else:
        print("")
    print(f"")

def show_info_thread():
    while running:
        show_info()
        sleep(0.01)

def main(): 
    global dark_value, light_value, running, info_thread

    running = True

    # show info thread
    info_thread = Thread(target=show_info_thread)
    info_thread.daemon = True
    info_thread.start()

    # key control
    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # select the servo 
        if key in ('qwe'):
            if key == 'q':
                dark_value = get_median_data()
            elif key == 'w':
                light_value = get_median_data()

        # quit
        elif key == readchar.key.CTRL_C or key in readchar.key.ESC:
            print('quit')
            break 

        sleep(0.01)
        if dark_value is not None and light_value is not None:
            car.calibrate_grayscale(light_value, dark_value)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('quit')
    except Exception as e:
        print(e)
    finally:
        running = False
        info_thread.join()
        car.stop()
