# Installation:
# pip install piper-tts

import os
import time
from picarx.music import Music

music = Music()

def say(text):
    start = time.time()
    os.system(f"echo {text} | piper --model en_US-danny-low  --output_file tts.wav")
    during = time.time() - start
    during = round(during, 3)
    print(f"Time taken: {during} seconds")
    # os.system("aplay tts.wav")
    music.play_sound("tts.wav")

while True:
    text = input("Enter text to say: ")
    say(text)
