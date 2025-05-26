#!/usr/bin/env python3
from picarx import PiCarX
import readchar 
from time import sleep

AVERAGE_COUNT = 10

usage = '''
---------------- Picar-X Grayscale Sensor Calibration Helper ----------------

- Put all 3 sensors over the line and press [Q] to get on-line values
- Put all 3 sensors off the line and press [W] to get off-line values
- Lift all 3 sensors up and press [E] to get cliff values

After all values are set, reference values will calculate automatically
And save to the config file.
Press [Ctrl] + [C] to quit.

                           ___________________
                           -------------------
   ______┌─────┐______           ┌─────┐                   ┌─────┐      
   ------└┌───┐┘------           └┌───┐┘         ┌─────────└┌───┐┘─────────┐
      ┌─┐ │   │ ┌─┐           ┌─┐ │   │ ┌─┐      │      ┌─┐ │   │ ┌─┐      │
      │ │=│   │=│ │           │ │=│   │=│ │      │      │ │=│   │=│ │      │
      └─┘ │   │ └─┘           └─┘ │   │ └─┘      │      └─┘ │   │ └─┘      │

           [Q]                     [W]                       [E]'''    

car = PiCarX()
off_line_value = None
on_line_value = None
clift_value = None
line_reference = None
cliff_reference = None

def show_info():
    print("\033[H\033[J", end='')  # clear terminal windows
    print(usage)
    print(f"    {str(on_line_value).center(16)}        {str(off_line_value).center(16)}           {str(clift_value).center(16)}")
    print(f"")
    if line_reference == None:
        print(f"   Line Reference: {car.line_reference}(Not set)")
        print(f"  Cliff Reference: {car.cliff_reference}(Not set)")
    else:
        print(f"   Line Reference: {line_reference}")
        print(f"  Cliff Reference: {cliff_reference}")

def get_average_values():
    datas = []
    for _ in range(AVERAGE_COUNT):
        datas.append(car.get_grayscale_data())
        sleep(0.1)
    
    result = [int(sum(x)/AVERAGE_COUNT) for x in zip(*datas)]
    return result

def calculate_reference():
    global line_reference, cliff_reference
    line_reference = [int((x+y)/2) for x, y in zip(on_line_value, off_line_value)]
    cliff_reference = [int((x+y)/5) for x, y in zip(clift_value, line_reference)]
    car.set_line_reference(line_reference)
    car.set_cliff_reference(cliff_reference)

def main(): 
    global off_line_value, on_line_value, clift_value, line_reference, cliff_reference
    # key control
    while True:
        show_info()
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # select the servo 
        if key in ('qwe'):
            if key == 'q':
                on_line_value = get_average_values()
            elif key == 'w':
                off_line_value = get_average_values()
            elif key == 'e':
                clift_value = get_average_values()

        # quit
        elif key == readchar.key.CTRL_C or key in readchar.key.ESC:
            print('quit')
            break 

        sleep(0.01)
        if off_line_value is not None and on_line_value is not None and clift_value is not None:
            calculate_reference()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('quit')
    except Exception as e:
        print(e)
    finally:
        car.stop()
