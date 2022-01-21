""" Functions for basic maneuvering """

from picarx_improved import Picarx
import logging
from time import sleep

# Setup logging format
logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO,
    datefmt="%H:%M:%S")

LEFT = 1
RIGHT = 2

def move(px: Picarx, speed: int, angle: int)->None:
    # Send movement commands to picar
    px.drivetrain.set_angle(angle)
    px.drivetrain.set_speed(speed)

def parallel_park(px: Picarx, dir: int)->None:
    # Setup sign for LEFT or RIGHT
    if dir == LEFT:
        sign = 1
    else:
        sign = -1
    # Set parking parameters
    speed = 30
    angle = 20
    pause_duration = 2 # seconds
    # Send robot commands for parking
    # Comments are for LEFT parking
    # Left forward
    move(px, speed, sign* -angle)
    sleep(pause_duration)
    # Right forward
    move(px, speed, sign * angle)
    sleep(pause_duration)
    # Left backward
    move(px, -speed, sign * -angle)
    sleep(pause_duration)
    # Right backward
    move(px, -speed, sign * angle)
    sleep(pause_duration)
    # Stop
    move(px, 0, 0)

def k_turn(px: Picarx, dir: int)->None:
    # Setup sign for LEFT or RIGHT
    if dir == LEFT:
        sign = 1
    else:
        sign = -1
    # Set turn parameters
    speed = 50
    angle = 30
    pause_duration = 1.5 # seconds
    # Send robot commands for turn
    # Comments are for LEFT K-turn
    # Left forward
    move(px, speed, sign*-angle)
    sleep(pause_duration)
    # Right backward
    move(px, -speed, sign*angle)
    sleep(pause_duration/2)
    # Left forward
    move(px, speed, sign*-angle)
    sleep(pause_duration)
    # Forward
    move(px, speed, 0)
    sleep(pause_duration/2)
    # Stop
    move(px, 0, 0)
