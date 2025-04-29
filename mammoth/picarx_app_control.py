from mammoth_websocket.mammoth_websocket import MammothWebSocket
from mammoth_websocket.utils import get_ips
from picarx_entities import command_entities, sensor_entities
from picarx_entities import color_detection_command, picarx_sounds, picarx_musics, traffic_sign_label
from picarx_functions import *
from picarx import Picarx

from openai_helper import OpenAiHelper
import speech_recognition as sr

from robot_hat.utils import get_battery_voltage
import json
from vilib import Vilib
import cv2

import time

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

#----
status = ''
error = []
api_key = None
assistant_id = None

CAMERA_SIZE = (800, 600)

'''
SGBRG10_CSI2P,640x480/0 - Score: 3296
SGBRG10_CSI2P,1296x972/0 - Score: 1000
SGBRG10_CSI2P,1920x1080/0 - Score: 1349.67
SGBRG10_CSI2P,2592x1944/0 - Score: 1567
'''

def init_openai():
    global openai
    if api_key is None or api_key == '' \
        or assistant_id is None or assistant_id == '':
        return False
    print(f"Init OpenAI with API Key: {api_key} and Assistant ID: {assistant_id}")
    openai = OpenAiHelper(api_key, assistant_id, 'picar-x')
    sensor_entities.ai_initialized.value = 1
    return True

# --- handler functions ---

def handle_name_changed(name):
    DEVICE_INFO["Name"] = name
    print(f"Name changed to {name}")
    px.config_file.set("name", name)

def handle_motor(values):
    px.set_motor_speed(1, values[0])
    px.set_motor_speed(2, values[1])

def handle_steering(values):
    angle = values[0]
    # print(f"Handle Steering servo: {angle}")
    px.set_dir_servo_angle(angle)

def handle_camera_pan(values):
    angle = values[0]
    # print(f"Handle Camera Pan servo: {angle}")
    px.set_cam_pan_angle(values[0])

def handle_camera_tilt(values):
    angle = values[0]
    angle = constrain(angle, -20, 20)
    # print(f"Handle Camera Tilt servo: {angle}")
    px.set_cam_tilt_angle(values[0])

def handle_color_detection_switch(values):
    color = values[0]
    color_name = color_detection_command[color]
    # print(f"Handle Color Detection Switch: {color_name}")
    Vilib.color_detect(color_name)

def handle_face_detection_switch(values):
    Vilib.face_detect_switch(values[0])

def handle_traffic_sign_detection_switch(values):
    Vilib.traffic_detect_switch(values[0])

def handle_qr_code_detection_switch(values):
    Vilib.qrcode_detect_switch(values[0])

def handle_sound_effect(values):
    if music.get_sound_busy():
        print(f"[WARNING] sound effect is busy")
        return
    index = values[0] - 1
    if index not in range(len(picarx_sounds)):
        print(f"[WARNING] sound effect index out of range")
        return
    print(f"[INFO] play sound effect: {picarx_sounds[index]}")
    music.play_sound_effect(picarx_sounds[index])

def handle_music(values):
    if music.get_sound_busy():
        print(f"[WARNING] sound effect is busy")
        return
    index = values[0] - 1
    if index not in range(len(picarx_musics)):
        print(f"[WARNING] music index out of range")
        return
    print(f"[INFO] play music: {picarx_musics[index]}")
    music.play_music(picarx_musics[index])

def handle_music_control(values):
    music.music_control(values[0])

def handle_music_volume(values):
    music.set_music_volume(values[0])

def handle_track_mode(values):
    mode = values[0]
    speed = values[1]
    if mode == 0: # stop
        px.stop()
    elif mode == 1: # forward
        line_track(speed)

def handle_obstacle_mode(values):
    mode = values[0]
    speed = values[1]
    if mode == 0: # stop
        px.stop()
    elif mode == 1: # forward
        avoid_obstacles(speed)

def handle_servo_calibation(values):
    servo_index = values[0]
    direction = values[1]
    offset = None
    if servo_index == 0: # camera pan servo
        offset = px.cam_pan_cali_val + direction * 0.2
        offset = constrain(offset, -20, 20)
        px.cam_pan_servo_calibrate(offset)
    elif servo_index == 1: # camera tilt servo
        offset = px.cam_tilt_cali_val + direction * 0.2
        offset = constrain(offset, -20, 20)
        px.cam_tilt_servo_calibrate(offset)
    elif servo_index == 2: # dir servo 1
        offset = px.dir_cali_val + direction * 0.2
        offset = constrain(offset, -20, 20)
        px.dir_servo_calibrate(offset)
    if offset != None:
        sensor_entities.servos_offset.values[servo_index] = round(offset * 10, 0)

def handle_motors_calibation(values):
    px.motor_direction_calibrate(1, values[0])
    px.motor_direction_calibrate(2, values[1])
    px.forward(30)
    time.sleep(2)
    px.stop()
    sensor_entities.motors_offset.values = list(values)

def handle_set_api_key(value):
    global api_key
    if value != api_key:
        api_key = value
        print(f"[INFO] api-key: {api_key}")
        init_openai()
    
def handle_set_assistant_id(value):
    global assistant_id
    if value!= assistant_id:
        assistant_id = value
        print(f"[INFO] assistant-id: {assistant_id}")
        init_openai()

def handle_listen():
    if openai is None:
        if not init_openai():
            print("Open AI init error")
            return
    
    # recording audio
    with sr.Microphone(chunk_size=8192) as source:
        cancel_redirect_error() # restore error print
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # stt
    st = time.time()
    result = openai.stt(audio, language=LANGUAGE)
    if len(result) > 65535:
        print(f"[WARN] listen result is too long, {len(result)} > 65535, cut to 65535")
        result = result[:65535]
    sensor_entities.listen_result.values = result

def handle_think(value, with_image=False):
    
    if openai is None:
        if not init_openai():
            print("Open AI init error")
            return
    print(f"Think with: {value}, with image: {with_image}")
    if with_image:
        img_path = './img_imput.jpg'
        cv2.imwrite(img_path, Vilib.img)
        response = openai.dialogue_with_img(value, img_path)
    else:
        response = openai.dialogue(value)
    if len(response) > 65535:
        print(f"[WARN] think result is too long, {len(response)} > 65535, cut to 65535")
        response = response[:65535]
    print(f"Think result: {response}")
    sensor_entities.think_result.values = response

def handle_speak(value):
    if openai is None:
        if not init_openai():
            print("Open AI init error")
            return

    voice = "echo" # alloy, echo, fable, onyx, nova, and shimmer
    gain = 3
    timestamp = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
    filename = f"./tts/{timestamp}_raw.wav"
    status = openai.text_to_speech(value, filename, voice, response_format='wav')
    # software volume gain
    if status:
        new_filename = f"./tts/{timestamp}_{gain}dB.wav"
        status = volume_gain(filename, new_filename, gain)

def on_io_data(data):
    # control
    # ------------------------------------
    # --- motors ---
    if 'motor' in data.keys():
        values = data['motor']
        handle_motor(values)
    # --- steering servo ---
    if 'steering' in data.keys():
        values = data['steering']
        handle_steering(values)
    # --- camera pan servo ---
    if 'camera_pan' in data.keys():
        values = data['camera_pan']
        handle_camera_pan(values)
    # --- camera tilt servo ---
    if 'camera_tilt' in data.keys():
        values = data['camera_tilt']
        handle_camera_tilt(values)
        
    # vision processing
    # ------------------------------------
    # --- color detection ---
    if 'color_detection_switch' in data.keys():
        values = data['color_detection_switch']
        handle_color_detection_switch(values)
    # --- face detection ---
    if 'face_detection_switch' in data.keys():
        values = data['face_detection_switch']
        handle_face_detection_switch(values)
    # --- traffic sign detection ---
    if 'traffic_sign_detection_switch' in data.keys():
        values = data['traffic_sign_detection_switch']
        handle_traffic_sign_detection_switch(values)
    # --- qr code detection ---
    if 'qr_code_detection_switch' in data.keys():
        values = data['qr_code_detection_switch']
        handle_qr_code_detection_switch(values)

    # sound and music
    # ------------------------------------
    # --- sound effect ---
    if 'sound_effect' in data.keys():
        values = data['sound_effect']
        handle_sound_effect(values)
    # --- music ---
    if 'music' in data.keys():
        values = data['music']
        handle_music(values)
    # --- music control ---
    if 'music_control' in data.keys():
        values = data['music_control']
        handle_music_control(values)
    # --- music volume ---
    if 'music_volume' in data.keys():
        values = data['music_volume']
        handle_music_volume(values)

    # track_mode
    # ------------------------------------
    if 'track_mode' in data.keys():
        values = data['track_mode']
        handle_track_mode(values)
    # obstacle_mode
    # ------------------------------------
    if 'obstacle_mode' in data.keys():
        values = data['obstacle_mode']
        handle_obstacle_mode(values)

    # Calibrations
    # ------------------------------------
    # servos_calibration
    if 'servos_calibration' in data.keys():
        values = data['servos_calibration']
        handle_servo_calibation(values)
    # motors calibration
    if 'motors_calibration' in data.keys():
        values = data['motors_calibration']
        handle_motors_calibation(values)
    
    # GPT
    # ------------------------------------
    # set api-key
    if 'set_api_key' in data.keys():
        value = data['set_api_key']
        handle_set_api_key(value)
    # set assistant-id
    if 'set_assistant_id' in data.keys():
        value = data['set_assistant_id']
        handle_set_assistant_id(value)
    # listen
    if 'listen' in data.keys():
        handle_listen()
    # think
    if 'think' in data.keys():
        value = data['think']
        handle_think(value, with_image=False)
    if 'think_with_image' in data.keys():
        value = data['think_with_image']
        handle_think(value, with_image=True)
    # speak
    if 'speak' in data.keys():
        value = data['speak']
        handle_speak(value)

def on_device_config(commands):
    print("device changed")
    for command, value in commands.items():
        print(f"command: {command}, value: {value}")
        if command == 'name':
            handle_name_changed(value)

async def on_connect(**kwargs):
    # if 'client' in kwargs:
    #     client = kwargs['client']
    #     client_id = client['id']
    #     client_ip = client['ip']
    #     ws.send(DEVICE_INFO, client_id)
    # else:
    #     ws.send(DEVICE_INFO)
    print(f'on_connected: {kwargs}')
    pass

async def on_disconnect(**kwargs):
    pass

def update_data():
    # Read sensor data
    # Ultrasonic sensor data
    ultrasonic_distance = px.get_distance()
    value = int(ultrasonic_distance*10)
    sensor_entities.ultrasonic.value = value

    # Battery voltage
    battery_voltage = get_battery_voltage()
    if battery_voltage < 6:
        battery_voltage = 6
    elif battery_voltage > 8.5:
        battery_voltage = 8.5
    sensor_entities.battery_voltage.value = int((battery_voltage-6)*100)

    # Grayscale sensor data
    grayscale_data = px.get_grayscale_data()
    grayscale_status = []
    for data in grayscale_data:
        if data > 1000:
            grayscale_status.append(0)
        elif data > 300:
            grayscale_status.append(1)
        else:
            grayscale_status.append(2)
    sensor_entities.grayscale.values = grayscale_data
    sensor_entities.grayscale_status.values = list.copy(grayscale_status)

    # Color detection data
    if command_entities.color_detection_switch.value == 1:
        color_detect_result = [
            Vilib.color_obj_parameter['n'],
            Vilib.color_obj_parameter['x'],
            Vilib.color_obj_parameter['y'],
            # Vilib.color_obj_parameter['w'],
            # Vilib.color_obj_parameter['h'],
        ]
        sensor_entities.color_detection.values = color_detect_result
    # Face detection data
    if command_entities.face_detection_switch.value == 1:
        face_detect_result = [
            Vilib.face_obj_parameter['n'],
            Vilib.face_obj_parameter['x'],
            Vilib.face_obj_parameter['y'],
            # Vilib.face_obj_parameter['w'],
            # Vilib.face_obj_parameter['h'],
        ]
        sensor_entities.face_detection.values = face_detect_result
    # Traffic sign detection data
    if command_entities.traffic_sign_detection_switch.value == 1:
        _traffic_sign = Vilib.traffic_sign_obj_parameter['t']
        traffic_sign_detect_result = [traffic_sign_label[_traffic_sign]]
        sensor_entities.traffic_sign_detection.values = traffic_sign_detect_result
    # QR code detection data
    if command_entities.qr_code_detection_switch.value == 1:
        qr_cod_tests = [x['text'] for x in Vilib.detect_obj_parameter['qr_list']]
        if len(qr_cod_tests) > 0:
            ws.send(qr_cod_tests)

    # Sound status
    if music.get_sound_busy():
        sensor_entities.sound_effect_status.value = 1
    else:
        sensor_entities.sound_effect_status.value = 0

    # Music status
    if music.get_music_busy():
        # sensor_entities.music_position.values = [music.get_music_length(), music.get_music_pos()]
        sensor_entities.music_position.values = [0, music.get_music_pos()]

def main():
    global openai, status, error

    ips = get_ips()
    print(ips)
    ip = '0.0.0.0'
    if 'wlan0' in ips:
        ip = ips['wlan0']
    elif 'eth0' in ips:
        ip = ips['eth0']

    DEVICE_INFO["Name"] = px.config_file.get("name", default_value=DEVICE_INFO["Name"])
    DEVICE_INFO["video"] = f"{ip}:9000/mjpg"
    print(json.dumps(DEVICE_INFO, indent=4))
    px.reset()

    # --- Init Vilib ---
    try:
        Vilib.camera_start(vflip=False, hflip=False, size=CAMERA_SIZE)
        Vilib.show_fps()
        Vilib.display(local=False,web=True)
    except Exception as e:
        vilib_obj_error.add(str(e))
        print(e)

    # --- Init Websocket ---
    ws.device_info = DEVICE_INFO
    ws.command_entities = command_entities
    ws.sensor_entities = sensor_entities
    ws.on_device_config = on_device_config
    ws.on_io_data = on_io_data
    ws.start()
    # pause()

    usage_st = time.time()

    sensor_entities.motors_offset.values = list.copy(px.cali_dir_value)
    servo_offset = [round(px.cam_pan_cali_val * 10), round(px.cam_tilt_cali_val * 10), round(px.dir_cali_val * 10)]
    sensor_entities.servos_offset.values = servo_offset

    while True:
        with sensor_entities.data_lock:
            # print(f"[INFO] update data")
            update_data()

        time.sleep(0.02)


if __name__ == "__main__":
    try:
        main()
    # except KeyboardInterrupt:
    #     print("KeyboardInterrupt")
    # except Exception as e:
    #     print(e)
    finally:
        print("Exiting")
        # ws.close()
        px.stop()