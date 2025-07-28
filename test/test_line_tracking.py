from picarx.picarx import PiCarX
import time
from picarx.auto_drive import LineTracking
from vilib import Vilib

car = PiCarX()
lt = LineTracking(car)
Vilib.camera_start(vflip=False, hflip=False, size=(800, 600))
Vilib.show_fps()
Vilib.display(local=False,web=True)

try:
    lt.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    lt.stop()