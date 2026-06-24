---
name: picarx-control
description: "Control a SunFounder PiCar-X robot car: drive, steer, sense, camera gimbal, play sounds, camera vision."
homepage: https://docs.sunfounder.com/projects/picar-x/en/latest/
metadata:
  openclaw:
    emoji: "🚗"
    requires:
      bins: ["python3"]
      python: ["picarx", "robot_hat", "vilib"]
---

# PiCar-X Control Skill

You are controlling a **PiCar-X** robot car — a Raspberry Pi with 2 rear drive motors, a front steering servo, a 2-axis camera gimbal (pan/tilt), an ultrasonic distance sensor, a 3-channel grayscale module, and a PiCamera with speaker.

When the user talks to you in natural language ("drive forward", "turn left", "check if there's an obstacle ahead"), use `exec` to run Python code on the robot's Raspberry Pi. Examples below show exactly what to exec.

## Safety Rules — Always Follow These

1. **Start slow**: Use speed=30 for testing, 50 for normal driving, 80 max. Reduce speed when turning.
2. **Stop after each action**: Always call `car.stop()` after completing a movement sequence.
3. **Check surroundings first**: If the user asks to move, consider checking the ultrasonic distance first.
4. **Flat surface**: Ensure the car is on a flat, clear surface before driving.
5. **Don't run multiple moves simultaneously**: Wait for one action (including delays) to finish before starting the next.
6. **Steering angle**: Keep between -30 and 30. Use smaller angles (15-20) at higher speeds.

## ⚠️ Grayscale Sensor ADC Poisoning — Quick Rules

`Picarx.__init__()` calls `reset_mcu()`, which reboots the Robot HAT's STM32 co-processor. If this happens AFTER ADC objects already exist, the ADC is poisoned and returns fake values **`[2571, 3085, 3599]`** forever. Real readings are **0–2000** with slight variation between reads.

**Two simple rules to avoid poisoning entirely:**

| If you need... | Do this | Poison risk |
|---|---|---|
| Only grayscale (no movement) | Just create `Grayscale_Module` with `ADC`. Don't import Picarx. | Zero |
| Movement + grayscale (e.g. line tracking) | Create `Picarx` FIRST, then create `Grayscale_Module` with fresh `ADC` objects after. | Zero |

```python
# ✅ Only grayscale — no Picarx at all
from robot_hat import ADC, Grayscale_Module
gs = Grayscale_Module(ADC("A0"), ADC("A1"), ADC("A2"), reference=[1000, 1000, 1000])

# ✅ Movement + grayscale — Picarx FIRST, then ADC
from picarx import Picarx
from robot_hat import ADC, Grayscale_Module
car = Picarx()                                                              # ← reset_mcu happens here
gs = Grayscale_Module(ADC("A0"), ADC("A1"), ADC("A2"), reference=[1000, 1000, 1000])  # ← safe: ADC created after

# ❌ ADC before Picarx — WILL be poisoned
gs = Grayscale_Module(ADC("A0"), ADC("A1"), ADC("A2"), reference=[1000, 1000, 1000])
car = Picarx()  # ← reset_mcu kills the existing ADC!
```

**Safety net**: As a final safeguard, always validate the first reading. If it's `[2571, 3085, 3599]`, discard and re-create the `Grayscale_Module` with fresh `ADC` objects.

## Recognition Mapping — What the User Said → What You Run

| User says... | You should exec... |
|---|---|
| "drive forward / go forward / move ahead" | `car.forward(speed) → sleep → car.stop()` |
| "go backward / reverse / move back" | `car.backward(speed) → sleep → car.stop()` |
| "turn left" | `car.set_dir_servo_angle(-30) → drive forward briefly → straighten → stop` |
| "turn right" | `car.set_dir_servo_angle(30) → drive forward briefly → straighten → stop` |
| "look left" | `car.set_cam_pan_angle(60)` |
| "look right" | `car.set_cam_pan_angle(-60)` |
| "look up" | `car.set_cam_tilt_angle(40)` |
| "look down" | `car.set_cam_tilt_angle(-20)` |
| "look straight / look ahead" | `car.set_cam_pan_angle(0) + car.set_cam_tilt_angle(0)` |
| "is there something ahead / measure distance" | `exec ultrasonic read, return the value to user` |
| "make a sound / honk / play sound" | `music.sound_play(path) or music.music_play(path)` |
| "take a photo / take a picture" | `Vilib.take_photo() → tell user where it saved` |
| "detect faces / look at me" | `Vilib.face_detect_switch(True) → read result → tell user` |
| "find red / find blue / locate color..." | `Vilib.color_detect('red') → read coordinates → tell user` |
| "follow the line" | ⚠️ Create Grayscale_Module for sensor + Picarx for movement. Validate readings aren't poisoned [2571, 3085, 3599]. |
| "check cliff / check for cliff" | ⚠️ Read grayscale, check if any channel <= 500. Validate reading first. |
| "read grayscale / what are the grayscale values" | ⚠️ Create Grayscale_Module with direct ADC. Validate reading isn't poisoned before reporting. |
| "detect QR code / scan QR" | `Vilib.qrcode_detect_switch(True) → read qr_data` |
| "recognize gesture" | `Vilib.gesture_detect_switch(True) → read gesture_t` |
| "detect traffic sign" | `Vilib.traffic_sign_detect_switch(True) → read traffic_sign_t` |

Response style: When you successfully execute a command, briefly tell the user what happened in a friendly tone. e.g. "Driving forward 🚗" or "Turned right, the path looks clear" or "There's an obstacle 23 cm ahead."

## exec Code Templates

### Basic Movement — Drive Forward

```python
from picarx import Picarx
from time import sleep
car = Picarx()
try:
    car.forward(50)       # speed 0-100
    sleep(1.0)            # adjust duration for distance
finally:
    car.stop()
```

### Basic Movement — Drive Backward

```python
from picarx import Picarx
from time import sleep
car = Picarx()
try:
    car.backward(50)
    sleep(1.0)
finally:
    car.stop()
```

### Turn Left / Right

```python
from picarx import Picarx
from time import sleep
car = Picarx()
try:
    car.set_dir_servo_angle(-30)   # -30=left, 30=right
    sleep(0.3)
    car.forward(30)                # slow speed while turning
    sleep(0.8)
    car.set_dir_servo_angle(0)     # straighten wheels
    sleep(0.3)
finally:
    car.stop()
```

### Adjust Camera Gimbal

```python
from picarx import Picarx
car = Picarx()
car.set_cam_pan_angle(60)     # range: -90 to 90
# car.set_cam_tilt_angle(40)  # range: -35 to 65
```

To reset camera to center:
```python
car.set_cam_pan_angle(0)
car.set_cam_tilt_angle(0)
```

### Read Ultrasonic Distance

```python
from picarx import Picarx
car = Picarx()
d = car.get_distance()
print(f"{d:.1f}" if d else "None")
```

Parse `stdout` from exec output to get the distance value in cm.

### Read Grayscale Sensor (Line Tracking / Cliff Detection)

Use direct ADC and auto-calibrate the reference from a few samples:

```python
from robot_hat import ADC, Grayscale_Module
from time import sleep
adc0, adc1, adc2 = ADC("A0"), ADC("A1"), ADC("A2")

# Auto-calibrate: sample a few readings, set reference to their midpoint
gs = Grayscale_Module(adc0, adc1, adc2, reference=[200, 200, 200])
sleep(0.3)
samples = [gs.read() for _ in range(3)]
# Reference = average of sampled values (midpoint between black line and white surface)
ref = [sum(s[i] for s in samples) // len(samples) for i in range(3)]
gs.reference(ref)
print(f"Auto ref: {ref}")

data = gs.read()
print(f"Grayscale: {data}")
```

Check line status:
```python
status = gs.read_status(data)
print(status)  # [0,0,0]=all_black, [0,1,0]=center_white=forward, etc.
```

Check cliff (any channel below threshold = cliff):
```python
is_cliff = any(data[i] <= 500 for i in range(3))
print(f"Cliff detected: {is_cliff}")
```

### Play Sound Effects

```python
from robot_hat import Music
music = Music()
music.music_set_volume(50)
music.sound_play('/path/to/sound.wav')
# or non-blocking: music.sound_play_threading('/path/to/sound.wav')
# or background music: music.music_play('/path/to/music.wav')
```

Set volume only:
```python
music.music_set_volume(80)  # 0-100
```

Stop playback:
```python
music.music_stop()
```

### Take a Photo

```python
from vilib import Vilib
from time import sleep, strftime, localtime
from os.path import expanduser
Vilib.camera_start(vflip=False, hflip=False)
Vilib.display(local=True, web=True)
sleep(1)
name = f"photo_{strftime('%Y-%m-%d-%H-%M-%S', localtime())}"
Vilib.take_photo(name, expanduser('~/Pictures/'))
Vilib.camera_close()
print(f"saved: {expanduser('~/Pictures/')}{name}.jpg")
```

### Detect Faces

```python
from vilib import Vilib
from time import sleep
Vilib.camera_start(vflip=False, hflip=False)
Vilib.display(local=True, web=True)
sleep(1)
Vilib.face_detect_switch(True)
sleep(2)
n = Vilib.detect_obj_parameter.get('human_n', 0)
if n > 0:
    x = Vilib.detect_obj_parameter.get('human_x')
    y = Vilib.detect_obj_parameter.get('human_y')
    print(f"Detected {n} face(s), center at ({x}, {y})")
else:
    print("No faces detected")
Vilib.camera_close()
```

### Detect Colors

```python
from vilib import Vilib
from time import sleep
Vilib.camera_start(vflip=False, hflip=False)
Vilib.display(local=True, web=True)
sleep(1)
Vilib.color_detect('red')   # options: red, orange, yellow, green, blue, purple, close
sleep(2)
n = Vilib.detect_obj_parameter.get('color_n', 0)
if n > 0:
    x = Vilib.detect_obj_parameter.get('color_x')
    y = Vilib.detect_obj_parameter.get('color_y')
    print(f"Detected {n} color block(s), center at ({x}, {y})")
else:
    print("No color blocks detected")
Vilib.camera_close()
```

### QR Code / Gesture / Traffic Sign Detection

```python
from vilib import Vilib
from time import sleep
Vilib.camera_start(vflip=False, hflip=False)
Vilib.display(local=True, web=True)
sleep(1)
Vilib.qrcode_detect_switch(True)         # QR codes
# Vilib.gesture_detect_switch(True)      # rock/paper/scissor
# Vilib.traffic_sign_detect_switch(True) # stop/left/right/forward
sleep(2)

# QR code result
qr_data = Vilib.detect_obj_parameter.get('qr_data', '')
if qr_data:
    print(f"QR code: {qr_data}")
else:
    print("No QR code detected")

# Gesture result
# gesture_type = Vilib.detect_obj_parameter.get('gesture_t', '')
# print(f"Gesture: {gesture_type}")

# Traffic sign result
# sign_type = Vilib.detect_obj_parameter.get('traffic_sign_t', '')
# print(f"Traffic sign: {sign_type}")

Vilib.camera_close()
```

### Line Tracking Loop (Continuous)

Picarx first, then Grayscale_Module with auto-calibrated reference:

```python
from picarx import Picarx
from robot_hat import ADC, Grayscale_Module
from time import sleep

# Order: Picarx FIRST (reset_mcu), then ADC — avoids poisoning
car = Picarx()
gs = Grayscale_Module(ADC("A0"), ADC("A1"), ADC("A2"), reference=[200, 200, 200])
sleep(0.3)

# Safety check + auto-calibrate reference from current surface
if gs.read() == [2571, 3085, 3599]:
    gs = Grayscale_Module(ADC("A0"), ADC("A1"), ADC("A2"), reference=[200, 200, 200])
    sleep(0.3)
samples = [gs.read() for _ in range(3)]
ref = [sum(s[i] for s in samples) // len(samples) for i in range(3)]
gs.reference(ref)
print(f"Auto ref: {ref}")

try:
    for _ in range(50):  # adjust loop count
        gm_data = gs.read()
        if gm_data == [2571, 3085, 3599]:
            continue      # skip poisoned reading
        status = gs.read_status(gm_data)
        if status == [0, 1, 0]:    # center on white → go forward
            car.set_dir_servo_angle(0)
            car.forward(30)
        elif status == [1, 1, 0]:  # left on white → turn left
            car.set_dir_servo_angle(25)
            car.forward(30)
        elif status == [0, 1, 1]:  # right on white → turn right
            car.set_dir_servo_angle(-25)
            car.forward(30)
        else:                       # all black or all white → stop
            car.stop()
            break
        sleep(0.05)
finally:
    car.stop()
```

## Typical Conversation Flow

**User:** "drive forward"
**AI executes:** the "Basic Movement — Drive Forward" template above
**AI replies:** "Driving forward now 🚗"

**User:** "turn left"
**AI executes:** the "Turn Left / Right" template, with `set_dir_servo_angle(-30)`
**AI replies:** "Turning left — path looks clear"

**User:** "check if there's something ahead"
**AI executes:** the "Read Ultrasonic Distance" template
**AI replies:** "There's an obstacle about 23 cm ahead" / "The path is clear ahead"

**User:** "look to the right"
**AI executes:** the "Adjust Camera Gimbal" template with `set_cam_pan_angle(-60)`
**AI replies:** "Looking to the right now"

**User:** "take a photo"
**AI executes:** the "Take a Photo" template
**AI replies:** "Photo saved to ~/Pictures/photo_2026-01-15-14-30-22.jpg"

**User:** "follow the line"
**AI executes:** the "Line Tracking Loop" template
**AI replies:** "Following the line... I'll stop if I lose track"

## Full API Reference

See `references/api.md` for all available methods:
- `Picarx` — forward, backward, stop, set_dir_servo_angle, set_cam_pan_angle, set_cam_tilt_angle, get_distance, get_grayscale_data, get_line_status, get_cliff_status, set_power, reset, close
- `Vilib` — camera_start, camera_close, display, take_photo, face_detect_switch, color_detect, qrcode_detect_switch, gesture_detect_switch, traffic_sign_detect_switch, detect_obj_parameter
- `Music` — music_set_volume, sound_play, sound_play_threading, music_play, music_stop, music_pause, music_resume
- `Ultrasonic` — read (returns cm)
- `Grayscale_Module` — read, read_status, reference
- `Pin`, `PWM`, `Servo`, `ADC` — low-level hardware control

## Helper Script (Optional)

There's also a CLI convenience script at `scripts/pc.py` — same functions, but prefer direct Python inline via exec for more control.
