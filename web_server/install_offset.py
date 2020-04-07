from ezblock import Servo, PWM

dir_servo_pin = Servo(PWM('P2'))
camera_servo_pin1 = Servo(PWM('P0'))
camera_servo_pin2 = Servo(PWM('P1'))

dir_servo_pin.angle(0)
camera_servo_pin1.angle(0)
camera_servo_pin2.angle(0)