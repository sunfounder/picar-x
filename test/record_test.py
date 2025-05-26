import speech_recognition as sr
import wave
from io import BytesIO
import os

# speech_recognition init
# =================================================================
'''
recognizer.energy_threshold = 300  # minimum audio energy to consider for recording
recognizer.dynamic_energy_threshold = True
recognizer.dynamic_energy_adjustment_damping = 0.15
recognizer.dynamic_energy_ratio = 1.5
recognizer.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
recognizer.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

recognizer.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
recognizer.non_speaking_duration = 0.5  # seconds of non-speaking audio to keep on both sides of the recording

'''
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.16
recognizer.dynamic_energy_ratio = 1.6
# recognizer.pause_threshold = 0.8


while True:
    with sr.Microphone(chunk_size=8192) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        wav_data = BytesIO(audio.get_wav_data())
        wav_data.name = "stt_output.wav"
        
        file = "./stt_output.wav"
        with wave.open(file, "wb") as wf:
            wf.setnchannels(1)  # 单声道
            wf.setsampwidth(audio.sample_width)  # 采样宽度（来自AudioData）
            wf.setframerate(audio.sample_rate)  # 采样率（来自AudioData）
            wf.writeframes(audio.get_wav_data())

        os.system("aplay ./stt_output.wav")
