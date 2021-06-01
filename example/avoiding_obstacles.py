import sys
sys.path.append(r'/home/pi/picar-x/lib')
from utils import reset_mcu
reset_mcu()

from picarx import Picarx
from ultrasonic import Ultrasonic
from pin import Pin

if __name__ == "__main__":
    try:
        trig_pin = Pin("D2") 
        echo_pin = Pin("D3")
        sonar = Ultrasonic(trig_pin, echo_pin)
        px = Picarx()
        px.forward(30)
        while True:
            distance = sonar.read()
            print("distance: ",distance)
            if distance > 0 and distance < 300:
                if distance < 25:
                    px.set_dir_servo_angle(-35)
                else:
                    px.set_dir_servo_angle(0)
    finally:
        px.forward(0)


