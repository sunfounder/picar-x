

from mammoth_websocket.entities import Entities

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
`0x0E` | 后台音效播放控制 | 1 | `uint8` | `0`停止</br>`1`播放</br>`2`暂停
`0x0F` | 循迹模式 | 2 | `uint8`, `uint8` | `[0]`0关闭循迹,1开启循迹</br>`[1]`表示移动功率, 范围`0~100`
`0x10` | 障碍模式 | 2 | `uint8`, `uint8`| `[0]` 0表示关闭障碍模式, 1标识开启障碍模式</br>`[1]` 表示移动功率，范围`0~100`
`0x11` | 舵机校准 | 2 | `uint8`, `int8` | `[0]` 舵机：`0`表示摄像头舵机x轴，`1`表示摄像头舵机y轴，`2`表示转向舵机</br>`[1]` 操作，`0` 表示不操作，`1`表示增加， `-1` 表示减少， `2` 表示保存
`0x12` | 电机方向校准 | 2 | `int8`, `int8` | 设置电机校准值, 1或者-1</br> `[0]`左轮，</br>`[1]`右轮`
`0x13` | 三路灰度模块校准 | 1 | `uint8` | `0`不操作，`1`开始校准
`0x14` | OpenAI 设置 API Key | 1+ | `uint8`, `str` | 第一位表示后面字符串长度，后面是API Key字符串。
`0x15` | OpenAI 设置 Assistant ID | 1+ | `uint8`, `str` | 第一位表示后面字符串长度，后面是Assistant ID字符串。
`0x16` | 听 | 1 | `uint8` | 使用麦克风录音，并返回听到的内容（看传感器实体的听到的内容）</br>`0`关闭</br>`1`打开
`0x17` | 思考 | 2+ | `uint16`, `str` | 前两位是Uint16类型的字符串长度，后面是字符串内容。使用OpenAI的API，根据输入的内容，通过思考的结果传感器实体返回思考结果。
`0x18` | 说 | 2+ | `uint16`, `str` | 前两位是Uint16类型的字符串长度，后面是字符串内容。使用OpenAI的API，根据输入的内容，通过喇叭播放内容。
`0x19` | 包含画面思考 | 2+ | `uint16`, `str` | 前两位是Uint16类型的字符串长度，后面是字符串内容。使用OpenAI的API，根据输入的内容，通过思考的结果传感器实体返回思考结果。

'''	
command_entities = Entities()
command_entities.add('motor', 0x01, ['int8', 'int8'])
command_entities.add('steering', 0x02, ['int8'])
command_entities.add('camera_pan', 0x03, ['int8'])
command_entities.add('camera_tilt', 0x04, ['int8'])
command_entities.add('camera_switch', 0x05, ['uint8'])
command_entities.add('color_detection_switch', 0x06, ['uint8'])
command_entities.add('face_detection_switch', 0x07, ['uint8'])
command_entities.add('traffic_sign_detection_switch', 0x08, ['uint8'])
command_entities.add('qr_code_detection_switch', 0x09, ['uint8'])
command_entities.add('sound_effect', 0x0A, ['uint8'])
command_entities.add('sound_volume', 0x0B, ['uint8'])
command_entities.add('music', 0x0C, ['uint8'])
command_entities.add('music_volume', 0x0D, ['uint8'])
command_entities.add('music_control', 0x0E, ['uint8'])
command_entities.add('track_mode', 0x0F, ['uint8', 'uint8'])
command_entities.add('obstacle_mode', 0x10, ['uint8', 'uint8'])
command_entities.add('servos_calibration', 0x11, ['uint8', 'int8'])
command_entities.add('motors_calibration', 0x12, ['int8', 'int8'])
command_entities.add('grayscale_calibration', 0x13, ['uint8'])
command_entities.add('set_api_key', 0x14, ['uint8', 'str'])
command_entities.add('set_assistant_id', 0x15, ['uint8', 'str'])
command_entities.add('listen', 0x16, ['uint8'])
command_entities.add('think', 0x17, ['uint16', 'str'])
command_entities.add('say', 0x18, ['uint16', 'str'])
command_entities.add('think_with_image', 0x19, ['uint16','str'])


'''
### 传感器实体

ID | 名称 | 数据长度</br>（字节）| 数据类型 | 说明
:-:|:-:|:-:|:-:|:-
`0x81` | 超声波距离 | 2 | `int16` | 超声波距离, 单位cm。</br>-1表示超声波超时</br>-2表示无超声波传感器
`0x82` | 3路灰度模块原始值 | 6 | `uint16`, `uint16`, `uint16` | 灰度值</br>`[0]`左</br>`[1]`中</br>`[2]`右
`0x83` | 电池电压 | 1 | `uint8` | 电池电压, 单位0.1V。
`0x84` | 摄像头颜色识别数据 | 5 | `uint8_t`, `uint16`, `uint16` | `[0]`检测到的色块数量</br> `[1]`最大色块中心x坐标</br> `[2]`最大色块中心y坐标
`0x85` | 摄像头人脸识别数据 | 5 | `uint8_t`, `uint16`, `uint16` | `[0]`检测到的人脸数量</br>`[1]`最大人脸中心x坐标</br>`[2]`最大人脸中心y坐标
`0x86` | 摄像头交通标志识别数据 | 1 | `uint8_t` | 最大交通标志的序号
`0x87` | 摄像头二维码识别数据 | - | `str` | 二维码内容
`0x88` | 前台音效状态| 1 | `uint8_t` | `0`停止</br>`1`播放</br>`2`暂停
`0x89` | 背景音效状态| 1 | `uint8_t` | `0`停止</br>`1`播放</br>`2`暂停
`0x8A` | 3路灰度模块状态 | 3 | `uint8`, `uint8`, `uint8` | 状态值可能为0, 在线外， 1，表示在线内， 2，表示悬空 </br>`[0]`左</br>`[1]`中</br>`[2]`右
`0x8B` | 舵机角度校准值| 6 | `int16`, `int16`, `int16` | 舵机校准值，单位0.1度，范围-20.0~20.0</br>，`[0]`摄像头舵机x轴</br>`[1]`摄像头舵机y轴</br>`[2]`转向舵机
`0x8C` | 电机方向校准值| 2 | `int8`, `int8` | 电机方向校准值, `1`或者`-1`,</br>`[0]`左轮</br>`[1]`右轮
`0x8D` | 三路灰度模块校准值| 1 | `uint8`| 状态, `0`无操作, `1` 校准中，`2` 校准完成，`3` 校准失败
`0x8E` | 背景音乐时长 | 4 | `uint16`，`uint16` | [0]音乐总时长,单位秒</br> [1]当前播放时长 ,单位秒
`0x8F` | 听到的内容 | 2+ | `uint16`, `str` | 麦克风录音，并返回听到的内容，第一位是长度，后面是utf8编码的字符串
`0x90` | 思考的结果 | 2+ | `uint16`, `str` | 前两位是Uint16类型的字符串长度，后面是字符串内容。使用OpenAI的API，根据输入的内容，通过思考传感器实体返回思考结果。
`0x91` | AI是否已初始化 | 1 | `uint8` | `0`未初始化</br>`1`已初始化

'''

sensor_entities = Entities()
sensor_entities.add('ultrasonic', 0x81, ['int16'])
sensor_entities.add('grayscale', 0x82, ['uint16', 'uint16', 'uint16'])
sensor_entities.add('battery_voltage', 0x83, ['uint8'])
sensor_entities.add('color_detection', 0x84, ['uint8', 'uint16', 'uint16'])
sensor_entities.add('face_detection', 0x85, ['uint8', 'uint16', 'uint16'])
sensor_entities.add('traffic_sign_detection', 0x86, ['uint8'])
sensor_entities.add('qr_code_detection', 0x87, ['str'])
sensor_entities.add('sound_effect_status', 0x88, ['uint8'])
sensor_entities.add('music_status', 0x89, ['uint8'])
sensor_entities.add('grayscale_status', 0x8A, ['uint8', 'uint8', 'uint8'])
sensor_entities.add('servos_offset', 0x8B, ['int16', 'int16', 'int16'])
sensor_entities.add('motors_offset', 0x8C, ['int8', 'int8'])
sensor_entities.add('grayscale_calibration_status', 0x8D, ['uint8'])
sensor_entities.add('music_position', 0x8E, ['uint16', 'uint16'])
sensor_entities.add('listen_result', 0x8F, ['uint16', 'str'])
sensor_entities.add('think_result', 0x90, ['uint16','str'])
sensor_entities.add('ai_initialized', 0x91, ['uint8'])
