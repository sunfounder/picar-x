from openai import OpenAI
from enum import StrEnum
import time
import shutil
import os

STT_LANGUAGES = {
  "Afrikaans": "af",
  "Arabic": "ar",
  "Armenian": "hy",
  "Azerbaijani": "az",
  "Belarusian": "be",
  "Bosnian": "bs",
  "Bulgarian": "bg",
  "Catalan": "ca",
  "Chinese": "zh",
  "Croatian": "hr",
  "Czech": "cs",
  "Danish": "da",
  "Dutch": "nl",
  "English": "en",
  "Estonian": "et",
  "Finnish": "fi",
  "French": "fr",
  "Galician": "gl",
  "German": "de",
  "Greek": "el",
  "Hebrew": "he",
  "Hindi": "hi",
  "Hungarian": "hu",
  "Icelandic": "is",
  "Indonesian": "id",
  "Italian": "it",
  "Japanese": "ja",
  "Kannada": "kn",
  "Kazakh": "kk",
  "Korean": "ko",
  "Latvian": "lv",
  "Lithuanian": "lt",
  "Macedonian": "mk",
  "Malay": "ms",
  "Marathi": "mr",
  "Maori": "mi",
  "Nepali": "ne",
  "Norwegian": "no",
  "Persian": "fa",
  "Polish": "pl",
  "Portuguese": "pt",
  "Romanian": "ro",
  "Russian": "ru",
  "Serbian": "sr",
  "Slovak": "sk",
  "Slovenian": "sl",
  "Spanish": "es",
  "Swahili": "sw",
  "Swedish": "sv",
  "Tagalog": "tl",
  "Tamil": "ta",
  "Thai": "th",
  "Turkish": "tr",
  "Ukrainian": "uk",
  "Urdu": "ur",
  "Vietnamese": "vi",
  "Welsh": "cy",
}

TTS_VOICES = [
    "alloy",
    "ash",
    "ballad",
    "coral",
    "echo",
    "fable",
    "nova",
    "onyx",
    "sage",
    "shimmer"
]

class AIStatus(StrEnum):
    """AI状态枚举（字符串类型）"""
    NOT_INITIALIZED = "NOT_INITIALIZED"
    INITIALIZING = "INITIALIZING"
    IDLE = "IDLE"
    FAILED = "FAILED"
    LISTENING = "LISTENING" 
    STT = "STT"
    TTS = "TTS"
    THINKING = "THINKING"
    SPEAKING = "SPEAKING"

# utils
# =================================================================
def chat_print(label, message):
    width = shutil.get_terminal_size().columns
    msg_len = len(message)
    line_len = width - 27

    # --- normal print ---
    print(f'{time.time():.3f} {label:>6} >>> {message}')
    return

    # --- table mode ---
    if width < 38 or msg_len <= line_len:
        print(f'{time.time():.3f} {label:>6} >>> {message}')
    else:
        texts = []

        # words = message.split()
        # print(words)
        # current_line = ""
        # for word in words:
        #     if len(current_line) + len(word) + 1 <= line_len:
        #         current_line += word + " "
        #     else:
        #         texts.append(current_line)
        #         current_line = ""

        # if current_line:
        #     texts.append(current_line)

        for i in range(0, len(message), line_len):
            texts.append(message[i:i+line_len])

        for i, text in enumerate(texts):
            if i == 0:
                print(f'{time.time():.3f} {label:>6} >>> {text}')
            else:
                print(f'{"":>26} {text}')

# OpenAiHelper
# =================================================================
class OpenAiHelper():
    STT_OUT = "stt_output.wav"
    TTS_OUTPUT_FILE = 'tts_output.mp3'
    TIMEOUT = 30 # seconds

    def __init__(self, api_key, assistant_id, assistant_name, timeout=TIMEOUT) -> None:
        
        self.api_key = api_key
        self.assistant_id = assistant_id
        self.assistant_name = assistant_name

        self.client = OpenAI(api_key=api_key, timeout=timeout)
        self.thread = self.client.beta.threads.create()
        self.run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=assistant_id,
        )

    def stt(self, audio, language='auto'):
        try:
            from io import BytesIO

            wav_data = BytesIO(audio.get_wav_data())
            wav_data.name = self.STT_OUT

            options = {
                "model": "whisper-1",
                "file": wav_data,
            }

            if language in STT_LANGUAGES.values():
                options['language'] = language
            elif language != 'auto':
                print(f"[Warning] stt language not supported: {language}")

            transcript = self.client.audio.transcriptions.create(**options)
            return transcript.text
        except Exception as e:
            print(f"stt err:{e}")
            return False

    def speech_recognition_stt(self, recognizer, audio):
        import speech_recognition as sr

        # # recognize speech using Sphinx
        # try:
        #     print("Sphinx thinks you said: " + r.recognize_sphinx(audio, language="en-US"))
        # except sr.UnknownValueError:
        #     print("Sphinx could not understand audio")
        # except sr.RequestError as e:
        #     print("Sphinx error; {0}".format(e))

        # recognize speech using whisper
        # try:
        #     print("Whisper thinks you said: " + r.recognize_whisper(audio, language="english"))
        # except sr.UnknownValueError:
        #     print("Whisper could not understand audio")
        # except sr.RequestError as e:
        #     print(f"Could not request results from Whisper; {e}")

        # recognize speech using Whisper API
        try:
            return recognizer.recognize_whisper_api(audio, api_key=self.api_key)
        except sr.RequestError as e:
            print(f"Could not request results from Whisper API; {e}")
            return False

    def dialogue(self, msg):
        chat_print("user", msg)
        message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=msg
            )
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
        )
        if run.status == 'completed': 
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id
            )

            for message in messages.data:
                if message.role == 'assistant':
                    for block in message.content:
                        if block.type == 'text':
                            value = block.text.value
                            chat_print(self.assistant_name, value)
                            try:
                                value = eval(value) # convert to dict
                                return value
                            except Exception as e:
                                return str(value)
                break # only last reply
        else:
            print(run.status)


    def dialogue_with_img(self, msg, img_path):
        chat_print(f"user", msg)

        img_file = self.client.files.create(
                    file=open(img_path, "rb"),
                    purpose="vision"
                )

        message =  self.client.beta.threads.messages.create(
            thread_id= self.thread.id,
            role="user",
            content= [
                {
                    "type": "text",
                    "text": msg
                },
                # {
                # "type": "image_url",
                # "image_url": {"url": "https://example.com/image.png"}
                # },
                {
                    "type": "image_file",
                    "image_file": {"file_id": img_file.id}
                }
            ],
            )
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=self.thread.id,
            assistant_id=self.assistant_id,
        )
        if run.status == 'completed': 
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id
            )

            for message in messages.data:
                if message.role == 'assistant':
                    for block in message.content:
                        if block.type == 'text':
                            value = block.text.value
                            chat_print(self.assistant_name, value)
                            try:
                                value = eval(value) # convert to dict
                                return value
                            except Exception as e:
                                return str(value)
                break # only last reply
        else:
            print(run.status)


    def text_to_speech(self, text, output_file, voice='alloy', response_format="mp3", speed=1):
        '''
        voice: alloy, echo, fable, onyx, nova, and shimmer
        '''
        if voice not in TTS_VOICES:
            print(f"[Warning] tts voice not supported: {voice}")
            voice = 'alloy'
        try:
            # check dir
            dir = os.path.dirname(output_file)
            if not os.path.exists(dir):
                os.mkdir(dir)
            elif not os.path.isdir(dir):
                raise FileExistsError(f"\'{dir}\' is not a directory")

            # tts
            with self.client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice=voice,
                input=text,
                response_format=response_format,
                speed=speed,
            ) as response:
                response.stream_to_file(output_file)

            return True
        except Exception as e:
            print(f'tts err: {e}')
            return False

