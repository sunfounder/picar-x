import sys
sys.path.append(r'/home/pi/picar-x/lib')
from utils import reset_mcu
reset_mcu()

from picarx import Picarx
from ultrasonic import Ultrasonic
from pin import Pin



if __name__ == "__main__":
    trig_pin = Pin("D0") 
    echo_pin = Pin("D1")
    px = Picarx()
    px.forward(0)
    while True:
        distance = Ultrasonic(trig_pin, echo_pin).read()
        if distance > 0:
            if distance < 10:
                px.set_dir_servo_angle(-30)
            else:
                px.set_dir_servo_angle(0)


