# https://github.com/mammoth-education/mammoth-coding-docs/blob/main/Picar-X实体定义.md

'''
### 命令实体

ID | 名称 | 数据长度</br>（字节）| 数据类型 | 说明
:-:|:-:|:-:|:-:|:-
`0x01` | 电机控制 | 2 | `int8`, `int8` | 速度, 范围 -100~100</br>`[0]`左轮速度</br>`[1]`右轮速度
`0x02` | 转向舵机 | 1 | `int8` | 角度, 范围 -90~90
`0x03` | 摄像头舵机x轴 | 1 | `int8` | 角度, 范围 -90~90
`0x04` | 摄像头舵机y轴 | 1 | `int8` | 角度, 范围 -90~90
`0x05` | 摄像头开关 | 1 | `uint8` | `0`关闭</br>`1`打开
`0x06` | 摄像头颜色识别开关 | 1 | `uint8` | `0`关闭</br>`1`red</br>`2`orange</br>`3`yellow</br>`4`green</br>`5`blue</br>`6`purple
`0x07` | 摄像头人脸识别开关 | 1 | `uint8` | `0`关闭</br>`1`打开
`0x08` | 摄像头交通标志识别开关 | 1 | `uint8` | `0`关闭</br>`1`打开
`0x09` | 摄像头二维码识别开关 | 1 | `uint8` | `0`关闭</br>`1`打开
`0x0A` | 前台播放音效 | 1 | `uint8` | 音效序号
`0x0B` | 前台音效音量 | 1 | `uint8` | 音量大小, 范围`0~100`
`0x0C` | 后台播放音效 | 1 | `uint8` | 音效序号
`0x0D` | 后台音效音量 | 1 | `uint8` | 音量大小, 范围`0~100`
`0x0E` | 后台音效播放控制 | 1 | `uint8` | `0`播放</br>`1`暂停</br>`2`停止
`0x0F` | 循迹模式 | 2 | `uint8`, `uint8` | `[0]`0关闭循迹,1开启循迹</br>`[1]`表示移动功率, 范围`0~100`
`0x10` | 障碍模式 | 3 | `uint8`, `uint8`, `uint8` | `[0]` 0表示关闭障碍模式, 1标识开启障碍模式</br>`[1]` 0表示避障, 1表示跟随</br>`[2]` 表示移动功率，范围`0~100`

'''	
sound_dir = '/home/xo/picar-x/sounds/'
picarx_sounds = [
    f'{sound_dir}car-double-horn.wav',
    f'{sound_dir}car-start-engine.wav',
    f'{sound_dir}car-double-horn.wav'
]

music_dir = '/home/xo/picar-x/musics/'
picarx_musics = [
    f'{music_dir}spry.mp3',
    f'{music_dir}peace.mp3',
    f'{music_dir}slow-trail-Ahjay_Stelino.mp3',
]

color_detection_command = {
    0x0: 'close',
    0x1: 'red',
    0x2: 'orange',
    0x3: 'yellow',
    0x4: 'green',
    0x5: 'blue',
    0x6: 'purple'
}

traffic_sign_label = {
    'none': 0x00,
    'stop': 0x01,
    'right': 0x02,
    'left': 0x03,
    'forward': 0x04,
}

MUSIC_PLAY_FLAG = 0x00
MUSIC_PAUSE_FLAG = 0x01
MUSIC_STOP_FLAG = 0x02


picarx_command_entities= {
    'id': {
        0x01: 'motor',
        0x02: 'steering',
        0x03: 'camera_pan',
        0x04: 'camera_tilt',
        0x05: 'camera_switch',
        0x06: 'color_detection_switch',
        0x07: 'face_detection_switch',
        0x08: 'traffic_sign_detection_switch',
        0x09: 'qr_code_detection_switch',
        0x0A: 'front_sound_effect',
        0x0B: 'front_sound_volume',
        0x0C: 'background_music',
        0x0D: 'background_music_volume',
        0x0E: 'background_music_control',
        0x0F: 'track_mode',
        0x10: 'obstacle_mode',
        0x11: 'servos_calibration',
        0x12: 'motors_calibration',
        0x13: 'grayscale_calibration',
    },
    'motor': {
        'id': 0x01,
        'len': 2,
        'type': ['int8', 'int8'],
        'value': [0, 0],
        'last_value': [0, 0],
    },
    'steering': {
        'id': 0x02,
        'len': 1,
        'type': ['int8'],
        'value': [0],
        'last_value': [0],
    },
    'camera_pan': {
        'id': 0x03,
        'len': 1,
        'type': ['int8'],
        'value': [0],
        'last_value': [0],
    },
    'camera_tilt': {
        'id': 0x04,
        'len': 1,
        'type': ['int8'],
        'value': [0],
        'last_value': [0],
    },
    'camera_switch': {
        'id': 0x05,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'color_detection_switch': {
        'id': 0x06,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'face_detection_switch': {
        'id': 0x07,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'traffic_sign_detection_switch': {
        'id': 0x08,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'qr_code_detection_switch': {
        'id': 0x09,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'front_sound_effect': {
        'id': 0x0A,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'front_sound_volume': {
        'id': 0x0B,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'background_music': {
        'id': 0x0C,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'background_music_volume': {
        'id': 0x0D,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'background_music_control': {
        'id': 0x0E,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    },
    'track_mode': {
        'id': 0x0F,
        'len': 2,
        'type': ['uint8', 'uint8'],
        'value': [0, 0],
        'last_value': [0, 0],
    },
    'obstacle_mode': {
        'id': 0x10,
        'len': 2,
        'type': ['uint8', 'uint8'],
        'value': [0, 0],
        'last_value': [0, 0],
    },
    'servos_calibration':{
        'id': 0x11,
        'len': 2,
        'type': ['uint8', 'int8'],
        'value': [0, 0],
        'last_value': [0, 0],
    },
    'motors_calibration':{
        'id': 0x12,
        'len': 2,
        'type': ['int8', 'int8'],
        'value': [0, 0],
        'last_value': [0, 0],
    },
    'grayscale_calibration':{
        'id': 0x13,
        'len': 1,
        'type': ['uint8'],
        'value': [0],
        'last_value': [0],
    }
}

'''
### 传感器实体

ID | 名称 | 数据长度</br>（字节）| 数据类型 | 说明
:-:|:-:|:-:|:-:|:-
`0x81` | 超声波距离 | 2 | `int16` | 超声波距离, 单位cm。</br>-1表示超声波超时</br>-2表示无超声波传感器
`0x82` | 3路灰度模块 | 6 | `uint16`, `uint16`, `uint16` | 灰度值</br>`[0]`左</br>`[1]`中</br>`[2]`右 
`0x83` | 电池电压 | 1 | `uint8` | 电池电压, 单位0.1V。
`0x84` | 摄像头颜色识别数据 | 5 | `uint8_t`, `uint16`, `uint16` | `[0]`检测到的色块数量</br> `[1]`最大色块中心x坐标</br> `[2]`最大色块中心y坐标
`0x85` | 摄像头人脸识别数据 | 5 | `uint8_t`, `uint16`, `uint16` | `[0]`检测到的人脸数量</br>`[1]`最大人脸中心x坐标</br>`[2]`最大人脸中心y坐标
`0x86` | 摄像头交通标志识别数据 | 1 | `uint8_t` | 最大交通标志的序号
# `0x87` | 摄像头二维码识别数据 | - | `str` | 二维码内容
`0x88` | 前台音效状态| 1 | `uint8_t` | `0`播放中</br>`1`暂停</br>`2`停止
`0x89` | 背景音效状态| 1 | `uint8_t` | `0`播放中</br>`1`暂停</br>`2`停止
`0x8A` | 3路灰度模块状态 | 3 | `uint8`, `uint8`, `uint8` | 状态值可能为0, 在线外， 1，表示在线内， 2，表示悬空 </br>`[0]`左</br>`[1]`中</br>`[2]`右

'''

picarx_sensor_entities= {
    'ultrasonic': {
        'id': 0x81,
        'type': ['int16'],
        'value': [0],
    },
    'grayscale': {
        'id': 0x82,
        'type': ['uint16', 'uint16', 'uint16'],
        'value': [0, 0, 0],
    },
    'battery_voltage': {
        'id': 0x83,
        'type': ['uint8'],
        'value': [0],
    },
    'color_detection': {
        'id': 0x84,
        'type': ['uint8', 'uint16', 'uint16'],
        'value': [0, 0, 0],
    },
    'face_detection': {
        'id': 0x85,
        'type': ['uint8', 'uint16', 'uint16'],
        'value': [0, 0, 0],
    },
    'traffic_sign_detection': {
        'id': 0x86,
        'type': ['uint8'],
        'value': [0],
    },
    'sound_effect_status': {
        'id': 0x88,
        'type': ['uint8'],
        'value': [0],
    },
    'background_music_status': {
        'id': 0x89,
        'type': ['uint8'],
        'value': [0],
    },
    'grayscale_status': {
        'id': 0x8A,
        'type': ['uint8', 'uint8', 'uint8'],
        'value': [0, 0, 0],
    },
    'servos_offset': {
        'id': 0x8B,
        'type': ['int16', 'int16', 'int16'],
        'value': [0, 0, 0],
    },
    'motors_offset': {
        'id': 0x8C,
        'type': ['int8', 'int8'],
        'value': [0, 0],
    },
    'grayscale_calibration_status': {
        'id': 0x8D,
        'type': ['uint8'],
        'value': [0],
    },
    'background_music_pos': {
        'id': 0x8E,
        'type': ['uint16', 'uint16'],
        'value': [0, 0],
    },
    
}