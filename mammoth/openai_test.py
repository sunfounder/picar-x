
from openai_helper import OpenAiHelper
import speech_recognition as sr
from secret import OPENAI_API_KEY, OPENAI_ASSISTANT_ID
from utils import *
import time



openai = OpenAiHelper(
    api_key=OPENAI_API_KEY,
    assistant_id=OPENAI_ASSISTANT_ID,
    assistant_name="robot",
)
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.16
recognizer.dynamic_energy_ratio = 1.6


def listen(language=[]):
    # recording audio
    print(f"[INFO] listening...")
    with sr.Microphone(chunk_size=8192) as source:
        cancel_redirect_error() # restore error print
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    print(f"[INFO] audio recorded, length: {len(audio.frame_data)}")

    # stt
    st = time.time()
    print(f"[INFO] stt...")
    result = openai.stt(audio, language=language)
    if len(result) > 65535:
        print(f"[WARN] listen result is too long, {len(result)} > 65535, cut to 65535")
        result = result[:65535]
    print(f"[INFO] result: {result}")

listen()

