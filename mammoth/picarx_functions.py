import time
import threading

# avoid_obstacles
# =================================================================
AVOID_OBSTACLES_SPEED = 40
SafeDistance = 40   # > 40 safe
DangerDistance = 20 # > 20 && < 40 turn around, < 20 backward

def avoid_obstacles(px, speed):
    distance = px.get_distance()
    if distance >= SafeDistance:
        px.set_dir_servo_angle(0)
        px.forward(speed)
    elif distance >= DangerDistance:
        px.set_dir_servo_angle(30)
        px.forward(speed)
        time.sleep(0.1)
    else:
        px.set_dir_servo_angle(-30)
        px.backward(speed)
        time.sleep(0.5)


# line_track
# =================================================================
current_line_state = None
last_line_state = "stop"
LINE_TRACK_SPEED = 10
LINE_TRACK_ANGLE_OFFSET = 20

def get_status(px, val_list):
    _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
    if _state == [0, 0, 0]:
        return 'stop'
    elif _state[1] == 1:
        return 'forward'
    elif _state[0] == 1:
        return 'right'
    elif _state[2] == 1:
        return 'left'

def outHandle(px):
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
    time.sleep(0.001)

def line_track(px, speed):
    global last_line_state
    gm_val_list = px.get_grayscale_data()
    gm_state = get_line_status(gm_val_list)

    if gm_state != "stop":
        last_line_state = gm_state

    if gm_state == 'forward':
        px.set_dir_servo_angle(0)
        px.forward(speed) 
    elif gm_state == 'left':
        px.set_dir_servo_angle(LINE_TRACK_ANGLE_OFFSET)
        px.forward(speed) 
    elif gm_state == 'right':
        px.set_dir_servo_angle(-LINE_TRACK_ANGLE_OFFSET)
        px.forward(speed) 
    else:
        outHandle()

# avoid_obstacles
# =================================================================
AVOID_OBSTACLES_SPEED = 40
SafeDistance = 40   # > 40 safe
DangerDistance = 20 # > 20 && < 40 turn around, < 20 backward

def avoid_obstacles(px, speed):
    distance = px.get_distance()
    if distance >= SafeDistance:
        px.set_dir_servo_angle(0)
        px.forward(speed)
    elif distance >= DangerDistance:
        px.set_dir_servo_angle(30)
        px.forward(speed)
        time.sleep(0.1)
    else:
        px.set_dir_servo_angle(-30)
        px.backward(speed)
        time.sleep(0.5)


# line_track
# =================================================================
current_line_state = None
last_line_state = "stop"
LINE_TRACK_SPEED = 10
LINE_TRACK_ANGLE_OFFSET = 20

def get_line_status(px, val_list):
    _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
    if _state == [0, 0, 0]:
        return 'stop'
    elif _state[1] == 1:
        return 'forward'
    elif _state[0] == 1:
        return 'right'
    elif _state[2] == 1:
        return 'left'

def outHandle(px):
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
    time.sleep(0.001)

def line_track(px, speed):
    global last_line_state
    gm_val_list = px.get_grayscale_data()
    gm_state = get_status(gm_val_list)

    if gm_state != "stop":
        last_line_state = gm_state

    if gm_state == 'forward':
        px.set_dir_servo_angle(0)
        px.forward(speed) 
    elif gm_state == 'left':
        px.set_dir_servo_angle(LINE_TRACK_ANGLE_OFFSET)
        px.forward(speed) 
    elif gm_state == 'right':
        px.set_dir_servo_angle(-LINE_TRACK_ANGLE_OFFSET)
        px.forward(speed) 
    else:
        outHandle()

# sound effect and music
# =================================================================
class Music:
    def __init__(self):
        from robot_hat import Music
        
        self.music = Music()
        self.sound_thread = None
        self.music_path = None
        self.volume = 100

    def play_sound(self, file_path):
        self.music.sound_play(filename=file_path, volume=self.volume)

    def play_sound_background(self, file_path, volume=100):
        global sound_thread
        sound_thread = threading.Thread(target=self.music.sound_play, kwargs={
            "filename": file_path,
            "volume": volume
            }
        )
        sound_thread.start()

    def play_music_background(self, file_path):
        self.music_path = file_path
        self.music.music_play(file_path)

    def music_control(self, action):
        if action == 0: # 'stop'
            self.music.music_stop()
        elif action == 2: # 'pause'
            self.music.music_pause()
        elif action == 1: # 'resume'
            self.music.music_resume()

    def set_music_volume(self, volume):
        if volume > 100:
            volume = 100
        elif volume < 0:
            volume = 0
        self.volume = volume
        self.music.music_set_volume(volume)

    def get_music_busy(self):
        return self.music.pygame.mixer.music.get_busy()
    
    def get_music_length(self, file_path=None):
        if file_path is None:
            file_path = self.music_path
        sound = self.music.pygame.mixer.Sound(file_path)
        return int(sound.get_length())

    def get_music_pos(self):
        return int(self.music.pygame.mixer.music.get_pos() / 1000)
    
    def get_sound_busy(self):
        if self.sound_thread is None:
            return False
        if self.sound_thread.is_alive():
            return True
        else:
            return False
        
# calibration
# ================================================================
picarx_servos_offset = [0, 0, 0] # [dir_offset, cam_pan_offset, cam_tilt_offset]

def  init_picarx_servos_offset(px):
    global picarx_servos_offset
    _dir_offset = px.dir_cali_val
    _cam_pan_offset = px.cam_pan_cali_val
    _cam_tilt_offset = px.cam_tilt_cali_val
    picarx_servos_offset = [_dir_offset, _cam_pan_offset, _cam_tilt_offset]

def set_picarx_servos_offset(px, servo_index, option):
    global picarx_servos_offset
    if option == 1: # increase
        picarx_servos_offset[servo_index] += 1
    elif option == -1: # decrease
        picarx_servos_offset[servo_index] -= 1

    if servo_index == 0: # dir
        px.dir_servo_pin.angle(picarx_servos_offset[servo_index])
    elif servo_index == 1: # cam_pan
        px.cam_pan_servo_pin.angle(picarx_servos_offset[servo_index])
    elif servo_index == 2: # cam_tilt
        px.cam_tilt_servo_pin.angle(picarx_servos_offset[servo_index])

def save_picarx_servos_offset(px):
    global picarx_servos_offset
    px.dir_servo_calibrate(picarx_servos_offset[0])
    px.cam_pan_servo_calibrate(picarx_servos_offset[1])
    px.cam_tilt_servo_calibrate(picarx_servos_offset[2])
