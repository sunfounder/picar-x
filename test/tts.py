from picarx import TTS

tts = TTS()

print("------ Available models ------")
print(tts.available_models())
print("")
print("------ Available countrys ------")
print(tts.available_countrys())
print("")
print("------ Available models in en_US ------")
print(tts.available_models("en_US"))
print("")

import time

# text = "The MODEL_CARD file for each voice contains important licensing information. Piper is intended for text to speech research, and does not impose any additional restrictions on voice models. Some voices may have restrictive licenses, however, so please review them carefully!"
# print(f"Stream TTS: {text}")
# start = time.time()
# tts.say(text)
# duration = time.time() - start
# duration = round(duration, 3)
# print(f"Duration: {duration} ms")

# print(f"TTS: {text}")
# start = time.time()
# tts.say(text, stream=False)
# duration = time.time() - start
# duration = round(duration, 3)
# print(f"Duration: {duration} ms")


while True:
    text = input("Enter text to say: ")
    start = time.time()
    tts.say(text)
    duration = time.time() - start
    duration = round(duration, 3)
    print(f"Duration: {duration} s")
