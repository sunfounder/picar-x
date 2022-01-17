
from robot_hat import PWM, Servo


if __name__ == '__main__':
    P_11 = Servo(PWM('P11'))         
    P_11.angle(0)     

