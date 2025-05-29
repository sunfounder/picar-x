import pyaudio
import wave
from vosk import Model, KaldiRecognizer
import time
import numpy as np
import collections

# Constants
DEVICE_INDEX = 1  # Update this to match your headset's device index
RATE = 44100  # Sample rate
CHUNK = 1024  # Frame size
FORMAT = pyaudio.paInt16
RECORD_SECONDS = 10  # Duration to record after detecting voice
THRESHOLD = 500  # Adjust this to match your environment's noise level
MODEL_PATH = "/opt/vosk-models/vosk-model-small-en-us-0.15"  # Path to your Vosk model
OUTPUT_FILE = "translate.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(
    format=FORMAT,
    channels=1,
    rate=RATE,
    input=True,
    # input_device_index=DEVICE_INDEX,
    frames_per_buffer=CHUNK
)

print("Listening for voice...")

def detect_voice(audio_chunk):
    """Return True if audio chunk likely contains a human voice."""
    # Decode byte data to int16
    try:
        audio_chunk = np.frombuffer(audio_chunk, dtype=np.int16)
    except ValueError as e:
        print(f"Error decoding audio chunk: {e}")
        return False

    # Inspect the range of audio data
    print(f"Min: {audio_chunk.min()}, Max: {audio_chunk.max()}")

    # Compute the volume
    volume = np.abs(audio_chunk).max()  # Use absolute to handle both +ve and -ve peaks
    print(f"Volume: {volume}")

    # Define threshold (adjust based on testing)
    THRESHOLD = 1500  # Adjust based on normalized scale
    return volume > THRESHOLD


# Parameters for silence detection
SILENCE_TIMEOUT = 2  # seconds of silence to stop recording
MAX_SILENCE_CHUNKS = int(SILENCE_TIMEOUT * RATE / CHUNK)  # Convert to chunk count

# Record audio with silence detection
frames = []
silent_chunks = 0

# Wait for voice
# Add a buffer to store audio chunks before voice is detected
pre_record_buffer = collections.deque(maxlen=int(RATE / CHUNK * 2))  # Buffer up to 2 seconds of audio

print("Listening for voice...")
while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    pre_record_buffer.append(data)  # Continuously store audio chunks
    if detect_voice(data):
        print("Voice detected! Starting recording...")
        frames.extend(pre_record_buffer)  # Include pre-recorded audio
        frames.append(data)  # Include the current chunk with voice
        break

print("Recording... Speak now.")
while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    frames.append(data)

    # Detect silence
    if not detect_voice(data):
        silent_chunks += 1
        if silent_chunks >= MAX_SILENCE_CHUNKS:
            print("Silence detected. Stopping recording...")
            break
    else:
        silent_chunks = 0  # Reset silence counter if voice is detected

# Stop and close stream
stream.stop_stream()
stream.close()
audio.terminate()

# The 'frames' list now contains the recorded audio data.

# Save audio to file
with wave.open(OUTPUT_FILE, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))

print(f"Audio recorded to {OUTPUT_FILE}")

# Start speech-to-text
print("Starting speech-to-text...")
start_time = time.perf_counter()

wf = wave.open(OUTPUT_FILE, "rb")
model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, wf.getframerate())
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print("Transcription:", rec.Result())

# End timer
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
