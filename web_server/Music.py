import pygame
import time
import threading


pygame.mixer.init()

class MyThreading(threading.Thread):

    def __init__(self, func, **arg):
        super(MyThreading,self).__init__()
        self.func = func
        self.arg = arg

    def run(self):
        self.func(**self.arg)

def sound_effect_play(file_name,volume = 0.5):
    file_name = '/opt/ezblock/sound/' + file_name
    music = pygame.mixer.Sound(str(file_name))
    music.set_volume(volume)
    time_delay = round(music.get_length(),2)
    music.play()
    time.sleep(time_delay)

def sound_effect_threading(file_name,volume = 0.5):
    # file_name = './sound/' + file_name
    obj = MyThreading(sound_effect_play,file_name = file_name,volume = volume)
    obj.start()


def background_music(file_name,loops=-1, start=0.0,volume = 0.5):#-1:continue
    if loops <= 0:
        loops = 0
    file_name = '/opt/ezblock/music/' + str(file_name)
    pygame.mixer.music.load(str(file_name))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops-1, start)

def record_play(file_name,loops=1, start=0.0,volume = 0.5):
    # pygame.mixer.init(16000)
    file_name = './records/' + str(file_name)
    # print(1)
    print(pygame.mixer.music.load(str(file_name)))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops, start)
    # music = pygame.mixer.Sound(str(file_name))
    # music.set_volume(volume)
    # time_delay = round(music.get_length(),2)
    # music.play()
    # time.sleep(time_delay)


def music_set_volume(value=0.5):
    pygame.mixer.music.set_volume(value)

def music_stop():
    pygame.mixer.music.stop()

def music_pause():
    pygame.mixer.music.pause()

def music_unpause():
    pygame.mixer.music.unpause()

def sound_length(file_name):
    music = pygame.mixer.Sound(str(file_name))
    return round(music.get_length(),2)


if __name__=='__main__':
    # for i in range(5):
    # sound_effect_threading('Weapon_Armor.wav',volume = 0.1)
    # print("abc")
    # time.sleep(1)
    # # time.sleep(5)
    # background_music("go.mp3",volume = 0.1)
    record_play('4.mp3')
    while True:
        pass
#     print(sound_length("ss.wav"))
#     while True:
#         pass
        # sound_effect_play("ss.wav")
        # music_set_volume(value=0.5)
        # print("0.5")
        # time.sleep(5)
        # sound_effect_play("ss.wav")
        # music_set_volume(value=0.1)
        # print("0.1")
        # time.sleep(5)
        # music_pause()
        # print("pause")
        # time.sleep(5)
        # music_unpause()
        # print("unpause")
        # time.sleep(5)
        # music_stop()
        # print("stop")
        # time.sleep(5)

    # for i in range(3):
    #     sound_effect_play("ss.wav",volume=0.1+i*0.2)
    #     print("ok")
    # time.sleep(5)
    # sound_effect_threading("ss.wav",volume=0.8)
    # return 1
    

