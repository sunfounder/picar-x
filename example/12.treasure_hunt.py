from picarx import PiCarX
from time import sleep
from picarx import TTS
from vilib import Vilib
import readchar
import random
import threading

car = PiCarX()
tts = TTS()

manual = '''
Press keys on keyboard to control Picar-X!
    w: Forward
    a: Turn left
    s: Backward
    d: Turn right
    space: Say the target again
    ctrl+c: Quit
'''

color = "red"
color_list=["red","orange","yellow","green","blue","purple"]

def renew_color_detect():
    global color
    color = random.choice(color_list)
    Vilib.color_detect(color)
    tts.say("Look for " + color)

key = None
lock = threading.Lock()
def key_scan_thread():
    global key
    while True:
        key_temp = readchar.readkey()
        print('\r',end='')
        with lock:
            key = key_temp.lower()
            if key == readchar.key.SPACE:
                key = 'space'
            elif key == readchar.key.CTRL_C:
                key = 'quit'
                break
        sleep(0.01)

def car_move(key):
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


def main():
    global key
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=False,web=True)
    sleep(0.8)
    print(manual)

    sleep(1)
    _key_t = threading.Thread(target=key_scan_thread)
    _key_t.setDaemon(True)
    _key_t.start()

    tts.say("game start")
    sleep(0.05)
    renew_color_detect()
    while True:

        if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
            tts.say("will done")
            sleep(0.05)
            renew_color_detect()

        with lock:
            if key != None and key in ('wsad'):
                car_move(key)
                sleep(0.5)
                car.stop()
                key =  None
            elif key == 'space':
                tts.say("Look for " + color)
                key =  None
            elif key == 'quit':
                _key_t.join()
                print("\n\rQuit")
                break

        sleep(0.05)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        Vilib.camera_close()
        car.reset()
        print("Stop and exit")
        sleep(0.1)