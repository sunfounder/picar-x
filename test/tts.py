from picarx import TTS

tts = TTS()

print("Available models:")
print(tts.available_models())
print("Available countrys:")
print(tts.available_countrys())
print("Available models in en_US:")
print(tts.available_models("en_US"))

tts.set_model("en_US-danny-low")
tts.say("Hello, world!")
