#!/usr/bin/env python3
from vilib import Vilib
import time

def main():

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    Vilib.color_detect("red")  # Set the color to be detected
    time.sleep(2)
    print('\npress Ctrl+C to exit\n')

    while True:
        try:
            num = Vilib.detect_obj_parameter['color_n'] 
            print("\rnumber of color blocks found: %s  "%num, end='', flush=True)
            time.sleep(0.5)
        except KeyboardInterrupt:
            print('\nquit ...')
            break
        except Exception as e:
            print('error:%s'%e)
            break

    Vilib.camera_close()
            

if __name__ == "__main__":
    main()

