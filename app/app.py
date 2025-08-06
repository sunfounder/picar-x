from mammoth_websocket.mammoth_websocket import MammothWebSocket
from mammoth_websocket.utils import get_ips

from picarx.picarx import PiCarX
from picarx.tts import TTS
from picarx.music import SoundFiles, music_list, sound_list
from picarx.utils import *
from picarx.auto_drive import LineTracking, ObstacleAvoidance, Following
from picarx.openai_helper import OpenAiHelper, AIStatus

import speech_recognition as sr
import signal

import json
from vilib import Vilib
import cv2

import time
import logging
import threading

import wave
from io import BytesIO
import os

# --- debug ---
# import psutil
# import os
# pid = os.getpid()
# process = psutil.Process(pid)

# global variables
# =================================================================
VERSION = "0.0.1"

DEVICE_INFO = {
    "Name": "PiCar-X",
    "Type": "PiCar-X",
    "Check": "MC",
    "Version": VERSION,
    "video": "",
}

CHECK_WIFI_EVERY = 5 # seconds
CAMERA_SIZE = (800, 600)

COLOR_DETECTION_COMMANDS = ['close','red','orange','yellow','green','blue','purple']
TRAFFIC_SIGNS =  ['none', 'stop', 'right', 'left', 'forward']

ws = MammothWebSocket()
car = PiCarX()
piper = TTS()
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.16
recognizer.dynamic_energy_ratio = 1.6
# recognizer.pause_threshold = 1
log = logging.getLogger("PiCar-X")
data_interval = 5 # miliseconds
openai = None

line_tracking = LineTracking(car, log=log)
obstacle_avoidance = ObstacleAvoidance(car, log=log)
following = Following(car, log=log)

#----
ai_api_key = None
ai_assistant_id = None
ai_listen_language = "auto"
ai_say_voice = "alloy"
ai_status = AIStatus.NOT_INITIALIZED
# ai_status = AIStatus.IDLE
ai_listen_result = None
ai_think_result = None
ai_error = ""
color_detection_mode = "close"
face_detection_enable = False
traffic_sign_detection_enable = False
qr_code_detection_enable = False
motor_power = 0
steering_angle = 0
camera_pan_angle = 0
camera_tilt_angle = 0
grayscale_calibrate_light_data = None
grayscale_calibrate_dark_data = None
music_index = None
button_pressed = False
button_pressed_for = 0
button_pressed_at = 0
connected = False
connected_changed = False
check_wifi_time = 0

data_received = {}
data_to_send = {}
data_rec_lock = threading.Lock()

delay_stop_motor_timer = None

'''
SGBRG10_CSI2P,640x480/0 - Score: 3296
SGBRG10_CSI2P,1296x972/0 - Score: 1000
SGBRG10_CSI2P,1920x1080/0 - Score: 1349.67
SGBRG10_CSI2P,2592x1944/0 - Score: 1567
'''

class Timer():
    def __init__(self):
        self.start = None
        self.end = None

    def print(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            # 计算函数运行的间隔
            interval = None
            if self.start is not None:
                interval = start - self.start
                interval = round(interval*1000, 2)
            self.start = start

            result = func(*args, **kwargs)
            self.end = time.time()
            duration = self.end - self.start
            duration = round(duration*1000, 2)
            if interval is None:
                print(f"[{duration:>6}] {func.__name__}")
            else:
                print(f"[{interval:>6}, {duration:>6}] {func.__name__}")
            return result
        return wrapper

update_data_timer = Timer()

def init_openai():
    global openai, ai_status, ai_error
    ai_status = AIStatus.INITIALIZING
    ai_error = ""
    log.info(f"Init OpenAI with API Key: {ai_api_key} and Assistant ID: {ai_assistant_id}")
    try:
        openai = OpenAiHelper(ai_api_key, ai_assistant_id, 'picar-x')
        ai_status = AIStatus.IDLE
    except Exception as e:
        log.error(f"OpenAI init failed: {e}")
        ai_error = f"[ERROR] {str(e)}"
        ai_status = AIStatus.FAILED
        return False
    return True

def check_openai():
    global ai_error
    if ai_status == AIStatus.NOT_INITIALIZED:
        log.error("Open AI not initialized")
        ai_error = "[ERROR] Open AI not initialized"
        return False
    elif ai_status != AIStatus.IDLE:
        log.warning(f"Open AI is {ai_status}, wait...")
        ai_error = f"[WARNING] Open AI is {ai_status}, wait..."
        for _ in range(10):
            if ai_status == AIStatus.IDLE:
                log.info(f"Open AI init done")
                return True
            time.sleep(1)
        if ai_status != AIStatus.IDLE:
            log.error(f"Open AI init timeout")
            ai_error = "[ERROR] Open AI init timeout"
            return False

    return True
    
def ai_listen_task():
    global ai_status, ai_listen_result
    if not check_openai():
        return
    
    # recording audio
    ai_status = AIStatus.LISTENING
    log.debug(f"Start listening...")
    for _ in range(10):
        with sr.Microphone(chunk_size=8192) as source:
            cancel_redirect_error() # restore error print
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

            wav_data = BytesIO(audio.get_wav_data())
            wav_data.name = "stt_output.wav"
            
            file = "./stt_output.wav"
            with wave.open(file, "wb") as wf:
                wf.setnchannels(1)  # 单声道
                wf.setsampwidth(audio.sample_width)  # 采样宽度（来自AudioData）
                wf.setframerate(audio.sample_rate)  # 采样率（来自AudioData）
                wf.writeframes(audio.get_wav_data())

            # os.system("aplay ./stt_output.wav")

        # stt
        log.debug(f"Converting audio to text...")
        ai_status = AIStatus.STT
        result = openai.stt(audio, language=ai_listen_language)
        result = result.strip()
        if len(result) == 0:
            log.warning(f"Listen result empty, try again...")
            continue
        ai_listen_result = result
        log.debug(f"Listen result: {result}")
        ai_status = AIStatus.IDLE
        break

def ai_think_task(value, with_image=False):
    global ai_status, ai_think_result
    if not check_openai():
        return
    
    content = value.strip()
    if len(content) == 0:
        log.error(f"Invalid think content: {content}")
        return

    ai_status = AIStatus.THINKING
    log.debug(f"Think with: {content}, with image: {with_image}")
    if with_image:
        img_path = './img_imput.jpg'
        cv2.imwrite(img_path, Vilib.img)
        response = openai.dialogue_with_img(content, img_path)
    else:
        response = openai.dialogue(content)
    if len(response) > 65535:
        log.warning(f"think result is too long, {len(response)} > 65535, cut to 65535")
        response = response[:65535]
    log.debug(f"Think result: {response}")
    ai_status = AIStatus.IDLE
    ai_think_result = response

def ai_say_task(value):
    global ai_status
    if not check_openai():
        return

    content = value.strip()
    if len(content) == 0:
        log.error(f"Invalid speak content: {content}")
        return

    ai_status = AIStatus.TTS
    log.debug(f"speak: [{content}]")
    gain = 3
    timestamp = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
    filename = f"./tts/{timestamp}_raw.wav"
    status = openai.text_to_speech(content, filename, ai_say_voice, response_format='wav')
    # software volume gain
    if status:
        ai_status = AIStatus.SPEAKING
        new_filename = f"./tts/{timestamp}_{gain}dB.wav"
        status = volume_gain(filename, new_filename, gain)
        if status:
            car.music.play_sound(new_filename)
    # Cleanup tts files
    if status:
        os.remove(filename)
        os.remove(new_filename)
    ai_status = AIStatus.IDLE

def piper_say_task(value):
    data_to_send["piper_saying"] = True
    start = time.time()
    if not piper.model_downloaded():
        log.info(f"Downloading piper model:{piper.model}")
        piper.download_model()
    piper.say(value)
    duration = round(time.time() - start, 3)
    log.debug(f"piper_say done in {duration} s")
    data_to_send["piper_saying"] = False

# --- handler functions ---
def handle_name_changed(name):
    DEVICE_INFO["Name"] = name
    log.debug(f"Name changed to {name}")
    car.set_name(name)

def handle_ai_api_key(value):
    global ai_api_key
    if ai_api_key == value:
        return
    DEVICE_INFO["ai_api_key"] = value
    car.config.set("ai_api_key", value)
    log.debug(f"Set api-key: {value}")
    ai_api_key = value

def handle_motor(power):
    global motor_power
    log.debug(f"Set motor power: {power}")
    if motor_power != power:
        car.forward(power)
        motor_power = power
        data_to_send["motor_power"] = power

def handle_steering(angle):
    global steering_angle
    angle = constrain(angle, -30, 30)
    log.debug(f"Set steering angle: {angle}")
    if angle!= steering_angle:
        car.set_steering_angle(angle)
        steering_angle = angle
        data_to_send["steering_angle"] = angle

def handle_camera_pan(angle):
    global camera_pan_angle
    angle = constrain(angle, -90, 90)
    log.debug(f"Set camera pan angle: {angle}")
    if angle!= camera_pan_angle:
        car.set_camera_pan_angle(angle)
        camera_pan_angle = angle
        data_to_send["camera_pan_angle"] = angle

def handle_camera_tilt(angle):
    global camera_tilt_angle
    angle = constrain(angle, -30, 30)
    log.debug(f"Set camera tilt angle: {angle}")
    if angle!= camera_tilt_angle:
        car.set_camera_tilt_angle(angle)
        camera_tilt_angle = angle
        data_to_send["camera_tilt_angle"] = angle

def handle_color_detection(mode_index):
    global color_detection_mode
    try:
        mode = COLOR_DETECTION_COMMANDS[mode_index]
    except KeyError:
        log.error(f"Invalid color detection mode: {mode_index}")
        return
    log.debug(f"Set color detection mode: {mode}")
    Vilib.color_detect(mode)
    color_detection_mode = mode

def handle_face_detection(enable):
    global face_detection_enable
    log.debug(f"Set face detection: {enable}")
    Vilib.face_detect_switch(enable)
    face_detection_enable = enable

def handle_traffic_sign_detection(enable):
    global traffic_sign_detection_enable
    log.debug(f"Set traffic sign detection: {enable}")
    Vilib.traffic_detect_switch(enable)
    traffic_sign_detection_enable = enable

def handle_qr_code_detection(enable):
    global qr_code_detection_enable
    log.debug(f"Set QR code detection: {enable}")
    Vilib.qrcode_detect_switch(enable)
    qr_code_detection_enable = enable

def handle_play_sound(index):
    if car.music.is_sound_busy():
        log.error(f"Sound effect is busy")
        return
    try:
        sound_file = sound_list[index]
    except IndexError:
        log.error(f"Invalid sound effect index: {index}")
        return
    log.debug(f"Play sound effect: {index} {sound_file}")
    car.music.play_sound_background(sound_file)

def handle_play_music(index):
    global music_index
    try:
        music_file = music_list[index]
    except IndexError:
        log.error(f"Invalid music index: {index}")
        return

    if index == music_index and car.music.is_music_busy():
        log.warning(f"Music {index} {music_file} is already playing")
        return
        
    log.debug(f"Play music: {index} {music_file}")
    data_to_send["music_length"] = car.music.get_music_length(music_file)
    music_index = index
    car.music.play_music_background(music_file)

def handle_music_control(control):
    log.debug(f"Music control: {control}")
    car.music.music_control(control)

def handle_music_volume(volume):
    volume = constrain(volume, 0, 100)
    log.debug(f"Set volume: {volume}")
    data_to_send["volume"] = volume
    car.music.set_volume(volume)

def handle_line_tracking(enable):
    if enable == 0:
        log.debug(f"Stop line tracking")
        line_tracking.stop()
    elif enable == 1:
        log.debug(f"Start line tracking")
        line_tracking.start()

def handle_line_tracking_power(power):
    log.debug(f"Set line tracking power: {power}")
    line_tracking.set_power(power)

def handle_obstacle_avoidance(enable):
    if enable == 0:
        log.debug(f"Stop obstacle avoidance")
        obstacle_avoidance.stop()
    elif enable == 1:
        log.debug(f"Start obstacle avoidance")
        obstacle_avoidance.start()

def handle_obstacle_avoidance_power(power):
    log.debug(f"Set obstacle avoidance power: {power}")
    obstacle_avoidance.set_power(power)

def handle_following(enable):
    if enable == 0:
        log.debug(f"Stop following")
        following.stop()
    elif enable == 1:
        log.debug(f"Start following")
        following.start()

def handle_following_power(power):
    log.debug(f"Set following power: {power}")
    following.set_power(power)

def handle_following_mode(mode):
    log.debug(f"Set following mode: {mode}")
    try:
        following.set_mode(mode)
    except ValueError as e:
        log.error(f"Invalid following mode: {mode}, err: {e}")

def handle_steering_offset(offset):
    offset = constrain(offset, -20, 20)
    offset = round(offset, 2)
    log.debug(f"Set steering offset: {offset}")
    car.set_steering_offset(offset)
    data_to_send['steering_offset'] = offset

def handle_camera_pan_offset(offset):
    offset = constrain(offset, -20, 20)
    offset = round(offset, 2)
    log.debug(f"Set camera pan offset: {offset}")
    car.set_camera_pan_offset(offset)
    data_to_send['camera_pan_offset'] = offset

def handle_camera_tilt_offset(offset):
    offset = constrain(offset, -20, 20)
    offset = round(offset, 2)
    log.debug(f"Set camera tilt offset: {offset}")
    car.set_camera_tilt_offset(offset)
    data_to_send['camera_tilt_offset'] = offset

def handle_motors_reverse(data):
    global delay_stop_motor_timer
    left_reverse, right_reverse = data
    log.debug(f"Set motors reverse: [{left_reverse}, {right_reverse}]")
    car.set_left_motor_reverse(left_reverse)
    car.set_right_motor_reverse(right_reverse)
    data_to_send['motor_reverse'] = [left_reverse, right_reverse]
    car.forward(30)
    if delay_stop_motor_timer is not None:
        delay_stop_motor_timer.cancel()
    delay_stop_motor_timer = threading.Timer(2, lambda: car.stop())
    delay_stop_motor_timer.start()

def handle_grayscale_calibration(data):
    light, dark = data
    if not isinstance(light, list):
        log.error(f"light must be list, light: {light}")
        return
    if not isinstance(dark, list):
        log.error(f"dark must be list, dark: {dark}")
        return
    log.debug(f"Set grayscale calibration, light: {light}, dark: {dark}")
    if min(light) < max(dark):
        log.error(f"light must larger than dark, light: {light}, dark: {dark}")
        return
    car.calibrate_grayscale(light, dark)

def handle_grayscale_cliff_threshold(value):
    log.debug(f"Set grayscale cliff threshold: {value}")
    data_to_send['grayscale_cliff_threshold'] = value
    car.grayscale.set_cliff_threshold(value)

def handle_ai_assistant_id(value):
    global ai_assistant_id
    if ai_assistant_id == value:
        return
    log.debug(f"Set assistant-id: {value}")
    ai_assistant_id = value

def handle_ai_init(enable):
    global ai_error
    log.debug(f"Init OpenAI: {enable}")
    if enable == 0:
        return
    
    if ai_api_key is None or ai_api_key == '' \
        or ai_assistant_id is None or ai_assistant_id == '':
        ai_error = "[ERROR] API Key or Assistant ID is empty"
        return False
    
    if ai_status == AIStatus.INITIALIZING:
        log.warning(f"Open AI is initializing")
        ai_error = "[ERROR] Open AI is initializing"
        return False
    
    if ai_status in [AIStatus.NOT_INITIALIZED, AIStatus.FAILED]:
        task = threading.Thread(target=init_openai)
        task.start()
        return True

    log.warning(f"Open AI is already initialized")
    return True

def handle_ai_say_voice(value):
    global ai_say_voice
    ai_say_voice = value
    log.debug(f"Set speak voice: {ai_say_voice}")

def handle_ai_listen_language(value):
    global ai_listen_language
    ai_listen_language = value
    log.debug(f"Set listen language: {ai_listen_language}")

def handle_ai_listen(enable):
    if not check_openai():
        return
    if enable == 0:
        return

    task = threading.Thread(target=ai_listen_task)
    task.start()

def handle_ai_think(value, with_image=False):
    if not check_openai():
        return
    
    if len(value) == 0:
        log.error(f"Invalid think content: {content}")
        return

    task = threading.Thread(target=ai_think_task, args=(value, with_image))
    task.start()

def handle_ai_think_with_image(value):
    handle_ai_think(value, with_image=True)

def handle_ai_say(value):
    log.debug(f"handle_ai_say: {value}")
    # if not check_openai():
    #     return

    if len(value) == 0:
        log.error(f"Invalid speak content: {value}")
        return

    task = threading.Thread(target=ai_say_task, args=(value,))
    task.start()

def handle_do_action(action):
    if action not in car.actions:
        log.error(f"Invalid action: {action}")
        return
    
    data_to_send['action_status'] = True
    car.actions[action]()
    data_to_send['action_status'] = False

def handle_led(status):
    if status not in [0, 1]:
        log.error(f"Invalid led status: {status}")
        return
    log.debug(f"Set led: {status}")
    car.set_user_led(status)

def handle_piper_set_model(model):
    log.debug(f"Set piper model: {model}")
    piper.set_model(model)
    data_to_send['piper_model'] = model

def handle_piper_say(value):
    log.debug(f"handle_piper_say: {value}")
    task = threading.Thread(target=piper_say_task, args=(value,))
    task.start()

DEVICE_INFO_MAP = {
    "name": handle_name_changed,
    "ai_api_key": handle_ai_api_key,
}

COMMAND_MAP = {
    # Robot control
    "motor": handle_motor,
    "steering": handle_steering,
    "camera_pan": handle_camera_pan,
    "camera_tilt": handle_camera_tilt,
    # Camera detection
    "color_detection": handle_color_detection,
    "face_detection": handle_face_detection,
    "traffic_sign_detection": handle_traffic_sign_detection,
    "qr_code_detection": handle_qr_code_detection,
    # Sound and music
    "play_sound": handle_play_sound,
    "play_music": handle_play_music,
    "music_control": handle_music_control,
    "music_volume": handle_music_volume,
    # Auto drive
    "line_tracking": handle_line_tracking,
    "line_tracking_power": handle_line_tracking_power,
    "obstacle_avoidance": handle_obstacle_avoidance,
    "obstacle_avoidance_power": handle_obstacle_avoidance_power,
    "following": handle_following,
    "following_power": handle_following_power,
    "following_mode": handle_following_mode,
    # Calibration
    "steering_offset": handle_steering_offset,
    "camera_pan_offset": handle_camera_pan_offset,
    "camera_tilt_offset": handle_camera_tilt_offset,
    "motor_reverse": handle_motors_reverse,
    "grayscale_calibration": handle_grayscale_calibration,
    "grayscale_cliff_threshold": handle_grayscale_cliff_threshold,
    # AI
    "ai_api_key": handle_ai_api_key,
    "ai_assistant_id": handle_ai_assistant_id,
    "ai_init": handle_ai_init,
    "ai_listen_language": handle_ai_listen_language,
    "ai_say_voice": handle_ai_say_voice,
    "ai_listen": handle_ai_listen,
    "ai_think": handle_ai_think,
    "ai_think_with_image": handle_ai_think_with_image,
    "ai_say": handle_ai_say,
    # Others
    "piper_set_model": handle_piper_set_model,
    "piper_say": handle_piper_say,
    "do_action": handle_do_action,
    "led": handle_led,
}

def handle_received_data():
    global data_received

    rec = {}
    with data_rec_lock:
        rec = data_received
        data_received = {}

    # if rec != {}:
    #     log.debug(f"Received data: {rec}")

    if 'ai_say' in rec.keys():
        print(f"AI say:  {rec['ai_say']}")

    for command in rec.keys():
        if command not in COMMAND_MAP:
            log.error(f"Invalid command: {command}")
            continue
        data = rec[command]
        if data is not None:
            COMMAND_MAP[command](rec[command])


async def handle_io_data(data):
    global data_received

    # Save received data
    with data_rec_lock:
        data_received.update(data)

    # pack data and send
    data = { "io_data": data_to_send }
    data = json.dumps(data)
    # Add data header
    data = f'DATA+{data}'
    await ws.send(data)
    clear_once_data_to_send()

async def handle_device_config(commands):
    log.debug("device changed")
    for command, value in commands.items():
        if command not in DEVICE_INFO_MAP:
            log.error(f"Invalid command: {command}")
            continue
        DEVICE_INFO_MAP[command](value)

async def handle_connected(client_ip):
    global connected, connected_changed
    connected = True
    connected_changed = True
    log.info(f"Client {client_ip} connected")

async def handle_disconnected():
    global connected, connected_changed
    connected = False
    connected_changed = True
    log.debug("handle_disconnected")

    # Reset robot
    car.stop()
    car.set_steering_angle(0)
    car.set_camera_pan_angle(0)
    car.set_camera_tilt_angle(0)

def handle_restart_service(delay=0):
    log.info(f"Restart service in {delay}s")
    blink_delay = 0.1
    for_count = int(delay / blink_delay / 2)
    for _ in range(for_count):
        car.set_user_led(1)
        time.sleep(blink_delay)
        car.set_user_led(0)
        time.sleep(blink_delay)
    log.info("Restart service")
    os.system("systemctl restart picar-x-app.service")

def get_button_status():
    global button_pressed, button_pressed_for, button_pressed_at
    pressed = bool(car.get_usr_btn())

    if pressed == True:
        if button_pressed == False:
            button_pressed = True
            button_pressed_at = time.time()
        else:
            button_pressed_for = time.time() - button_pressed_at
            if button_pressed_for > 5:
                log.debug("Press button for 5s, restart service")
                handle_restart_service(delay=2)
    else:
        if button_pressed == True:
            button_pressed = False
            button_pressed_for = 0
            button_pressed_at = 0

    return pressed

# @update_data_timer.print
def update_data():
    global ai_listen_result, ai_think_result

    # Read sensor data
    data_to_send["ultrasonic_distance"] = car.get_distance()
    data_to_send["battery_voltage"] = car.get_battery_voltage()
    data_to_send["charge_state"] = car.get_charge_state()
    data_to_send["user_button_pressed"] = get_button_status()

    # Grayscale data
    raw_grayscale_data = car.get_grayscale_data(raw=True)
    grayscale_data = car.grayscale.calibrate_data(raw_grayscale_data)
    data_to_send["grayscale_data"] = grayscale_data
    data_to_send["grayscale_data_raw"] = raw_grayscale_data
    data_to_send["is_on_line"] = car.is_on_line(data=grayscale_data)
    data_to_send["is_on_cliff"] = car.is_on_cliff(data=grayscale_data)
    data_to_send["line_position"] = car.get_line_position(data=grayscale_data)

    # Color detection data
    if color_detection_mode != "close":
        data_to_send["color_detection"] = {
            "x": int(Vilib.color_obj_parameter['x']),
            "y": int(Vilib.color_obj_parameter['y']),
            "w": int(Vilib.color_obj_parameter['w']),
            "h": int(Vilib.color_obj_parameter['h']),
            "n": int(Vilib.color_obj_parameter['n']),
        }
    else:
        if 'color_detection' in data_to_send:
            del data_to_send['color_detection']

    # Face detection data
    if face_detection_enable == True:
        data_to_send["face_detection"] = {
            "x": int(Vilib.face_obj_parameter['x']),
            "y": int(Vilib.face_obj_parameter['y']),
            "w": int(Vilib.face_obj_parameter['w']),
            "h": int(Vilib.face_obj_parameter['h']),
            "n": int(Vilib.face_obj_parameter['n']),
        }
    else:
        if 'face_detection' in data_to_send:
            del data_to_send['face_detection']

    # Traffic sign detection data
    if traffic_sign_detection_enable == True:
        data_to_send["traffic_sign_detection"] = {
            "x": int(Vilib.traffic_sign_obj_parameter['x']),
            "y": int(Vilib.traffic_sign_obj_parameter['y']),
            "w": int(Vilib.traffic_sign_obj_parameter['w']),
            "h": int(Vilib.traffic_sign_obj_parameter['h']),
            "t": str(Vilib.traffic_sign_obj_parameter['t']),
        }
    else:
        if 'traffic_sign_detection' in data_to_send:
            del data_to_send['traffic_sign_detection']

    # QR code detection data
    if qr_code_detection_enable == True:
        data = str(Vilib.qrcode_obj_parameter['data'])
        if data != "None":
            data_to_send["qr_code_detection"] = {
                "x": int(Vilib.qrcode_obj_parameter['x']),
                "y": int(Vilib.qrcode_obj_parameter['y']),
                "w": int(Vilib.qrcode_obj_parameter['w']),
                "h": int(Vilib.qrcode_obj_parameter['h']),
                "d": data,
            }
            print(data_to_send["qr_code_detection"])
    else:
        if 'qr_code_detection' in data_to_send:
            del data_to_send['qr_code_detection']

    # Sound status
    data_to_send["sound_status"] = int(car.music.is_sound_busy())

    # Music status
    data_to_send["music_status"] = int(car.music.is_music_busy())
    if car.music.is_music_busy():
        data_to_send["music_position"] = car.music.get_music_pos()

    # AI status
    data_to_send["ai_status"] = ai_status.value
    data_to_send["ai_error"] = ai_error
    if ai_listen_result is not None:
        data_to_send["ai_listen_result"] = ai_listen_result
        ai_listen_result = None
    if ai_think_result is not None:
        data_to_send["ai_think_result"] = ai_think_result
        ai_think_result = None

def set_log():
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s', datefmt='%y/%m/%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

def clear_once_data_to_send():
    if 'ai_listen_result' in data_to_send:
        del data_to_send['ai_listen_result']
    if 'ai_think_result' in data_to_send:
        del data_to_send['ai_think_result']
    if 'color_detection' in data_to_send:
        del data_to_send['color_detection']
    if 'face_detection' in data_to_send:
        del data_to_send['face_detection']
    if 'traffic_sign_detection' in data_to_send:
        del data_to_send['traffic_sign_detection']
    if 'qr_code_detection' in data_to_send:
        del data_to_send['qr_code_detection']
    if 'music_position' in data_to_send:
        del data_to_send['music_position']

def init():
    global ai_api_key
    set_log()

    ips = get_ips()
    log.debug(f"IPs: {ips}")
    ip = '0.0.0.0'
    if 'wlan0' in ips:
        ip = ips['wlan0']
    elif 'eth0' in ips:
        ip = ips['eth0']

    DEVICE_INFO["Name"] = car.name
    DEVICE_INFO["video"] = f"{ip}:9000/mjpg"
    ai_api_key = car.config.get("ai_api_key", default_value="")
    DEVICE_INFO["ai_api_key"] = ai_api_key

    log.info(json.dumps(DEVICE_INFO, indent=4))
    car.reset()
    # --- Init Vilib ---
    try:
        Vilib.camera_start(vflip=False, hflip=False, size=CAMERA_SIZE)
        Vilib.show_fps()
        Vilib.display(local=False,web=True)
    except Exception as e:
        vilib_obj_error.add(str(e))
        log.exception(str(e))

    # --- Init Websocket ---
    ws.set_device_info(DEVICE_INFO)
    ws.set_device_config_handler(handle_device_config)
    ws.set_io_data_handler(handle_io_data)
    ws.set_connect_handler(handle_connected)
    ws.set_disconnect_handler(handle_disconnected)
    ws.start()

    # --- Get initial data ---
    data_to_send['motor_reverse'] = [car.motors.left_reversed, car.motors.right_reversed]
    data_to_send['steering_offset'] = car.steering_servo.offset()
    data_to_send['camera_pan_offset'] = car.camera_pan_servo.offset()
    data_to_send['camera_tilt_offset'] = car.camera_tilt_servo.offset()
    data_to_send['grayscale_cliff_threshold'] = car.grayscale.cliff_threshold
    data_to_send['volume'] = car.music.get_volume()
    data_to_send['motor_power'] = 0
    data_to_send['steering_angle'] = 0
    data_to_send['camera_pan_angle'] = 0
    data_to_send['camera_tilt_angle'] = 0
    data_to_send['piper_model'] = piper.model
    data_to_send['piper_saying'] = False
    data_to_send['grayscale_calibration_data'] = car.get_grayscale_calibration_data()
    data_to_send['action_status'] = False

    # --- setup signal handler ---
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

def handle_signal(signal, frame):
    log.info(f"Received signal {signal}")
    close()

def check_wifi():
    global check_wifi_time
    # Get wifi interface ip with command
    if time.time() - check_wifi_time < CHECK_WIFI_EVERY:
        return True
    check_wifi_time = time.time()
    ips = get_ips()
    if 'wlan0' not in ips:
        return False

    return True

def check_connection():
    if not check_wifi():
        return False
    return True

def main():
    global connected_changed

    init()

    start = time.time()
    car.music.play_sound(SoundFiles.START_ENGINE)
    while True:
        if not check_wifi():
            log.error("No wifi connection, try restart wifi")
            os.system("sudo nmcli device down wlan0")
            car.set_user_led(1)
            time.sleep(0.5)
            car.set_user_led(0)
            time.sleep(0.5)
            car.set_user_led(1)
            time.sleep(0.5)
            car.set_user_led(0)
            os.system("sudo nmcli device up wlan0")
            time.sleep(2)
            continue
        if connected_changed:
            connected_changed = False
            if connected:
                car.set_user_led(0)
        if not connected:
            car.set_user_led(1)
            time.sleep(1)
            car.set_user_led(0)
            time.sleep(1)
            continue
        handle_received_data()
        update_data()
        delay = time.time() - start
        delay = delay * 1000
        delay = data_interval - delay
        delay = max(delay, 0)
        time.sleep(delay)

def close():
    log.info("Exiting")
    ws.close()
    Vilib.camera_close()
    car.close()
    exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.debug("KeyboardInterrupt")
    except Exception as e:
        log.exception(e)
    finally:
        close()
