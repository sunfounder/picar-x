from sunfounder_controller import SunFounderController
from picarx import Picarx
from robot_hat import utils, Music
from vilib import Vilib
import os
from time import sleep

# reset robot_hat
utils.reset_mcu()
sleep(0.2)

# init SunFounder Controller class
sc = SunFounderController()
sc.set_name('Picarx-001')
sc.set_type('Picarx')
sc.start()

# init picarx
px = Picarx()
speed = 0

current_line_state = None
last_line_state = "stop"
LINE_TRACK_SPEED = 10
LINE_TRACK_ANGLE_OFFSET = 20

AVOID_OBSTACLES_SPEED = 40
SafeDistance = 40   # > 40 safe
DangerDistance = 20 # > 20 && < 40 turn around, < 20 backward

DETECT_COLOR = 'red' # red, green, blue, yellow , orange, purple

# init music player
music = Music()
if os.geteuid() != 0:
    print('\033[33mPlay sound needs to be run with sudo.\033[m')

def horn(): 
    _status, _result = utils.run_command('sudo killall pulseaudio')
    music.sound_play_threading('./sounds/car-double-horn.wav')

def avoid_obstacles():
    distance = px.get_distance()
    if distance >= SafeDistance:
        px.set_dir_servo_angle(0)
        px.forward(AVOID_OBSTACLES_SPEED)
    elif distance >= DangerDistance:
        px.set_dir_servo_angle(30)
        px.forward(AVOID_OBSTACLES_SPEED)
        sleep(0.1)
    else:
        px.set_dir_servo_angle(-30)
        px.backward(AVOID_OBSTACLES_SPEED)
        sleep(0.5) 

def get_status(val_list):
    _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
    if _state == [0, 0, 0]:
        return 'stop'
    elif _state[1] == 1:
        return 'forward'
    elif _state[0] == 1:
        return 'right'
    elif _state[2] == 1:
        return 'left'

def outHandle():
    global last_line_state, current_line_state
    if last_line_state == 'left':
        px.set_dir_servo_angle(-30)
        px.backward(10)
    elif last_line_state == 'right':
        px.set_dir_servo_angle(30)
        px.backward(10)
    while True:
        gm_val_list = px.get_grayscale_data()
        gm_state = get_status(gm_val_list)
        currentSta = gm_state
        if currentSta != last_line_state:
            break
    sleep(0.001)

def line_track():
    global last_line_state
    gm_val_list = px.get_grayscale_data()
    gm_state = get_status(gm_val_list)

    if gm_state != "stop":
        last_line_state = gm_state

    if gm_state == 'forward':
        px.set_dir_servo_angle(0)
        px.forward(LINE_TRACK_SPEED) 
    elif gm_state == 'left':
        px.set_dir_servo_angle(LINE_TRACK_ANGLE_OFFSET)
        px.forward(LINE_TRACK_SPEED) 
    elif gm_state == 'right':
        px.set_dir_servo_angle(-LINE_TRACK_ANGLE_OFFSET)
        px.forward(LINE_TRACK_SPEED) 
    else:
        outHandle()

def main():
    global speed

    ip = utils.get_ip()
    print('ip : %s'%ip)
    sc.set('video','http://'+ip+':9000/mjpg')

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=False, web=True)
    speak = None
    while True:
        # --- send data ---
        sc.set("A", speed)

        grayscale_data = px.get_grayscale_data()
        sc.set("D", grayscale_data )

        distance = px.get_distance()
        sc.set("F", distance)

        # --- control ---

        # # horn
        # if sc.get('M') == True:
        #     horn()

        # speaker
        if sc.get('J') != None:
            speak=sc.get('J')
            print(f'speaker: {speak}')
        if speak in ["forward"]:
            px.forward(speed)
        elif speak in ["backward"]:
            px.backward(speed)
        elif speak in ["left"]:
            px.set_dir_servo_angle(-30)
            px.forward(60)
            sleep(1.2)
            px.set_dir_servo_angle(0)
            px.forward(speed)
        elif speak in ["right", "white", "rice"]:
            px.set_dir_servo_angle(30)
            px.forward(60)
            sleep(1.2)
            px.set_dir_servo_angle(0)
            px.forward(speed)
        elif speak in ["stop"]:
            px.stop()

        # line_track and avoid_obstacles
        line_track_switch = sc.get('I')
        avoid_obstacles_switch = sc.get('E')
        if line_track_switch == True:
            line_track()
        elif avoid_obstacles_switch == True:
            avoid_obstacles()
    
        # joystick moving
        if line_track_switch != True and avoid_obstacles_switch != True:
            Joystick_K_Val = sc.get('K')
            if Joystick_K_Val != None:
                dir_angle = utils.mapping(Joystick_K_Val[0], -100, 100, -30, 30)
                speed = Joystick_K_Val[1]
                px.set_dir_servo_angle(dir_angle)
                if speed > 0:
                    px.forward(speed)
                elif speed < 0:
                    speed = -speed
                    px.backward(speed)
                else:
                    px.stop()

        # camera servos control
        Joystick_Q_Val = sc.get('Q')
        if Joystick_Q_Val != None:
            pan = min(90, max(-90, Joystick_Q_Val[0]))
            tilt = min(65, max(-35, Joystick_Q_Val[1]))
            px.set_cam_pan_angle(pan)
            px.set_cam_tilt_angle(tilt)

        # image recognition
        if sc.get('N') == True:
            Vilib.color_detect(DETECT_COLOR)
        else:
            Vilib.color_detect_switch(False)

        if sc.get('O') == True:
            Vilib.human_detect_switch(True)  
        else:
            Vilib.human_detect_switch(False)  

        if sc.get('P') == True:
            Vilib.object_detect_switch(True) 
        else:
            Vilib.object_detect_switch(False)


if __name__ == "__main__":
    try:
        main()
    finally:
        print("stop and exit")
        px.stop()
        Vilib.camera_close()




