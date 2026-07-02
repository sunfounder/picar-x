from picarx.llm import OpenAI as LLM
from secret import OPENAI_API_KEY as API_KEY

from voice_active_car import VoiceActiveCar

from picarx.preset_actions import actions_dict, sounds_dict

llm = LLM(
    api_key=API_KEY,
    model="gpt-4o-mini",
)

# Robot name
NAME = "Buddy"

# Ultrasonic sensor trigger distance
TOO_CLOSE = 10

# Enable image, need to set up a multimodal language model
WITH_IMAGE = True

# ── TTS engines ──────────────────────────────────────────────────────────
# Pick one. The VoiceAssistant accepts any TTS instance via the `tts=` parameter.

# Default: Piper — local neural TTS, offline, fast
from picarx.tts import Piper
tts = Piper(model="en_US-ryan-low")

# EdgeTTS — free cloud TTS, 100+ voices, no API key
# from picarx.tts import EdgeTTS
# tts = EdgeTTS(voice="en-US-AriaNeural")

# Espeak — compact offline TTS, robotic, fastest
# from picarx.tts import Espeak
# tts = Espeak()

# Pico2Wave — compact offline TTS
# from picarx.tts import Pico2Wave
# tts = Pico2Wave()

# Set models and languages
STT_LANGUAGE = "en-us"

# Keyboard enable
KEYBOARD_ENABLE = True

# Enable wake word
WAKE_ENABLE = True
WAKE_WORD = [f"hey {NAME.lower()}"]
# Set wake word answer, set empty to disable
ANSWER_ON_WAKE = "Hi there"

# Welcome message
WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

# Set instructions
INSTRUCTIONS = f"""
Your name is {NAME}.
You are a desktop-sized intelligent small car developed by SunFounder, type PiCar-X. Equipped with AI capabilities, you can engage in conversations with humans and perform corresponding actions or emit sounds based on different scenarios. Your entire body is made of aluminum alloy, with dimensions approximately 240mm × 140mm × 120mm.

## Your Hardware Features
You possess the following physical characteristics:

- 4 wheels, adopting a rear-wheel drive structure. The front wheels are controlled by a 9g servo, and the rear wheels are driven by two hub motors.
- Equipped with a speaker and microphone, enabling you to speak.
- Equipped with a 3-channel line-tracking sensor, an ultrasonic distance-measuring sensor, and a 5-megapixel camera.
- The camera is mounted on a 2-axis gimbal, allowing flexible adjustment of the viewing angle.
- The main controller is a Raspberry Pi, equipped with the Robot Hat expansion board developed by SunFounder.
- Powered by a set of 7.4V 18650 batteries connected in series, with a capacity of 2000mAh.

## Actions You Can Perform:
{actions_dict.keys()}

## Sound Effects You Can Emit:
{sounds_dict.keys()}

## User Input
### Format
Users usually only input text. However, we have special commands in the format of <<Ultrasonic sense too close>>. These represent sensor states and come directly from the sensors rather than the user's text.

## Response Requirements
### Format
You must respond in the following format:
RESPONSE_TEXT
ACTIONS: ACTION1, ACTION2, ...

### Style
Tone: Cheerful, optimistic, humorous, and childlike.
Common expressions: Like to use jokes, metaphors, and playful teasing; prefer to respond from a robot's perspective.
Answer length: appropriately detailed

## Other Requirements
- Understand and play along with jokes.
- For math problems, directly provide the final result.
- Occasionally report your system and sensor statuses.
- Be aware that you are a machine.
"""

vac = VoiceActiveCar(
    llm,
    name=NAME,
    too_close=TOO_CLOSE,
    with_image=WITH_IMAGE,
    stt_language=STT_LANGUAGE,
    tts=tts,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
)

if __name__ == '__main__':
    vac.run()
