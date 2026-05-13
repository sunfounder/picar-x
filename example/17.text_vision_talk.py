from picarx.llm import Ollama
from picamera2 import Picamera2
import time

"""
You need to set up Ollama first.

Note: At least 8GB RAM is recommended for small vision models (e.g., moondream:1.8b).
      For llava:7b, more memory is preferred (≥16GB).
"""

INSTRUCTIONS = "You are a helpful assistant."
WELCOME = "Hello, I am a helpful assistant. How can I help you?"

# If Ollama runs on the same Pi, use "localhost".
# If it runs on another computer in your LAN, replace with that computer's IP.
llm = Ollama(
    ip="localhost",          # e.g., "192.168.100.145" if remote
    model="llava:7b"         # change to "moondream:1.8b" or "granite3.2-vision:2b" for 8GB RAM
)

# Basic configuration
llm.set_max_messages(20)
llm.set_instructions(INSTRUCTIONS)
llm.set_welcome(WELCOME)

# Init camera
camera = Picamera2()
config = camera.create_still_configuration(
    main={"size": (1280, 720)},
)
camera.configure(config)
camera.start()
time.sleep(2)

print(WELCOME)

while True:
    input_text = input(">>> ")
    if input_text.strip().lower() in {"exit", "quit"}:
        break

    # Capture image
    img_path = "/tmp/llm-img.jpg"
    camera.capture_file(img_path)

    # Response with stream (text + image)
    response = llm.prompt(input_text, stream=True, image_path=img_path)
    for next_word in response:
        if next_word:
            print(next_word, end="", flush=True)
    print("")
