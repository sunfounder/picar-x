from mammoth_websocket.mammoth_websocket import MammothWebSocket
from mammoth_websocket.utils import get_ips

from picarx.picarx import PiCarX
from picarx.get_hat import is_fusion_hat
from picarx.tts import Piper, OpenAI_TTS
from picarx.stt import Vosk
from picarx.llm import Deepseek, Grok, Doubao, Gemini, Qwen, OpenAI
from picarx.user_button import UserButton

from picarx.music import SoundFiles, music_list, sound_list
from picarx.utils import *
from picarx.auto_drive import LineTracking, ObstacleAvoidance, Following

from utils import Task, Status
import signal

import json
from vilib import Vilib
import cv2

import time
import logging
import threading

import os

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
piper = Piper()
user_button = UserButton()

openai_tts = OpenAI_TTS(gain=3, model="tts-1", voice="alloy")
vosk = Vosk()

deepseek = Deepseek()
grok = Grok()
doubao = Doubao()
gemini = Gemini()
qwen = Qwen()
openai = OpenAI()
llm = None

log = logging.getLogger("PiCar-X")
data_interval = 5 # miliseconds

line_tracking = LineTracking(car, log=log)
obstacle_avoidance = ObstacleAvoidance(car, log=log)
following = Following(car, log=log)

#----
alert_message = None
ai_api_key = None
ai_status = Status.NOT_INITIALIZED
ai_think_result = ""
ai_think_running = False
ai_think_task = None
ai_say_task = None
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
connected = False
connected_changed = False
check_wifi_time = 0
vosk_listen_result = ""
vosk_language = ""
vosk_set_language_task = None
vosk_listen_task = None

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

# update_data_timer = Timer()

class VoskSetLanguageTask(Task):
    def download_callback(self, current, total):
        percent = current / total * 100
        log.debug(f"Downloading STT model: {current} / {total} ({percent:.2f}%)")
        alert("info", f"Downloading STT model: {percent:.2f}%")

    def main(self, language):
        global vosk_language
        try:
            if not vosk.is_model_downloaded(language):
                log.warning(f"Model {language} not downloaded, download it")
                vosk.download_model(language, progress_callback=self.download_callback)
                log.info(f"Model {language} downloaded")

            vosk.set_language(language)
            log.debug(f"Set Vosk language: {language}")
            vosk_language = language
            time.sleep(1)
        except Exception as e:
            log.error(f"Set Vosk language failed: {e}")

class VoskListenTask(Task):
    def main(self):
        global vosk_listen_result
        if not vosk.language():
            log.error("Vosk language not set")
            alert("error", "Set Vosk language first")
            return
        
        log.debug(f"Vosk start listening...")
        vosk_listen_result = ""
        for result in vosk.listen(stream=True):
            if not self.running:
                log.debug(f"Vosk listen terminated")
                break
            if result["done"]:
                log.debug(f"Vosk final result: {result['final']}")
                vosk_listen_result = result['final']
                break
            else:
                log.debug(f"Vosk partial result: {result['partial']}")
                vosk_listen_result = result['partial']

class AiThinkTask(Task):
    def main(self, value, with_image=False):
        global ai_status, ai_think_result, ai_think_running
        if llm is None:
            log.error("AI not initialized")
            ai_status = Status.FAILED
            alert("error", "AI not initialized")
            return
        
        content = value.strip()
        if len(content) == 0:
            log.error(f"Invalid think content: {content}")
            return

        ai_status = Status.THINKING
        ai_think_result = ""
        ai_think_running = True
        log.debug(f"Think with: {content}, with image: {with_image}")
        img_path = None
        try:
            if with_image:
                img_path = '/tmp/picar-x-app-think-img.jpg'
                # Save image
                cv2.imwrite(img_path, Vilib.img)
            response = llm.prompt(content, image_path=img_path, stream=True)
        except Exception as e:
            log.error(f"AI failed: {e}")
            alert("error", f"AI failed: {e}")
            ai_status = Status.FAILED
            return
        ai_think_result = ""
        for chunk in response:
            if chunk != None and len(chunk) > 0:
                ai_think_result = f"{ai_think_result}{chunk}"
            log.debug(f"Think result: {chunk}")
        ai_status = Status.IDLE
        ai_think_running = False

class AiSayTask(Task):
    def main(self, value):
        global ai_status
        if not openai_tts.is_ready:
            log.error("Open AI TTS not ready")
            ai_status = Status.FAILED
            alert("error", "Open AI TTS not ready")
            return

        content = value.strip()
        if len(content) == 0:
            log.error(f"Invalid speak content: {content}")
            return

        ai_status = Status.TTS
        log.debug(f"speak: [{content}]")
        openai_tts.say(content)
        ai_status = Status.IDLE

def piper_say_task(value):
    data_to_send["piper_saying"] = True
    start = time.time()
    if not piper.is_model_downloaded():
        log.info(f"Downloading piper model:{piper.model}")
        piper.download_model()
    piper.say(value)
    duration = round(time.time() - start, 3)
    log.debug(f"piper_say done in {duration} s")
    data_to_send["piper_saying"] = False

def alert(type, msg):
    global alert_message
    if type == 'error':
        type = 'warn'
    alert_message = [type, msg]

# --- handler functions ---
def handle_name_changed(name):
    DEVICE_INFO["Name"] = name
    log.debug(f"Name changed to {name}")
    car.set_name(name)

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

def handle_ai_api_key(api_key):
    global ai_status
    DEVICE_INFO["ai_api_key"] = api_key
    car.config.set("ai_api_key", api_key)
    openai_tts.set_api_key(api_key)
    llm.set_api_key(api_key)
    log.debug(f"Set api-key: {api_key}")
    ai_status = Status.IDLE

def handle_ai_init(provider, model):
    global llm, ai_status
    if provider == "deepseek":
        llm = deepseek
    elif provider == "grok":
        llm = grok
    elif provider == "doubao":
        llm = doubao
    elif provider == "gemini":
        llm = gemini
    elif provider == "qwen":
        llm = qwen
    elif provider == "openai":
        llm = openai
    llm.set_model(model)
    llm.set_api_key(ai_api_key)
    log.debug(f"Set AI model: {model}")
    ai_status = Status.IDLE

def handle_ai_say_voice(voice):
    openai_tts.set_voice(voice)
    log.debug(f"Set speak voice: {voice}")

def handle_ai_think(value, with_image=False):
    global ai_status
    if len(value) == 0:
        log.error(f"Invalid think content: {value}")
        return
    if value == "[STOP]":
        ai_think_task.stop()
        ai_status = Status.IDLE
        log.debug(f"Stop think")
        return
    if ai_status == Status.IDLE:
        ai_think_task.start(value, with_image)

def handle_ai_think_with_image(value):
    handle_ai_think(value, with_image=True)

def handle_ai_say(value):
    global ai_status
    log.debug(f"handle_ai_say: {value}")

    if len(value) == 0:
        log.error(f"Invalid speak content: {value}")
        return

    if value == "[STOP]":
        ai_say_task.stop()
        ai_status = Status.IDLE
        log.debug(f"Stop say")
        return

    if ai_status == Status.IDLE:
        ai_say_task.start(value)

def handle_do_action(action):
    log.debug(f"handle_do_action: {action}")
    if action == "[STOP]":
        log.debug(f"Stop action")
        return
    if action not in car.actions:
        log.error(f"Invalid action: {action}")
        return
    
    data_to_send['action_status'] = True
    car.actions[action]()
    data_to_send['action_status'] = False

def handle_led(status: bool):
    log.debug(f"Set led: {status}")
    car.set_led(status)

def handle_piper_set_model(model):
    log.debug(f"Set piper model: {model}")
    piper.set_model(model)
    data_to_send['piper_model'] = model

def handle_piper_say(value):
    log.debug(f"handle_piper_say: {value}")
    task = threading.Thread(target=piper_say_task, args=(value,))
    task.start()

def handle_vosk_set_language(language):
    if language == "[STOP]":
        log.debug(f"Vosk stop set language")
        vosk.cancel_download()
        vosk_set_language_task.stop()
        return
    vosk_set_language_task.start(language)

def handle_vosk_listen(enable):
    if enable == 0:
        log.debug(f"Vosk stop listen")
        vosk_listen_task.stop()
        return
    vosk_listen_task.start()

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
    "ai_init": handle_ai_init,
    "ai_say_voice": handle_ai_say_voice,
    "ai_think": handle_ai_think,
    "ai_think_with_image": handle_ai_think_with_image,
    "ai_say": handle_ai_say,
    # Piper
    "piper_set_model": handle_piper_set_model,
    "piper_say": handle_piper_say,
    # Vosk
    "vosk_set_language": handle_vosk_set_language,
    "vosk_listen": handle_vosk_listen,
    # Others
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

    # if 'ai_say' in rec.keys():
    #     print(f"AI say:  {rec['ai_say']}")

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
    # if "vosk_language_setting" in data_to_send.keys():
    #     print(f"Vosk language setting: {data_to_send['vosk_language_setting']}")

    try:
        data = json.dumps(data)
    except:
        log.error(f"Failed to dump data: {data}")
        return
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

async def handle_disconnected(ip):
    global connected, connected_changed
    connected = False
    connected_changed = True
    log.debug(f"Client {ip} disconnected")

    # Reset robot
    # car.stop()
    # car.set_steering_angle(0)
    # car.set_camera_pan_angle(0)
    # car.set_camera_tilt_angle(0)

def handle_restart_service():
    delay = 3
    log.info(f"Restart service in {delay}s")
    blink_delay = 0.1
    for_count = int(delay / blink_delay / 2)
    for _ in range(for_count):
        car.set_led(1)
        time.sleep(blink_delay)
        car.set_led(0)
        time.sleep(blink_delay)
    log.info("Restart service")
    os.system("systemctl restart picar-x-app.service")

# @update_data_timer.print
def update_data():
    global ai_think_result, alert_message

    # Read sensor data
    data_to_send["ultrasonic_distance"] = car.get_distance()
    data_to_send["battery_voltage"] = car.get_battery_voltage()
    if is_fusion_hat:
        data_to_send["charge_state"] = car.get_charge_state()
    data_to_send["user_button_pressed"] = user_button.is_pressed()

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
    data_to_send["ai_status"] = ai_status
    if alert_message is not None:
        data_to_send["alert"] = alert_message
        alert_message = None
    if ai_think_result != "":
        data_to_send["ai_think_result"] = ai_think_result
    
    # Vosk status
    data_to_send["vosk_listening"] = vosk_listen_task.running
    data_to_send["vosk_language_setting"] = vosk_set_language_task.running
    data_to_send["vosk_language"] = vosk_language
    data_to_send["vosk_listen_result"] = vosk_listen_result

def clear_once_data_to_send():
    if 'ai_listen_result' in data_to_send:
        del data_to_send['ai_listen_result']
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
    if 'alert' in data_to_send:
        del data_to_send['alert']

def init_log():
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('[%(levelname)s] %(message)s')
    console_handler.setFormatter(console_formatter)
    log.addHandler(console_handler)

def init():
    global ai_status, ai_api_key
    global vosk_listen_task, vosk_set_language_task, ai_think_task, ai_say_task
    init_log()

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

    # --- Init AI ---
    # if ai_api_key:
    #     try:
    #         openai_tts.set_api_key(ai_api_key)
    #         ai_status = Status.IDLE
    #     except Exception as e:
    #         log.exception(str(e))

    vosk_set_language_task = VoskSetLanguageTask()
    vosk_listen_task = VoskListenTask()
    ai_think_task = AiThinkTask()
    ai_say_task = AiSayTask()

    # --- Init User Button ---
    user_button.set_on_long_press(handle_restart_service, duration=3)
    user_button.start()

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

def is_wifi_connected():
    global check_wifi_time
    # Get wifi interface ip with command
    if time.time() - check_wifi_time < CHECK_WIFI_EVERY:
        return True
    check_wifi_time = time.time()
    ips = get_ips()
    if 'wlan0' not in ips:
        return False

    return True

def main():
    global connected_changed

    init()

    start = time.time()
    car.music.play_sound(SoundFiles.START_ENGINE)

    led_status = False
    start_led_time = time.time()
    while True:
        if not is_wifi_connected():
            log.error("No wifi connection, try restart wifi")
            os.system("sudo nmcli device down wlan0")
            car.set_led(1)
            time.sleep(0.5)
            car.set_led(0)
            time.sleep(0.5)
            car.set_led(1)
            time.sleep(0.5)
            car.set_led(0)
            os.system("sudo nmcli device up wlan0")
            continue
        if connected_changed:
            connected_changed = False
            if connected:
                car.set_led(0)
        if not connected:
            if time.time() - start_led_time > 1:
                led_status = not led_status
                car.set_led(led_status)
                start_led_time = time.time()
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
    user_button.stop()
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
