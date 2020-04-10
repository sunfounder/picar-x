#!/usr/bin/python3
from picarmini import dir_servo_angle_calibration
from picarmini import forward
from ezblock import delay
from picarmini import backward
from picarmini import set_dir_servo_angle
from picarmini import stop

dir_servo_angle_calibration(0)
def forever():
  forward(50)
  delay(1000)
  backward(50)
  delay(1000)
  forward(50)
  set_dir_servo_angle((-30))
  delay(1000)
  forward(50)
  set_dir_servo_angle(30)
  delay(1000)
  set_dir_servo_angle(0)
  stop()
  delay(2000)

if __name__ == "__main__":
    while True:
        forever()  