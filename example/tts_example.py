from tts import TTS


if __name__ == "__main__":
    words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
    tts_robot = TTS()
    for i in words:
        tts.say(i)
