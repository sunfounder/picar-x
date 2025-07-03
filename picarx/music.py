from robot_hat import Music as RobotHatMusic
import threading
from enum import IntEnum, StrEnum
from importlib.resources import files

SOUND_DIR = files('picarx').joinpath('sounds')
MUSIC_DIR = files('picarx').joinpath('musics')

class MusicStatus(IntEnum):
    STOP = 0
    PLAY = 1
    PAUSE = 2

class MusicFiles(StrEnum):
    SPRY = str(MUSIC_DIR.joinpath('spry.mp3'))
    PEACE = str(MUSIC_DIR.joinpath('peace.mp3'))
    SLOW_TRAIL = str(MUSIC_DIR.joinpath('slow-trail-Ahjay_Stelino.mp3'))

class SoundFiles(StrEnum):
    DOUBLE_HORN = str(SOUND_DIR.joinpath('car-double-horn.wav')),
    START_ENGINE = str(SOUND_DIR.joinpath('car-start-engine.wav')),

music_list = [MusicFiles.SPRY, MusicFiles.PEACE, MusicFiles.SLOW_TRAIL]
sound_list = [SoundFiles.DOUBLE_HORN, SoundFiles.START_ENGINE]

# sound effect and music
# =================================================================
class Music:
    def __init__(self):
        self.music = RobotHatMusic()
        self.sound_thread = None
        self.music_path = None
        self.volume = 100
        self.music_status = MusicStatus.STOP

    def play_sound(self, file_path):
        self.music.sound_play(filename=file_path, volume=self.volume)

    def play_sound_background(self, file_path):
        self.sound_thread = threading.Thread(target=self.music.sound_play, kwargs={
            "filename": file_path,
            "volume": self.volume
            }
        )
        self.sound_thread.start()

    def play_music_background(self, file_path):
        self.music_path = file_path
        self.music.music_play(file_path)

    def music_control(self, action):
        if action == MusicStatus.STOP:
            self.music.music_stop()
        elif action == MusicStatus.PLAY:
            if self.music_status == MusicStatus.PAUSE:
                self.music.music_resume()
            else:
                self.music.music_play(self.music_path)
        elif action == MusicStatus.PAUSE:
            self.music.music_pause()
        self.music_status = action

    def set_volume(self, volume):
        if volume > 100:
            volume = 100
        elif volume < 0:
            volume = 0
        self.volume = volume
        self.music.music_set_volume(volume)

    def is_music_busy(self):
        return self.music.pygame.mixer.music.get_busy()
    
    def get_music_length(self, file_path=None):
        if file_path is None:
            file_path = self.music_path
        sound = self.music.pygame.mixer.Sound(file_path)
        return int(sound.get_length())

    def get_music_pos(self):
        return int(self.music.pygame.mixer.music.get_pos() / 1000)
    
    def is_sound_busy(self):
        if self.sound_thread is None:
            return False
        if self.sound_thread.is_alive():
            return True
        else:
            return False

    def get_volume(self):
        return self.volume

    def stop(self):
        self.music.music_stop()