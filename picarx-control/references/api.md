# PiCar-X Python API Reference

This is the reference for programming PiCar-X directly from Python.
The OpenClaw AI agent should read this when it needs precise API signatures.

## picarx.Picarx

```python
from picarx import Picarx
car = Picarx(
    servo_pins=['P0', 'P1', 'P2'],       # cam_pan, cam_tilt, dir_servo
    motor_pins=['D4', 'D5', 'P13', 'P12'], # left_dir, right_dir, left_pwm, right_pwm
    grayscale_pins=['A0', 'A1', 'A2'],    # 3-channel ADC
    ultrasonic_pins=['D2', 'D3'],          # trig, echo
    config='/opt/picar-x/picar-x.conf'
)
```

Resets the MCU on init (~0.2s delay).

### Constants

| Constant | Value | Description |
|---|---|---|
| `DIR_MIN` | -30 | Minimum steering angle |
| `DIR_MAX` | 30 | Maximum steering angle |
| `CAM_PAN_MIN` | -90 | Minimum camera pan angle |
| `CAM_PAN_MAX` | 90 | Maximum camera pan angle |
| `CAM_TILT_MIN` | -35 | Minimum camera tilt angle |
| `CAM_TILT_MAX` | 65 | Maximum camera tilt angle |

### Movement

#### forward(speed)
Drive forward at the given speed (0-100).

```python
car.forward(50)
sleep(1.0)
car.stop()
```

#### backward(speed)
Drive backward at the given speed (0-100).

```python
car.backward(50)
sleep(1.0)
car.stop()
```

#### set_power(speed)
Set both motors to the same speed. Positive = forward, negative = backward.

```python
car.set_power(50)   # forward
car.set_power(-50)  # backward
```

#### stop()
Stop both motors immediately. Executes twice for reliability.

```python
car.stop()
```

#### set_motor_speed(motor, speed)
Control individual motor speed.
- `motor`: 1 = left motor, 2 = right motor
- `speed`: -100 to 100 (negative = reverse)

### Steering

#### set_dir_servo_angle(value)
Set the front steering servo angle. Range: -30 (left) to 30 (right).

```python
car.set_dir_servo_angle(-30)  # full left
car.set_dir_servo_angle(0)    # center
car.set_dir_servo_angle(30)   # full right
```

#### dir_servo_calibrate(value)
Set and persist the steering servo calibration offset.

```python
car.dir_servo_calibrate(5)  # offset by +5 degrees
```

### Camera Gimbal

#### set_cam_pan_angle(value)
Rotate camera horizontally. Range: -90 (right) to 90 (left).

```python
car.set_cam_pan_angle(60)   # look left
car.set_cam_pan_angle(-60)  # look right
car.set_cam_pan_angle(0)    # center
```

#### set_cam_tilt_angle(value)
Tilt camera vertically. Range: -35 (down) to 65 (up).

```python
car.set_cam_tilt_angle(40)   # look up
car.set_cam_tilt_angle(-20)  # look down
car.set_cam_tilt_angle(0)    # center
```

#### cam_pan_servo_calibrate(value)
#### cam_tilt_servo_calibrate(value)
Set and persist camera gimbal calibration offsets.

### Sensors

#### get_distance()
Read the ultrasonic distance sensor. Returns distance in cm as float, or `None` if no echo received. May block up to timeout (0.02s default).

```python
d = car.get_distance()
if d is not None:
    print(f"Distance: {d:.1f} cm")
```

#### get_grayscale_data()
Read the 3-channel grayscale module. Returns a list of 3 float values `[left, center, right]`. Lower values = darker surface (black line), higher values = lighter surface.

```python
data = car.get_grayscale_data()
print(data)  # e.g. [200.5, 850.3, 210.1]
```

#### get_line_status(gm_val_list)
Interpret grayscale data into a line-tracking direction.
Returns one of: `"forward"`, `"left"`, `"right"`, `"stop"`.

```python
data = car.get_grayscale_data()
status = car.get_line_status(data)
```

#### get_cliff_status(gm_val_list)
Check if any grayscale channel value is below the cliff reference threshold.
Returns `True` if a cliff/drop is detected, `False` otherwise.

```python
data = car.get_grayscale_data()
if car.get_cliff_status(data):
    print("Cliff detected! Stop!")
    car.stop()
```

#### set_line_reference(value)
#### set_cliff_reference(value)
Set the reference thresholds for line tracking and cliff detection.
Both take a list of 3 float values.

```python
car.set_line_reference([200, 800, 200])
car.set_cliff_reference([500, 500, 500])
```

### Motor Calibration

#### motor_speed_calibration(value)
Adjust motor speed balance. Positive value compensates for right-drift, negative for left-drift.

#### motor_direction_calibrate(motor, value)
Set motor direction. `motor`: 1 or 2. `value`: 1 (normal) or -1 (reversed).

### Lifecycle

#### reset()
Stop motors and reset all servos (steering, pan, tilt) to center.

```python
car.reset()
```

#### close()
Reset and close the ultrasonic sensor. Call when done using the car.

```python
car.close()
```

## robot_hat.Ultrasonic

```python
from robot_hat import Ultrasonic, Pin
sonar = Ultrasonic(Pin("D2"), Pin("D3"), timeout=0.02)
distance = sonar.read()    # Returns cm as float, may block
```

Trigger on D2, echo on D3. The `read()` can block if no echo received.

## robot_hat.Music

```python
from robot_hat import Music
music = Music()

music.music_set_volume(30)           # 0-100
music.music_play(filename, loops=1, start=0.0, volume=None)
music.music_stop()
music.music_pause()
music.music_resume()

music.sound_play(filename, volume=None)            # Blocking SFX
music.sound_play_threading(filename, volume=None)  # Non-blocking SFX

music.play_tone_for(freq, duration)  # Play a tone at freq Hz for duration s
```

## robot_hat.Pin

```python
from robot_hat import Pin
pin = Pin("D2")  # Digital pin by name
```

Common pin names on Robot HAT: `D0`–`D5`, `P0`–`P13`, `A0`–`A3`.

## robot_hat.Grayscale_Module

```python
from robot_hat import Grayscale_Module, ADC
adc0, adc1, adc2 = ADC("A0"), ADC("A1"), ADC("A2")
gs = Grayscale_Module(adc0, adc1, adc2, reference=None)

gs.reference([200, 800, 200])  # Set reference values
data = gs.read()                # Read 3-channel values
status = gs.read_status(data)   # Get line status string
```

## vilib.Vilib (Camera & Vision)

```python
from vilib import Vilib

# Start camera and display
Vilib.camera_start(vflip=False, hflip=False)
Vilib.display(local=True, web=True)
# Now visible at http://<pi-ip>:9000/mjpg

# Detection switches
Vilib.face_detect_switch(True|False)
Vilib.color_detect('close'|'red'|'orange'|'yellow'|'green'|'blue'|'purple')
Vilib.qrcode_detect_switch(True|False)
Vilib.gesture_detect_switch(True|False)
Vilib.traffic_sign_detect_switch(True|False)

# Results in detect_obj_parameter dict:
Vilib.detect_obj_parameter['color_x']     # Color block center X (0-320)
Vilib.detect_obj_parameter['color_y']     # Color block center Y (0-240)
Vilib.detect_obj_parameter['color_w']     # Color block width
Vilib.detect_obj_parameter['color_h']     # Color block height
Vilib.detect_obj_parameter['color_n']     # Number of color blocks

Vilib.detect_obj_parameter['human_x']     # Face center X
Vilib.detect_obj_parameter['human_y']     # Face center Y
Vilib.detect_obj_parameter['human_w']     # Face width
Vilib.detect_obj_parameter['human_h']     # Face height
Vilib.detect_obj_parameter['human_n']     # Number of faces

Vilib.detect_obj_parameter['gesture_x']   # Gesture X
Vilib.detect_obj_parameter['gesture_y']   # Gesture Y
Vilib.detect_obj_parameter['gesture_t']   # Type: paper|scissor|rock

Vilib.detect_obj_parameter['traffic_sign_x']  # Sign X
Vilib.detect_obj_parameter['traffic_sign_y']  # Sign Y
Vilib.detect_obj_parameter['traffic_sign_t']  # Type: stop|right|left|forward

Vilib.detect_obj_parameter['qr_data']     # QR decoded text
Vilib.detect_obj_parameter['qr_x']        # QR X
Vilib.detect_obj_parameter['qr_y']        # QR Y

# Capture photo
from time import strftime, localtime
from os.path import expanduser
name = f"photo_{strftime('%Y-%m-%d-%H-%M-%S', localtime())}"
Vilib.take_photo(name, expanduser("~/Pictures/"))
# Saved as ~/Pictures/photo_....jpg

# Cleanup
Vilib.camera_close()
```

## Wiring Info

- Motors: L298N dual H-bridge via Robot HAT (D4/D5 direction, P13/P12 PWM)
- Steering servo: PCA9685 channel P2
- Camera pan servo: PCA9685 channel P0
- Camera tilt servo: PCA9685 channel P1
- Ultrasonic: Trig=D2, Echo=D3
- Grayscale module: 3x ADC (A0, A1, A2)
- Camera: PiCamera via CSI port
- I2S audio: Built into Robot HAT
- Power: 7-12V via Robot HAT barrel jack or 3-pin battery (18650 × 2)
