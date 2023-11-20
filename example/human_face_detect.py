#!/usr/bin/env python3

from vilib import Vilib
from time import sleep

def main():
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=False)
    Vilib.face_detect_switch(True)
    sleep(2)
    print('\npress Ctrl+C to exit\n')

    while True:
        try:
            num = Vilib.detect_obj_parameter['human_n'] 
            print("\rnumber offaces found %s"%num, end='', flush=True)
            sleep(0.5)
        except KeyboardInterrupt:
            print('\nquit ...')
            break
        except Exception as e:
            print('error:%s'%e)
            break

    Vilib.camera_close()


if __name__ == "__main__":
    main()
