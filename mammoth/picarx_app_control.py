from mammoth_websocket.mammoth_websocket import MammothWebSocket
from mammoth_websocket.utils import get_ips
from constants import color_detection_command, picarx_sounds, picarx_musics, traffic_sign_label, AIStatus, CAMERA_SIZE
from picarx_functions import *

from preset_actions import *
from picarx import Picarx

from openai_helper import OpenAiHelper
import speech_recognition as sr

from robot_hat.utils import get_battery_voltage
import json
from vilib import Vilib
import cv2

import time
import logging
import threading

from utils import *

# --- debug ---
import psutil
import os
pid = os.getpid()
process = psutil.Process(pid)

from blessed import Terminal
term = Terminal()

# global variables
# =================================================================
VERSION = "0.0.1"

DEVICE_INFO = {
    "Name": "Picar-X-001", ## TODO: get the name from the device
    "Type": "Picar-X",
    "Check": "MC",
    "Version": VERSION,
    "video": "",
}

ws = MammothWebSocket()
openai = None
px = Picarx()
music = Music()
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.16
recognizer.dynamic_energy_ratio = 1.6
recognizer.pause_threshold = 1
log = logging.getLogger("PiCar-X")

#----
ai_api_key = None
ai_assistant_id = None
ai_listen_language = "auto"
ai_say_voice = "alloy"
ai_status = AIStatus.NOT_INITIALIZED
ai_need_reinitialize = False
color_detection_mode = "close"
face_detection_enable = False
traffic_sign_detection_enable = False
qr_code_detection_enable = False
line_tracking_power = 80
obstacle_avoidance_power = 80
io_data = {}
grayscale_line_reference = 1000
grayscale_cliff_reference = 300

delay_stop_motor_timer = None

'''
SGBRG10_CSI2P,640x480/0 - Score: 3296
SGBRG10_CSI2P,1296x972/0 - Score: 1000
SGBRG10_CSI2P,1920x1080/0 - Score: 1349.67
SGBRG10_CSI2P,2592x1944/0 - Score: 1567
'''

def init_openai():
    global openai, ai_status
    if ai_api_key is None or ai_api_key == '' \
        or ai_assistant_id is None or ai_assistant_id == '':
        return False
    ai_status = AIStatus.INITIALIZING
    log.info(f"Init OpenAI with API Key: {ai_api_key} and Assistant ID: {ai_assistant_id}")
    openai = OpenAiHelper(ai_api_key, ai_assistant_id, 'picar-x')
    ai_status = AIStatus.IDLE
    return True

def check_openai():
    if ai_status == AIStatus.NOT_INITIALIZED:
        log.error("Open AI not initialized")
        return False
    elif ai_status != AIStatus.IDLE:
        log.warning(f"Open AI is not ready, wait...")
        for _ in range(10):
            if ai_status == AIStatus.IDLE:
                log.info(f"Open AI init done")
                return True
            time.sleep(1)
        if ai_status != AIStatus.IDLE:
            log.error(f"Open AI init timeout")
            return False

    return True
    
def listen_task():
    global ai_status
    if not check_openai():
        return
    
    # recording audio
    ai_status = AIStatus.LISTENING
    log.debug(f"Start listening...")
    with sr.Microphone(chunk_size=8192) as source:
        cancel_redirect_error() # restore error print
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # stt
    log.debug(f"Converting audio to text...")
    ai_status = AIStatus.STT
    result = openai.stt(audio, language=ai_listen_language)
    io_data['ai_listen_result'] = result
    log.debug(f"Listen result: {result}")
    ai_status = AIStatus.IDLE

def think_task(value, with_image=False):
    global ai_status
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
    io_data['ai_think_result'] = response

def say_task(value):
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
            music.play_sound(new_filename)
    # Cleanup tts files
    if status:
        os.remove(filename)
        os.remove(new_filename)
    ai_status = AIStatus.IDLE

# --- handler functions ---
def handle_name_changed(name):
    DEVICE_INFO["Name"] = name
    print(f"Name changed to {name}")
    px.config_file.set("name", name)

def handle_motor(left_power, right_power):
    left_power = constrain(left_power, -100, 100)
    right_power = constrain(right_power, -100, 100)
    log.debug(f"Set motor: [{left_power}, {right_power}]")
    px.set_motor_speed(1, left_power)
    px.set_motor_speed(2, right_power)

def handle_steering(angle):
    angle = constrain(angle, -30, 30)
    log.debug(f"Set steering angle: {angle}")
    px.set_dir_servo_angle(angle)

def handle_camera_pan(angle):
    angle = constrain(angle, -90, 90)
    log.debug(f"Set camera pan angle: {angle}")
    px.set_cam_pan_angle(angle)

def handle_camera_tilt(angle):
    angle = constrain(angle, -30, 30)
    log.debug(f"Set camera tilt angle: {angle}")
    px.set_cam_tilt_angle(angle)

def handle_color_detection(mode_index):
    global color_detection_mode
    try:
        mode = color_detection_command[mode_index]
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
    Vilib.traffic_light_detect_switch(enable)
    traffic_sign_detection_enable = enable

def handle_qr_code_detection(enable):
    global qr_code_detection_enable
    log.debug(f"Set QR code detection: {enable}")
    Vilib.qrcode_detect_switch(enable)
    qr_code_detection_enable = enable

def handle_sound(index):
    if music.get_sound_busy():
        log.error(f"Sound effect is busy")
        return
    try:
        sound_file = picarx_sounds[index]
    except IndexError:
        log.error(f"Invalid sound effect index: {index}")
        return
    log.debug(f"Play sound effect: {index} {sound_file}")
    music.play_sound_background(sound_file)

def handle_music(index):
    if music.get_sound_busy():
        log.error(f"Music is busy")
        return
    try:
        music_file = picarx_musics[index]
    except IndexError:
        log.error(f"Invalid music index: {index}")
        return
    log.debug(f"Play music: {index} {music_file}")
    io_data["music_length"] = music.get_music_length(music_file)
    music.play_music_background(music_file)

def handle_music_control(flag):
    log.debug(f"Music control: {flag}")
    music.music_control(flag)

def handle_music_volume(volume):
    volume = constrain(volume, 0, 100)
    log.debug(f"Set music volume: {volume}")
    music.set_music_volume(volume)

def handle_line_tracking(enable):
    if enable == 0:
        log.debug(f"Stop line tracking")
        px.stop()
    elif enable == 1:
        log.debug(f"Set line tracking power: {line_tracking_power}")
        line_track(line_tracking_power)

def handle_obstacle_avoidance(enable):
    if enable == 0:
        log.debug(f"Stop obstacle avoidance")
        px.stop()
    elif enable == 1:
        log.debug(f"Set obstacle avoidance power: {obstacle_avoidance_power}")
        avoid_obstacles(obstacle_avoidance_power)

def handle_steering_offset(offset):
    offset = constrain(offset, -20, 20)
    offset = round(offset, 2)
    log.debug(f"Set steering offset: {offset}")
    px.dir_servo_calibrate(offset)
    io_data['steering_offset'] = offset

def handle_camera_pan_offset(offset):
    offset = constrain(offset, -20, 20)
    offset = round(offset, 2)
    log.debug(f"Set camera pan offset: {offset}")
    px.cam_pan_servo_calibrate(offset)
    io_data['camera_pan_offset'] = offset

def handle_camera_tilt_offset(offset):
    offset = constrain(offset, -20, 20)
    offset = round(offset, 2)
    log.debug(f"Set camera tilt offset: {offset}")
    px.cam_tilt_servo_calibrate(offset)
    io_data['camera_tilt_offset'] = offset

def handle_motors_reverse(left_reverse, right_reverse):
    global delay_stop_motor_timer
    log.debug(f"Set motors reverse: [{left_reverse}, {right_reverse}]")
    px.motor_direction_calibrate(1, left_reverse)
    px.motor_direction_calibrate(2, right_reverse)
    io_data['motor_reverse'] = [left_reverse, right_reverse]
    px.forward(30)
    if delay_stop_motor_timer is not None:
        delay_stop_motor_timer.cancel()
    delay_stop_motor_timer = threading.Timer(2, lambda: px.stop())
    delay_stop_motor_timer.start()

def handle_ai_api_key(value):
    global ai_api_key
    log.debug(f"Set api-key: {value}")
    if ai_api_key == value:
        return
    ai_api_key = value
    task = threading.Thread(target=init_openai)
    task.start()
    
def handle_ai_assistant_id(value):
    global ai_assistant_id
    log.debug(f"Set assistant-id: {value}")
    if ai_assistant_id == value:
        return
    ai_assistant_id = value
    task = threading.Thread(target=init_openai)
    task.start()

def handle_ai_say_voice(value):
    global ai_say_voice
    ai_say_voice = value
    log.debug(f"Set speak voice: {ai_say_voice}")

def handle_ai_listen_language(value):
    global ai_listen_language
    ai_listen_language = value
    log.debug(f"Set listen language: {ai_listen_language}")

def handle_ai_listen():
    if not check_openai():
        return

    task = threading.Thread(target=listen_task)
    task.start()

def handle_ai_think(value, with_image=False):
    if not check_openai():
        return
    
    if len(value) == 0:
        log.error(f"Invalid think content: {content}")
        return

    task = threading.Thread(target=think_task, args=(value, with_image))
    task.start()

def handle_ai_say(value):
    if not check_openai():
        return

    if len(value) == 0:
        log.error(f"Invalid speak content: {value}")
        return

    task = threading.Thread(target=say_task, args=(value,))
    task.start()

def handle_do_action(action):
    if action not in actions_dict:
        log.error(f"Invalid action: {action}")
        return
    
    actions_dict[action](px)

def handle_led(status):
    if status not in [0, 1]:
        log.error(f"Invalid led status: {status}")
        return
    log.debug(f"Set led: {status}")
    px.led.value(status)

def on_io_data(data):
    global line_tracking_power, obstacle_avoidance_power
    # control
    if 'motor' in data.keys():
        handle_motor(*data['motor'])
    if 'steering' in data.keys():
        handle_steering(data['steering'])
    if 'camera_pan' in data.keys():
        handle_camera_pan(data['camera_pan'])
    if 'camera_tilt' in data.keys():
        handle_camera_tilt(data['camera_tilt'])
    if 'color_detection' in data.keys():
        handle_color_detection(data['color_detection'])
    if 'face_detection' in data.keys():
        handle_face_detection(data['face_detection'])
    if 'traffic_sign_detection' in data.keys():
        handle_traffic_sign_detection(data['traffic_sign_detection'])
    if 'qr_code_detection' in data.keys():
        handle_qr_code_detection(data['qr_code_detection'])
    # sound and music
    if 'play_sound' in data.keys():
        handle_sound(data['play_sound'])
    if 'play_music' in data.keys():
        handle_music(data['play_music'])
    if 'music_control' in data.keys():
        handle_music_control(data['music_control'])
    if 'music_volume' in data.keys():
        handle_music_volume(data['music_volume'])
    # track_mode
    if 'line_tracking' in data.keys():
        handle_line_tracking(data['line_tracking'])
    if 'line_tracking_power' in data.keys():
        line_tracking_power = data['line_tracking_power']
    # obstacle_mode
    if 'obstacle_avoidance' in data.keys():
        handle_obstacle_avoidance(data['obstacle_avoidance'])
    if 'obstacle_avoidance_power' in data.keys():
        obstacle_avoidance_power = data['obstacle_avoidance_power']
    # Calibrations
    if 'steering_offset' in data.keys():
        handle_steering_offset(data['steering_offset'])
    if 'camera_pan_offset' in data.keys():
        handle_camera_pan_offset(data['camera_pan_offset'])
    if 'camera_tilt_offset' in data.keys():
        handle_camera_tilt_offset(data['camera_tilt_offset'])
    # motors calibration
    if 'motor_reverse' in data.keys():
        handle_motors_reverse(*data['motor_reverse'])
    # GPT
    if 'ai_api_key' in data.keys():
        handle_ai_api_key(data['ai_api_key'])
    if 'ai_assistant_id' in data.keys():
        handle_ai_assistant_id(data['ai_assistant_id'])
    if 'ai_listen_language' in data.keys():
        handle_ai_listen_language(data['ai_listen_language'])
    if 'ai_say_voice' in data.keys():
        handle_ai_say_voice(data['ai_say_voice'])
    if 'ai_listen' in data.keys():
        handle_ai_listen()
    if 'ai_think' in data.keys():
        handle_ai_think(data['ai_think'])
    if 'ai_think_with_image' in data.keys():
        handle_ai_think(data['ai_think_with_image'], with_image=True)
    if 'ai_say' in data.keys():
        handle_ai_say(data['ai_say'])

    # do actions
    if 'do_action' in data.keys():
        handle_do_action(data['do_action'])
    if 'led' in data.keys():
        handle_led(*data['led'])

def on_device_config(commands):
    log.debug("device changed")
    for command, value in commands.items():
        log.debug(f"command: {command}, value: {value}")
        if command == 'name':
            handle_name_changed(value)

def on_connect(client_id):
    pass

def on_disconnect(client_id):
    pass

def update_data():
    # Read sensor data
    # Ultrasonic sensor data
    ultrasonic_distance = px.get_distance()
    value = int(ultrasonic_distance*10)
    io_data["ultrasonic_distance"] = value

    # Battery voltage
    battery_voltage = get_battery_voltage()
    battery_voltage = constrain(battery_voltage, 6.2, 8.4)
    io_data["battery_voltage"] = battery_voltage

    # Grayscale sensor data
    grayscale_value = px.get_grayscale_data()
    grayscale_status = []
    for data in grayscale_value:
        if data > grayscale_line_reference:
            grayscale_status.append(0)
        elif data > grayscale_cliff_reference:
            grayscale_status.append(1)
        else:
            grayscale_status.append(2)
    io_data["grayscale_value"] = grayscale_value
    io_data["grayscale_status"] = grayscale_status

    # Color detection data
    if color_detection_mode != "close":
        color_detect_result = [
            Vilib.color_obj_parameter['n'],
            Vilib.color_obj_parameter['x'],
            Vilib.color_obj_parameter['y'],
        ]
        io_data["color_detection"] = color_detect_result
    # Face detection data
    if face_detection_enable == True:
        face_detect_result = [
            Vilib.face_obj_parameter['n'],
            Vilib.face_obj_parameter['x'],
            Vilib.face_obj_parameter['y'],
        ]
        io_data["face_detection"] = face_detect_result
    # Traffic sign detection data
    if traffic_sign_detection_enable == True:
        traffic_sign = Vilib.traffic_sign_obj_parameter['t']
        traffic_sign_detect_result = [traffic_sign_label[traffic_sign]]
        io_data["traffic_sign_detection"] = traffic_sign_detect_result
    # QR code detection data
    if qr_code_detection_enable == True:
        result = [x['text'] for x in Vilib.detect_obj_parameter['qr_list']]
        io_data["qr_code_detection"] = result

    # Sound status
    io_data["sound_status"] = int(music.get_sound_busy())

    # Music status
    io_data["music_status"] = int(music.get_music_busy())
    if music.get_music_busy():
        io_data["music_position"] = music.get_music_pos()

    # AI status
    io_data["ai_status"] = ai_status.value

    # Button status
    io_data["button_pressed"] = int(px.btn.value() == 0)

def set_log():
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s.%(msecs)03d [%(levelname)s] %(message)s', datefmt='%y/%m/%d %H:%M:%S')
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)

def clean_io_data():
    if 'ai_listen_result' in io_data:
        del io_data['ai_listen_result']
    if 'ai_think_result' in io_data:
        del io_data['ai_think_result']

def init():
    set_log()

    ips = get_ips()
    log.debug(f"IPs: {ips}")
    ip = '0.0.0.0'
    if 'wlan0' in ips:
        ip = ips['wlan0']
    elif 'eth0' in ips:
        ip = ips['eth0']

    DEVICE_INFO["Name"] = px.config_file.get("name", default_value=DEVICE_INFO["Name"])
    DEVICE_INFO["video"] = f"{ip}:9000/mjpg"
    log.info(json.dumps(DEVICE_INFO, indent=4))
    px.reset()
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
    ws.set_on_connect(on_connect)
    ws.set_on_disconnect(on_disconnect)
    ws.set_on_device_config(on_device_config)
    ws.set_on_io_data(on_io_data)
    ws.start()

    io_data['motor_reverse'] = list.copy(px.cali_dir_value)
    io_data['steering_offset'] = px.dir_cali_val
    io_data['camera_pan_offset'] = px.cam_pan_cali_val
    io_data['camera_tilt_offset'] = px.cam_tilt_cali_val

def main():

    init()

    while True:
        update_data()
        ws.update_io_data(io_data)
        clean_io_data()
        time.sleep(0.02)


if __name__ == "__main__":
    try:
        main()
    # except KeyboardInterrupt:
    #     print("KeyboardInterrupt")
    # except Exception as e:
    #     print(e)
    finally:
        log.info("Exiting")
        ws.close()
        px.stop()
