import sys
sys.path.append(r'/home/pi/picar-x/lib')
from utils import reset_mcu
reset_mcu()

from pwm import PWM
from servo import Servo


if __name__ == '__main__':
    P_11 = Servo(PWM('P11'))         
    P_11.angle(0)     

