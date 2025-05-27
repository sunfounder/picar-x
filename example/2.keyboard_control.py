from picarx import PiCarX
from time import sleep
import readchar

car = PiCarX()

usage = '''
Press keys on keyboard to control PiCar-X!
    w: Forward
    a: Turn left
    s: Backward
    d: Turn right
    i: Head up
    k: Head down
    j: Turn head left
    l: Turn head right
    q: Stop
    ctrl+c: Press twice to exit the program
'''

def show_info():
    print("\033[H\033[J",end='')  # clear terminal windows
    print(usage)

def main():
    pan_angle = 0
    tilt_angle = 0
    show_info()
    while True:
        key = readchar.readkey()
        key = key.lower()
        if key in('wsadikjlq'): 
            if 'w' == key:
                car.set_steering_angle(0)
                car.forward(80)
            elif 's' == key:
                car.set_steering_angle(0)
                car.backward(80)
            elif 'a' == key:
                car.set_steering_angle(-30)
                car.forward(80)
            elif 'd' == key:
                car.set_steering_angle(30)
                car.forward(80)
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
            elif 'q' == key:
                car.set_steering_angle(0)
                car.stop()

            car.set_camera_tilt_angle(tilt_angle)
            car.set_camera_pan_angle(pan_angle)      
            show_info()                     
        
        elif key == readchar.key.CTRL_C:
            print("\n Quit")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        car.reset()
        print("Stop and exit")
        sleep(0.1)



