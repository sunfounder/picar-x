""" Drive the car forward and then stop """

from picarx_improved import Picarx
import time
import logging

def drive_forward():
    """ Drives car forward
    """
    px = Picarx()
    px.forward(30)
    px.set_dir_servo_angle(0)
    time.sleep(6)
    px.forward(0)

if __name__ == "__main__":
    drive_forward()
    
