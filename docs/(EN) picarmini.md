# The documentation is used to illustrate the use of picar-x functions


## Methods
- set_motor_speed - Set the speed of the motor, the first parameter motor can be 1 or 2, representing different motors, followed by speed as a percentage of the size of the energy provided to the motor, the range is (0~100)
```python
set_motor_speed(motor, speed)
```

- motor_speed_calibration - Calibrate the speed of the motor, if the value is greater than 0, the speed of motor #1 is increased by the corresponding value, if it is less than 0, the speed of motor #2 is increased by the corresponding value, the range is (0~100)
```python
motor_speed_calibration(value)
```

- motor_direction_calibration - Adjust the direction of the motor, for motor installation error, or mismatch, resulting in incorrect wheel steering, the default is 0, just set the second parameter value to 1, the direction will be reversed
```python
motor_direction_calibration(motor, value)
```

- dir_servo_angle_calibration - Adjust the direction of the motor, for motor installation error, or mismatch, resulting in incorrect wheel steering, the default is 0, just set the second parameter value to 1, the direction will be reversed
```python
dir_servo_angle_calibration(value)
```

- set_dir_servo_angle - Set the angle of car direction servo, range (-90~90).
```python
set_dir_servo_angle(value)
```

- camera_servo1_angle_calibration -  Calibrate the angle of the servo under the camera, range (-90~90).
```python
camera_servo1_angle_calibration(value)
```

- camera_servo2_angle_calibration - Calibrate the angle of the servo above the camera, range (-90~90).
```python
camera_servo2_angle_calibration(value)
```

- set_camera_servo1_angle - Set the angle of the servo under the camera, range (-90~90).
```python
set_camera_servo1_angle(value)
```

- set_camera_servo2_angle - Set the angle of the servo above the camera, range (-90~90).
```python
set_camera_servo2_angle(value)
```

- get_adc_value - Get the adc value of the grayscale sensor, range (0~4095).
```python
get_adc_value()
```

- backward - Make the cart backward, speed range(-100~100).
```python
backward(speed)
```

- forward - Let the car advance, speed range(-100~100).
```python
forward(speed)
```

- stop - Stop the trolley.
```python
stop()
```

- Get_distance - Ultrasonic module to acquire distance.
```python
Get_distance()
```



     
