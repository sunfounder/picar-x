
from enum import StrEnum

CAMERA_SIZE = (800, 600)


SOUND_DIR = '../sounds/'
picarx_sounds = [
    f'{SOUND_DIR}car-double-horn.wav',
    f'{SOUND_DIR}car-start-engine.wav',
    f'{SOUND_DIR}car-double-horn.wav'
]

music_dir = '../musics/'
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

class AIStatus(StrEnum):
    """AI状态枚举（字符串类型）"""
    NOT_INITIALIZED = "NOT_INITIALIZED"
    INITIALIZING = "INITIALIZING"
    IDLE = "IDLE"
    LISTENING = "LISTENING" 
    STT = "STT"
    TTS = "TTS"
    THINKING = "THINKING"
    SPEAKING = "SPEAKING"