from picarx import Picarx
from time import sleep
import readchar

manual = '''
Press keys on keyboard to control PiCar-X!
    w: Forward
    a: Turn left
    s: Backward
    d: Turn right
    i: Head up
    k: Head down
    j: Turn head left
    l: Turn head right
    ctrl+c: Press twice to exit the program
'''

def show_info():
    print("\033[H\033[J",end='')  # clear terminal windows
    print(manual)


if __name__ == "__main__":
    try:
        pan_angle = 0
        tilt_angle = 0
        px = Picarx()
        show_info()
        while True:
            key = readchar.readkey()
            key = key.lower()
            if key in('wsadikjl'): 
                if 'w' == key:
                    px.set_dir_servo_angle(0)
                    px.forward(80)
                elif 's' == key:
                    px.set_dir_servo_angle(0)
                    px.backward(80)
                elif 'a' == key:
                    px.set_dir_servo_angle(-30)
                    px.forward(80)
                elif 'd' == key:
                    px.set_dir_servo_angle(30)
                    px.forward(80)
                elif 'i' == key:
                    tilt_angle+=5
                    if tilt_angle>30:
                        tilt_angle=30
                elif 'k' == key:
                    tilt_angle-=5
                    if tilt_angle<-30:
                        tilt_angle=-30
                elif 'l' == key:
                    pan_angle+=5
                    if pan_angle>30:
                        pan_angle=30
                elif 'j' == key:
                    pan_angle-=5
                    if pan_angle<-30:
                        pan_angle=-30                 

                px.set_cam_tilt_angle(tilt_angle)
                px.set_cam_pan_angle(pan_angle)      
                show_info()                     
                sleep(0.5)
                px.forward(0)
          
            elif key == readchar.key.CTRL_C:
                print("\n Quit")
                break

    finally:
        px.set_cam_tilt_angle(0)
        px.set_cam_pan_angle(0)  
        px.set_dir_servo_angle(0)  
        px.stop()
        sleep(.2)


