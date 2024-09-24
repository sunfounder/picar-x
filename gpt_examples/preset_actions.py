
from time import sleep
import random
from math import sin, cos, pi

def wave_hands(car):
    car.reset()
    car.set_cam_tilt_angle(20)
    for _ in range(2):
        car.set_dir_servo_angle(-25)
        sleep(.1)
        # car.set_dir_servo_angle(0)
        # sleep(.1)
        car.set_dir_servo_angle(25)
        sleep(.1)
    car.set_dir_servo_angle(0)

def resist(car):
    car.reset()
    car.set_cam_tilt_angle(10)
    for _ in range(3):
        car.set_dir_servo_angle(-15)
        car.set_cam_pan_angle(15)
        sleep(.1)
        car.set_dir_servo_angle(15)
        car.set_cam_pan_angle(-15)
        sleep(.1)
    car.stop()
    car.set_dir_servo_angle(0)
    car.set_cam_pan_angle(0)

def act_cute(car):
    car.reset()
    car.set_cam_tilt_angle(-20)
    for i in range(15):
        car.forward(5)
        sleep(0.02)
        car.backward(5)
        sleep(0.02)
    car.set_cam_tilt_angle(0)
    car.stop()

def rub_hands(car):
    car.reset()
    for i in range(5):
        car.set_dir_servo_angle(-6)
        sleep(.5)
        car.set_dir_servo_angle(6)
        sleep(.5)
    car.reset()

def think(car):
    car.reset()

    for i in range(11):
        car.set_cam_pan_angle(i*3)
        car.set_cam_tilt_angle(-i*2)
        car.set_dir_servo_angle(i*2)
        sleep(.05)
    sleep(1)
    car.set_cam_pan_angle(15)
    car.set_cam_tilt_angle(-10)
    car.set_dir_servo_angle(10)
    sleep(.1)
    car.reset()

def keep_think(car):
    car.reset()
    for i in range(11):
        car.set_cam_pan_angle(i*3)
        car.set_cam_tilt_angle(-i*2)
        car.set_dir_servo_angle(i*2)
        sleep(.05)

def shake_head(car):
    car.stop()
    car.set_cam_pan_angle(0)
    car.set_cam_pan_angle(60)
    sleep(.2)
    car.set_cam_pan_angle(-50)
    sleep(.1)
    car.set_cam_pan_angle(40)
    sleep(.1)
    car.set_cam_pan_angle(-30)
    sleep(.1)
    car.set_cam_pan_angle(20)
    sleep(.1)
    car.set_cam_pan_angle(-10)
    sleep(.1)
    car.set_cam_pan_angle(10)
    sleep(.1)
    car.set_cam_pan_angle(-5)
    sleep(.1)
    car.set_cam_pan_angle(0)

def nod(car):
    car.reset()
    car.set_cam_tilt_angle(0)
    car.set_cam_tilt_angle(5)
    sleep(.1)
    car.set_cam_tilt_angle(-30)
    sleep(.1)
    car.set_cam_tilt_angle(5)
    sleep(.1)
    car.set_cam_tilt_angle(-30)
    sleep(.1)
    car.set_cam_tilt_angle(0)


def depressed(car):
    # car.reset()
    # car.set_cam_tilt_angle(0)
    # car.set_cam_tilt_angle(20)
    # sleep(.22)
    # car.set_cam_tilt_angle(-30)
    # sleep(.1)
    # car.set_cam_tilt_angle(15)
    # sleep(.1)
    # car.set_cam_tilt_angle(-20)
    # sleep(.1)
    # car.set_cam_tilt_angle(10)
    # sleep(.1)
    # car.set_cam_tilt_angle(-10)
    # sleep(.1)
    # car.set_cam_tilt_angle(5)
    # sleep(.1)
    # car.set_cam_tilt_angle(-5)
    # sleep(.1)
    # car.set_cam_tilt_angle(2)
    # sleep(.1)
    # car.set_cam_tilt_angle(0)

    car.reset()
    car.set_cam_tilt_angle(0)
    car.set_cam_tilt_angle(20)
    sleep(.22)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(10)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(0)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(-10)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(-15)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)
    car.set_cam_tilt_angle(-19)
    sleep(.1)
    car.set_cam_tilt_angle(-22)
    sleep(.1)

    sleep(1.5)
    car.reset()

def twist_body(car):
    car.reset()
    for i in range(3):
        car.set_motor_speed(1, 20)
        car.set_motor_speed(2, 20)
        car.set_cam_pan_angle(-20)
        car.set_dir_servo_angle(-10)
        sleep(.1)
        car.set_motor_speed(1, 0)
        car.set_motor_speed(2, 0)
        car.set_cam_pan_angle(0)
        car.set_dir_servo_angle(0)
        sleep(.1)
        car.set_motor_speed(1, -20)
        car.set_motor_speed(2, -20)
        car.set_cam_pan_angle(20)
        car.set_dir_servo_angle(10)
        sleep(.1)
        car.set_motor_speed(1, 0)
        car.set_motor_speed(2, 0)
        car.set_cam_pan_angle(0)
        car.set_dir_servo_angle(0)

        sleep(.1)


def celebrate(car):
    car.reset()
    car.set_cam_tilt_angle(20)

    car.set_dir_servo_angle(30)
    car.set_cam_pan_angle(60)
    sleep(.3)
    car.set_dir_servo_angle(10)
    car.set_cam_pan_angle(30)
    sleep(.1)
    car.set_dir_servo_angle(30)
    car.set_cam_pan_angle(60)
    sleep(.3)
    car.set_dir_servo_angle(0)
    car.set_cam_pan_angle(0)
    sleep(.2)

    car.set_dir_servo_angle(-30)
    car.set_cam_pan_angle(-60)
    sleep(.3)
    car.set_dir_servo_angle(-10)
    car.set_cam_pan_angle(-30)
    sleep(.1)
    car.set_dir_servo_angle(-30)
    car.set_cam_pan_angle(-60)
    sleep(.3)
    car.set_dir_servo_angle(0)
    car.set_cam_pan_angle(0)
    sleep(.2)

def honking(music):
    import utils
    # utils.speak_block(music, "../sounds/car-double-horn.wav", 100)
    music.sound_play_threading("../sounds/car-double-horn.wav", 100)

def start_engine(music):
    import utils
    # utils.speak_block(music, "../sounds/car-start-engine.wav", 100)
    music.sound_play_threading("../sounds/car-start-engine.wav", 50)


actions_dict = {
    "shake head":shake_head, 
    "nod": nod,
    "wave hands": wave_hands,
    "resist": resist,
    "act cute": act_cute,
    "rub hands": rub_hands,
    "think": think,
    "twist body": twist_body,
    "celebrate": celebrate,
    "depressed": depressed,
}

sounds_dict = {
    "honking": honking,
    "start engine": start_engine,
}


if __name__ == "__main__":
    from picarx import Picarx
    from robot_hat import Music
    import os

    os.popen("pinctrl set 20 op dh") # enable robot_hat speake switch
    current_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_path) # change working directory

    my_car = Picarx()
    my_car.reset()

    music = Music()

    sleep(.5)

    _actions_num = len(actions_dict)
    actions = list(actions_dict.keys())
    for i, key in enumerate(actions_dict):
        print(f'{i} {key}')
    
    _sounds_num = len(sounds_dict)
    sounds = list(sounds_dict.keys())
    for i, key in enumerate(sounds_dict):
        print(f'{_actions_num+i} {key}')

    last_key = None

    try:
        while True:
            key = input()

            if key == '':
                if last_key > _actions_num - 1:
                    print(sounds[last_key-_actions_num])
                    sounds_dict[sounds[last_key-_actions_num]](music)
                else:
                    print(actions[last_key])
                    actions_dict[actions[last_key]](my_car)
            else:
                key = int(key)
                if key > (_actions_num + _sounds_num - 1):
                    print("Invalid key")
                elif key > (_actions_num - 1):
                    last_key = key
                    print(sounds[last_key-_actions_num])
                    sounds_dict[sounds[last_key-_actions_num]](music)
                else:
                    last_key = key
                    print(actions[key])
                    actions_dict[actions[key]](my_car)

            # sleep(2)
            # shake_head(my_car)
            # nod(my_car)
            # wave_hands(my_car)
            # resist(my_car)
            # act_cute(my_car)
            # rub_hands(my_car)
            # think(my_car)
            # twist(my_car)
            # celebrate(my_car)
            # depressed(my_car)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f'Error:\n {e}')
    finally:
        my_car.reset()
        sleep(.1)




