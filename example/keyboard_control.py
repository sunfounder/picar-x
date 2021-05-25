# # import picar_4wd as fc
import sys
import tty
import termios
from picarx import Picarx
import time


px = Picarx()
power_val = 0


def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)
 

def Keyborad_control():
    while True:
        global power_val,control_angle
        key = readkey()  # 读取键盘的按下值，这里是阻塞的
        print("key:",key)
        if key=='o':
            if power_val <=90:
                power_val += 10
                print("power_val:",power_val)  # 增大电机速度
        elif key=='p':
            if power_val >=10:
                power_val -= 10
                print("power_val:",power_val)  #减小电机速度
        if key=='w':
            # print("w:",)
            px.set_dir_servo_angle(0)
            px.forward(power_val)
        elif key=='a':
            px.set_dir_servo_angle(-30) # 左转
            px.forward(power_val)
        elif key=='s':
            px.set_dir_servo_angle(0) # 后退
            px.backward(power_val)
        elif key=='d':
            px.set_dir_servo_angle(30) # 右转
            px.forward(power_val)
        elif key=='t':   # 拍照
            Vilib.shuttle_button() 
        else:    
            px.stop()  #停下来
        if key=='q':
            print("quit")   #退出
            break  

if __name__ == "__main__":

    # while True:
    Keyborad_control()



