""" Functions for basic maneuvering """

from picarx_improved import Picarx
import logging

# Setup logging format
logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO,
    datefmt="%H:%M:%S")

def move(px: Picarx, speed: int, angle: int)->None:
    # Enforce speed boundaries
    max_speed = 100
    if speed > max_speed:
        logging.warning("Requested forwards speed higher than max speed. Set speed to max forwards speed.")
        speed = max_speed
    elif speed < -max_speed:
        logging.warning("Requsted backwards speed higher than max speed. Set speed to max backwards speed.")
        speed = -max_speed
    
    # Enforce angle boundaries
    max_angle = 30
    if angle > max_angle:
        logging.warning("Requested right-steering angle greater than max angle. Set angle to max angle right.")
        angle = max_angle
    elif angle < -max_angle:
        logging.warning("Requested left-steering angle greater than max angle. Set angle to max angle left.")
        angle = -max_angle

    # Send movement commands to picar
    if speed >= 0:
        px.forward(speed)
    else:
        px.backward(abs(speed))
    px.set_dir_servo_angle(angle)
