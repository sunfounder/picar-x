import numpy as np
from picarx_improved import Picarx

px = Picarx()
while True:
    raw_reading = np.asarray(px.ir_sensors.read())
    # print(raw_reading)
    state = np.average(np.diff(raw_reading))
    if state > 0:
        print("LEFT")
    elif state < 0:
        print("RIGHT")
    else:
        print("FORWARD")
