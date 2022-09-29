# #!/usr/bin/env python3

print('Please run under desktop environment (eg: vnc) to display the image window')

from robot_hat.utils import reset_mcu
from picarx import Picarx
from vilib import Vilib
from time import sleep, time, strftime, localtime
import readchar

reset_mcu()
sleep(0.2)

manual = '''
Press key to call the function(non-case sensitive):

    O: speed up
    P: speed down
    W: forward  
    S: backward
    A: turn left
    D: turn right
    F: stop
    T: take photo

    Ctrl+C: quit
'''


px = Picarx()

def take_photo():
    _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
    name = 'photo_%s'%_time
    path = "/home/pi/Pictures/picar-x/"
    Vilib.take_photo(name, path)
    print('\nphoto save as %s%s.jpg'%(path,name))


def move(operate:str, speed):

    if operate == 'stop':
        px.stop()  
    else:
        if operate == 'forward':
            px.set_dir_servo_angle(0)
            px.forward(speed)
        elif operate == 'backward':
            px.set_dir_servo_angle(0)
            px.backward(speed)
        elif operate == 'turn left':
            px.set_dir_servo_angle(-30)
            px.forward(speed)
        elif operate == 'turn right':
            px.set_dir_servo_angle(30)
            px.forward(speed)
        


def main():
    speed = 0
    status = 'stop'

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    sleep(2)  # wait for startup
    print(manual)
    
    while True:
        print("\rstatus: %s , speed: %s    "%(status, speed), end='', flush=True)
        # readkey
        key = readchar.readkey().lower()
        # operation 
        if key in ('wsadfop'):
            # throttle
            if key == 'o':
                if speed <=90:
                    speed += 10           
            elif key == 'p':
                if speed >=10:
                    speed -= 10
                if speed == 0:
                    status = 'stop'
            # direction
            elif key in ('wsad'):
                if speed == 0:
                    speed = 10
                if key == 'w':
                    # Speed limit when reversing,avoid instantaneous current too large
                    if status != 'forward' and speed > 60:  
                        speed = 60
                    status = 'forward'
                elif key == 'a':
                    status = 'turn left'
                elif key == 's':
                    if status != 'backward' and speed > 60: # Speed limit when reversing
                        speed = 60
                    status = 'backward'
                elif key == 'd':
                    status = 'turn right' 
            # stop
            elif key == 'f':
                status = 'stop'
            # move 
            move(status, speed)  
        # take photo
        elif key == 't':
            take_photo()
        # quit
        elif key == readchar.key.CTRL_C:
            print('\nquit ...')
            px.stop()
            Vilib.camera_close()
            break 

        sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:    
        print("error:%s"%e)
    finally:
        px.stop()
        Vilib.camera_close()


        