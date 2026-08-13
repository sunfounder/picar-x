from sunfounder_controller import SunFounderController
from picarx import Picarx
from picarx import utils
from picarx.music import Music
from vilib import Vilib
import os
import time
from time import sleep

try:
    from tflite_runtime.interpreter import Interpreter
    TF_SUPPORTED = True
except ImportError:
    TF_SUPPORTED = False

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

VOICE_SPEED = 50  # default speed for voice commands (independent of joystick speed)
VOICE_ACTION_TIME = 2.0  # seconds a voice action keeps executing (matches turn maneuver ~2s)

current_line_state = None
last_line_state = "stop"
LINE_TRACK_SPEED = 10
LINE_TRACK_ANGLE_OFFSET = 20

AVOID_OBSTACLES_SPEED = 40
SafeDistance = 40   # > 40 safe
DangerDistance = 20 # > 20 && < 40 turn around, < 20 backward

DETECT_COLOR = 'red' # red, green, blue, yellow , orange, purple
last_values = {}

# init music player
User = os.popen('echo ${SUDO_USER:-$LOGNAME}').readline().strip()
UserHome = os.popen('getent passwd %s | cut -d: -f 6' %User).readline().strip()

music = Music()
if os.geteuid() != 0:
    print('\033[33mPlay sound needs to be run with sudo.\033[m')

def horn(): 
    _status, _result = utils.run_command('sudo killall pulseaudio')
    music.sound_play_threading(f'{UserHome}/picar-x/sounds/car-double-horn.wav')

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
    last_cmd = None
    prev_j = None
    ack_ts = 0
    while True:
        # --- send data ---
        sc.set("A", speed)

        grayscale_data = px.get_grayscale_data()
        sc.set("D", grayscale_data )

        distance = px.get_distance()
        sc.set("F", distance)

        # --- control ---

        # # horn
        if sc.get('M') == True:
            horn()

        # speaker (J-key ack protocol: receive -> ack(1) -> execute -> done(0))
        # Note: the App clears the command as soon as it receives J:1, so the
        # action duration is enforced here (VOICE_ACTION_TIME), not by the App.
        j = sc.get('J')
        if j != prev_j:                       # edge on J value change (repeat commands trigger too)
            prev_j = j
            if j not in (None, ''):
                speak = j
                sc.set("J", 1)               # ack: App clears the pending command
                ack_ts = time.time()
                print(f'speaker: {speak}')
        # enforce the action duration on the device (works whether or not the App cleared J)
        if speak is not None and time.time() - ack_ts > VOICE_ACTION_TIME:
            sc.set("J", 0)                   # done
            speak = None

        # execute the voice action once per new command; hold it for VOICE_ACTION_TIME
        if speak is not None:
            if speak != last_cmd:
                last_cmd = speak
                if speak in ["forward", "move forward", "go forward", "move ahead"]:
                    px.forward(VOICE_SPEED)
                elif speak in ["backward", "move backward", "back up", "reverse"]:
                    px.backward(VOICE_SPEED)
                elif speak in ["left", "turn left", "from left", "go left"]:
                    px.set_dir_servo_angle(-30)
                    px.forward(60)
                    sleep(1.2)
                    px.set_dir_servo_angle(0)
                    px.stop()                 # turn done -> stop (no trailing forward)
                    sc.set("J", 0)           # finish immediately
                    speak = None
                    last_cmd = None
                elif speak in ["right", "turn right", "from right", "go right", "white", "rice"]:
                    px.set_dir_servo_angle(30)
                    px.forward(60)
                    sleep(1.2)
                    px.set_dir_servo_angle(0)
                    px.stop()                 # turn done -> stop (no trailing forward)
                    sc.set("J", 0)           # finish immediately
                    speak = None
                    last_cmd = None
                elif speak in ["stop", "halt", "brake"]:
                    px.stop()
                    sc.set("J", 0)           # stop is instant: finish immediately
                    speak = None
                    last_cmd = None
        elif last_cmd is not None:
            px.stop()                         # action finished -> stop the car
            last_cmd = None

        # line_track and avoid_obstacles
        line_track_switch = sc.get('I')
        avoid_obstacles_switch = sc.get('E')
        if line_track_switch == True:
            speed = LINE_TRACK_SPEED
            line_track()
        elif avoid_obstacles_switch == True:
            speed = AVOID_OBSTACLES_SPEED
            avoid_obstacles()
    
        # joystick moving (voice command in progress -> joystick waits)
        if speak is None and line_track_switch != True and avoid_obstacles_switch != True:
            Joystick_K_Val = sc.get('K')
            if Joystick_K_Val != None and isinstance(Joystick_K_Val, list) and len(Joystick_K_Val) == 2:
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
        if Joystick_Q_Val != None and isinstance(Joystick_Q_Val, list) and len(Joystick_Q_Val) == 2:
            pan = min(90, max(-90, Joystick_Q_Val[0]))
            tilt = min(65, max(-35, Joystick_Q_Val[1]))
            px.set_cam_pan_angle(pan)
            px.set_cam_tilt_angle(tilt)

        # image recognition
        n_value = sc.get('N')
        if n_value != last_values.get('N'):
            last_values['N'] = n_value
            if n_value == True:
                Vilib.color_detect(DETECT_COLOR)
            else:
                Vilib.color_detect("close")

        o_value = sc.get('O')
        if o_value != last_values.get('O'):
            last_values['O'] = o_value
            Vilib.face_detect_switch(o_value)  

        p_value = sc.get('P')
        if p_value != last_values.get('P'):
            last_values['P'] = p_value
            if not TF_SUPPORTED:
                print("[WARNING] Object detection is currently not available for this OS.")
            else:
                Vilib.object_detect_switch(p_value) 


if __name__ == "__main__":
    try:
        main()
    finally:
        print("stop and exit")
        px.stop()
        Vilib.camera_close()




