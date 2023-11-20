#!/usr/bin/env python3
from vilib import Vilib
import time

try:
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    time.sleep(2)
    print('\npress  Ctrl+C to exit')
    while True:
        time.sleep(1)  # Keep the main thread alive to accept the KeyboardInterrupt signal
except KeyboardInterrupt:
    print('\nquit ...')
except Exception as e:
    print('error:%s'%e)
finally:
    Vilib.camera_close()

