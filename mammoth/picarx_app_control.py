from mammoth_websocket import MammothWebSocket
from mammoth_websocket.utils import get_ips
from picarx_entity import picarx_command_entities as commands
from picarx_entity import picarx_sensor_entities as sensors
from picarx_entity import color_detection_command, picarx_sounds, picarx_musics, traffic_sign_label
from picarx_functions import *
from picarx import Picarx

from robot_hat.utils import get_battery_voltage
import json
from vilib import Vilib

import time
import threading

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

ips = get_ips()
print(ips)
ip = '0.0.0.0'
if 'wlan0' in ips:
    ip = ips['wlan0']
elif 'eth0' in ips:
    ip = ips['eth0']

DEVICE_INFO = {
    "Name": "Picar-X-001", ## TODO: get the name from the device
    "Type": "Picar-X",
    "Check": "MC",
    "video": f"{ip}:9000/mjpg",
    "Version": VERSION,
}

sensor_data_lock = threading.Lock()

color_detect_result = list.copy(sensors['color_detection']['value'])
face_detect_result = list.copy(sensors['face_detection']['value'])
traffic_sign_detect_result = list.copy(sensors['traffic_sign_detection']['value'])

# Mammoth WebSocket server
# =================================================================
ws = MammothWebSocket()
ws.device_info = DEVICE_INFO

#----
status = ''
error = []
data = {}

## initialize the picarx
# =================================================================
picarx_obj_status = ''
picarx_obj_error = []
try:
    px = Picarx()
    px.reset()
    picarx_object_status = 'OK'
except Exception as e:
    picarx_obj_error.append(str(e))
    print(e)

sensors['motors_offset']['value'] = list.copy(px.cali_dir_value)

music = Music()

# initialize the camera 
# =================================================================
vilib_obj_status = ''
vilib_obj_error = []
# CAMERA_SIZE = (800, 600)
CAMERA_SIZE = (800, 600)

'''
SGBRG10_CSI2P,640x480/0 - Score: 3296
SGBRG10_CSI2P,1296x972/0 - Score: 1000
SGBRG10_CSI2P,1920x1080/0 - Score: 1349.67
SGBRG10_CSI2P,2592x1944/0 - Score: 1567
'''

try:
    Vilib.camera_start(vflip=False, hflip=False, size=CAMERA_SIZE)
    Vilib.show_fps()
    Vilib.display(local=False,web=True)
    vilib_obj_status = 'OK'
except Exception as e:
    vilib_obj_error.add(str(e))
    print(e)

# main
# =================================================================
def commands__handler(_command_entities):
    # control
    # ------------------------------------
    # --- motors ---
    if 'motor' in _command_entities.keys():
        if _command_entities['motor']['value'] != commands['motor']['last_value']:
            _motor = _command_entities['motor']['value']
            commands['motor']['last_value'] = _motor
            px.set_motor_speed(1, _motor[0])
            px.set_motor_speed(2, _motor[1])
    # --- steering servo ---
    if 'steering' in _command_entities.keys():
        if _command_entities['steering']['value'] != commands['steering']['last_value']:
            _steering = _command_entities['steering']['value']
            commands['steering']['last_value'] = _steering
            px.set_dir_servo_angle(_steering[0])
    # --- camera pan servo ---
    if 'camera_pan' in _command_entities.keys():
        if _command_entities['camera_pan']['value'] != commands['camera_pan']['last_value']:
            _camera_pan = _command_entities['camera_pan']['value']
            commands['camera_pan']['last_value'] = _camera_pan
            px.set_cam_pan_angle(_camera_pan[0])
    # --- camera tilt servo ---
    if 'camera_tilt' in _command_entities.keys():
        if _command_entities['camera_tilt']['value'] != commands['camera_tilt']['last_value']:
            _camera_tilt = _command_entities['camera_tilt']['value']
            commands['camera_tilt']['last_value'] = _camera_tilt
            px.set_cam_tilt_angle(_camera_tilt[0])
        
    # vision processing
    # ------------------------------------
    # ---
    if 'color_detection_switch' in _command_entities.keys():
        if _command_entities['color_detection_switch']['value'] != commands['color_detection_switch']['last_value']:
            _color_switch = _command_entities['color_detection_switch']['value']
            commands['color_detection_switch']['last_value'] = _color_switch
            _color_switch = color_detection_command[_color_switch[0]]
            Vilib.color_detect(_color_switch)
    # ---
    if 'face_detection_switch' in _command_entities.keys():
        if _command_entities['face_detection_switch']['value'] != commands['face_detection_switch']['last_value']:
            _face_switch = _command_entities['face_detection_switch']['value']
            commands['face_detection_switch']['last_value'] = _face_switch
            Vilib.face_detect_switch(_face_switch[0])
    # ---
    if 'traffic_sign_detection_switch' in _command_entities.keys():
        if _command_entities['traffic_sign_detection_switch']['value'] != commands['traffic_sign_detection_switch']['last_value']:
            _traffic_sign_switch = _command_entities['traffic_sign_detection_switch']['value']
            commands['traffic_sign_detection_switch']['last_value'] = _traffic_sign_switch
            Vilib.traffic_detect_switch(_traffic_sign_switch[0])
    # ---
    if 'qr_code_detection_switch' in _command_entities.keys():
        if _command_entities['qr_code_detection_switch']['value'] != commands['qr_code_detection_switch']['last_value']:
            _qr_code_switch = _command_entities['qr_code_detection_switch']['value']
            commands['qr_code_detection_switch']['last_value'] = _qr_code_switch
            Vilib.qrcode_detect_switch(_qr_code_switch[0])

    # sound and music
    # ------------------------------------
    # --- sound effect ---
    if 'front_sound_effect' in _command_entities.keys():
        if _command_entities['front_sound_effect']['value'][0] != 0 and not music.get_sound_busy():
            _sound_effect_index = _command_entities['front_sound_effect']['value'][0]
            music.play_sound_effect(picarx_sounds[_sound_effect_index-1])

    # --- music ---
    if 'background_music' in _command_entities.keys() or 'background_music_control' in _command_entities.keys() or 'background_music_volume' in _command_entities.keys():
        _music_index = commands['background_music']['value']
        _last_music_index = commands['background_music']['last_value']
        _music_control = commands['background_music_control']['value']
        _last_music_control = commands['background_music_control']['last_value']
        _music_volume = commands['background_music_volume']['value']
        _last_music_volume = commands['background_music_volume']['last_value']

        print(_music_index, _last_music_index, _last_music_control[0])

        if _music_control[0] == 1:
            if (_last_music_control[0] == 0) or _music_index != _last_music_index:
                commands['background_music']['last_value'] = list(_music_index)
                _msic_path = picarx_musics[_music_index[0]-1]
                music.play_music(_msic_path)
                sensors['background_music_pos']['value'][0] = music.get_music_length(_msic_path)

        if _music_volume != _last_music_volume:
            music.set_music_volume(_music_volume[0])
        if _music_control != _last_music_control:
            music.music_control(_music_control[0])
        #
        commands['background_music_control']['last_value'] = list(_music_control)
        commands['background_music_volume']['last_value'] = list(_music_volume)
        #
        if music.get_music_busy():
            sensors['background_music_status']['value'] = list(_music_control)
        else:
            sensors['background_music_status']['value'] = [0]

    if music.get_music_busy():
        sensors['background_music_pos']['value'][1] = music.get_music_pos()


    # track_mode
    # ------------------------------------
    if 'track_mode' in _command_entities.keys():
        if _command_entities['track_mode']['value'] != commands['track_mode']['last_value']:
            _trace_mode = _command_entities['track_mode']['value']
            _track_speed = _command_entities['track_mode']['value'][1]
            commands['track_mode']['last_value'] = _trace_mode
            if _trace_mode[0] == 0:
                px.stop()
        if _command_entities['track_mode']['value'][0] != 0:
            _track_speed = _command_entities['track_mode']['value'][1]
            line_track(_track_speed)


    # obstacle_mode
    # ------------------------------------
    if 'obstacle_mode' in _command_entities.keys():
        if _command_entities['obstacle_mode']['value'] != commands['obstacle_mode']['last_value']:
            _obstacle_mode = _command_entities['obstacle_mode']['value']
            commands['obstacle_mode']['last_value'] = _obstacle_mode
            if _obstacle_mode[0] == 0:
                px.stop()
        if _command_entities['obstacle_mode']['value'][0] != 0:
            _obstacle_speed = _command_entities['obstacle_mode']['value'][1]
            avoid_obstacles(_obstacle_speed)

    # servos_calibration
    # ------------------------------------
    if 'servos_calibration' in _command_entities.keys():
        if _command_entities['servos_calibration']['value'] != commands['servos_calibration']['last_value']:
            _servos_calibration = _command_entities['servos_calibration']['value']
            commands['servos_calibration']['last_value'] = _servos_calibration
            _servo_index =_servos_calibration[0]
            _servo_opt = _servos_calibration[1]
            if _servo_opt == 1:
                sensors['servos_offset']['value'][_servo_index] += 2
                if sensors['servos_offset']['value'][_servo_index] > 200:
                    sensors['servos_offset']['value'][_servo_index] = 200
            elif _servo_opt == -1:
                sensors['servos_offset']['value'][_servo_index] -= 2
                if sensors['servos_offset']['value'][_servo_index] < -200:
                    sensors['servos_offset']['value'][_servo_index] = -200

    # motors calibration
    # ------------------------------------
    if 'motors_calibration' in _command_entities.keys():
        if _command_entities['motors_calibration']['value'] != commands['motors_calibration']['last_value']:
            _motors_offset = list(_command_entities['motors_calibration']['value'])
            commands['motors_calibration']['last_value'] = _motors_offset
            sensors['motors_offset']['value'] = _motors_offset
            px.cali_dir_value = list.copy(_motors_offset)


async def on_connect(**kwargs):
    # if 'client' in kwargs:
    #     client = kwargs['client']
    #     client_id = client['id']
    #     client_ip = client['ip']
    #     ws.send(DEVICE_INFO, client_id)
    # else:
    #     ws.send(DEVICE_INFO)
    pass

async def on_disconnect(**kwargs):
    pass

async def on_receive(data, client_id):
    # client = ws.clients[client_id]

    # string data
    # -----------------------------------------------
    if isinstance(data, str):
        # print(f"Received string ({client_id}): {data}")
        if data.startswith('SET+'):
            try:
                data = data[4:]
                data = json.loads(data)
                await ws.response('OK')
            except Exception as e:
                await ws.response('ERROR', ['Invalid json format', f'{e}'] )
        else:
            await ws.response('ERROR', ['Invalid command format'])

    # binary data
    # -----------------------------------------------
    elif isinstance(data, bytes):
        # print(f"Received bytes ({client_id}): {data}")

        # read command
        _command_entities = ws.bytes_to_entities(commands, data)
        # handle command
        commands__handler(_command_entities)

        # send sensors data
        with sensor_data_lock:
            binary_data = ws.entities_to_bytes(sensors)
        print(f"Send binary data ({client_id}): {binary_data}")
        await ws.asyn_send(binary_data, client_id)


def main():
    global color_detect_result, traffic_sign_detect_result, face_detect_result

    # ws.on_connect = on_connect
    # ws.on_disconnect = on_disconnect  
    ws.on_receive = on_receive
    ws.start()
    # pause()

    usage_st = time.time()

    while True:
        ## read sensor data
        ultrasonic_distance = px.get_distance()
        grayscale_data = px.get_grayscale_data()
        battery_voltage = get_battery_voltage()
        if battery_voltage < 6:
            battery_voltage = 6
        elif battery_voltage > 8.5:
            battery_voltage = 8.5

        grayscale_status = []
        for data in grayscale_data:
            if data > 1000:
                grayscale_status.append(0)
            elif data > 300:
                grayscale_status.append(1)
            else:
                grayscale_status.append(2)

        if commands['color_detection_switch']['value'][0] == 1:
            color_detect_result = [
                Vilib.color_obj_parameter['n'],
                Vilib.color_obj_parameter['x'],
                Vilib.color_obj_parameter['y'],
                # Vilib.color_obj_parameter['w'],
                # Vilib.color_obj_parameter['h'],
            ]
        if commands['face_detection_switch']['value'][0] == 1:
            face_detect_result = [
                Vilib.face_obj_parameter['n'],
                Vilib.face_obj_parameter['x'],
                Vilib.face_obj_parameter['y'],
                # Vilib.face_obj_parameter['w'],
                # Vilib.face_obj_parameter['h'],
            ]
        if commands['traffic_sign_detection_switch']['value'][0] == 1:
            # traffic_sign_detect_result = [
            #     Vilib.traffic_sign_obj_parameter['n'],
            #     Vilib.traffic_sign_obj_parameter['x'],
            #     Vilib.traffic_sign_obj_parameter['y'],
            #     # Vilib.traffic_sign_obj_parameter['w'],
            #     # Vilib.traffic_sign_obj_parameter['h'],
            # ]

            _traffic_sign = Vilib.traffic_sign_obj_parameter['t']
            traffic_sign_detect_result = [traffic_sign_label[_traffic_sign]]
            
        ###
        if commands['qr_code_detection_switch']['value'][0] == 1:
            qr_cod_tests = [x['text'] for x in Vilib.detect_obj_parameter['qr_list']]
            if len(qr_cod_tests) > 0:
                ws.send(qr_cod_tests)


        ###
        if music.get_sound_busy():
            sensors['sound_effect_status']['value'] = [1]
        else:
            sensors['sound_effect_status']['value'] = [0]


        with sensor_data_lock:
            sensors['ultrasonic']['value'] = int(ultrasonic_distance*10)
            sensors['grayscale']['value'] = grayscale_data
            sensors['battery_voltage']['value'] = int((battery_voltage-6)*100)
            sensors['color_detection']['value'] = list.copy(color_detect_result)
            sensors['face_detection']['value'] = list.copy(face_detect_result)
            sensors['traffic_sign_detection']['value'] = list.copy(traffic_sign_detect_result)
            sensors['grayscale_status']['value'] = list.copy(grayscale_status)
        # if time.time() - usage_st > 1:
        #     usage_st = time.time()

        #     num_fds = process.num_fds()
        #     memory_usage = process.memory_info().rss / 1024 / 1024  # MB 
        #     print(term.skyblue(f'num_fds: {num_fds} , memory: {memory_usage:.5f} MB'))
        time.sleep(0.02)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except Exception as e:
        print(e)
    finally:
        print("Exiting")
        # ws.close()
        px.stop()
        # if vilib_obj_status == 'OK':
        #     Vilib.camera_close()