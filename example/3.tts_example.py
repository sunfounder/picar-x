from time import sleep
from picarx import Music, TTS
from picarx.music import MusicFiles, SoundFiles, MusicStatus
import readchar
from os import geteuid

if geteuid() != 0:
    print(f"\033[0;33m{'The program needs to be run using sudo, otherwise there may be no sound.'}\033[0m")

music = Music()
tts = TTS()

manual = '''
Input key to call the function!
    space: Play sound effect (Car horn)
    c: Play sound effect with threads
    t: Text to speak
    q: Play/Stop Music
'''

def main():
    print(manual)

    flag_bgm = False
    music.set_volume(20)

    while True:
        key = readchar.readkey()
        key = key.lower()
        if key == "q":
            flag_bgm = not flag_bgm
            if flag_bgm is True:
                print('Play Music')
                music.play_music_background(MusicFiles.SLOW_TRAIL)
            else:
                print('Stop Music')
                music.music_control(MusicStatus.STOP)

        elif key == readchar.key.SPACE:
            print('Beep beep beep !')
            music.play_sound(SoundFiles.DOUBLE_HORN)
            sleep(0.05)

        elif key == "c":
            print('Beep beep beep !')
            music.play_sound_background(SoundFiles.DOUBLE_HORN)
            sleep(0.05)

        elif key == "t":
            words = "Hello"
            print(f'{words}')
            tts.say(words)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        print("Stop and exit")
        sleep(0.1)
