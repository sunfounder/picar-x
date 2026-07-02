from picarx.voice_assistant import VoiceAssistant
from picarx.led import LED

from picarx.picarx import Picarx
from picarx.preset_actions import ActionFlow

import time
import threading
import random
import json

# Robot name
NAME = "Rolly"

# Ultrasonic sensor trigger distance
TOO_CLOSE = 10

# Keyboard enable
KEYBOARD_ENABLE = True

# Enable image, need to set up a multimodal language model
WITH_IMAGE = True

# Set models and languages
LLM_MODEL = "gpt-4o-mini"
STT_LANGUAGE = "en-us"

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
["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate", "depressed"]

## Sound Effects You Can Emit:
["honking", "start engine"]

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

class VoiceActiveCar(VoiceAssistant):
    VOICE_ACTIONS = ["honking", "start engine"]

    def __init__(self, *args,
            too_close: int = TOO_CLOSE,
            **kwargs):
        self.too_close = too_close

        super().__init__(*args, **kwargs)
        self.car = Picarx()
        self.led = LED()
        self.action_flow = ActionFlow(self.car)
        self.add_trigger(self.is_too_close)

    def before_listen(self):
        self.led.blink(times=2, delay=0.1, pause=0.8)

    def before_think(self, text):
        self.led.blink(delay=0.1)

    def on_start(self):
        self.action_flow.start()
        self.led.off()

    def on_wake(self):
        if len(self.answer_on_wake) > 0:
            self.led.on()

    def on_heard(self, text):
        pass

    def parse_response(self, text):
        result = text.strip().split('ACTIONS: ')

        response_text = result[0].strip()
        if len(result) > 1:
            actions = result[1].strip()
            if len(actions) > 0:
                actions = actions.split(', ')
            else:
                actions = ['stop']
        else:
            actions = ['stop']
        
        self.action_flow.add_action(*actions)
        
        return response_text

    def before_say(self, text):
        self.led.on()

    def after_say(self, text):
        self.action_flow.wait_actions_done()

        self.led.off()

    def is_too_close(self) -> tuple[bool, bool, str]:
        triggered = False
        disable_image = False
        message = ''

        distance = self.car.get_distance()
        if distance < self.too_close and distance > 1:
            print(f'Ultrasonic sense too close: {distance}cm')
            message = f'<<<Ultrasonic sense too close: {distance}cm>>>'
            disable_image = True
            self.action_flow.add_action('backward')
            triggered = True
        return triggered, disable_image, message

    def on_finish_a_round(self):
        # wait actions done
        self.action_flow.wait_actions_done()
        # close rgb strip
        self.led.off()

    def on_stop(self):
        print('on_stop')
        print("stop actions")
        self.action_flow.stop()
        print("close car")
        self.car.close()
        print("close led")
        self.led.close()
