#!/usr/bin/env python3

print('Please run under desktop environment (eg: vnc) to display the image window')

'''
# We have integrated the camera-related functions into the vilb library,
# you can use the following code to achieve the same functionality.

from vilib import Vilib
import time

try:
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    time.sleep(2)
    print('\npress  Ctrl+C to exit')
    while True:
        time.sleep(1)  # Keep the main thread alive to accept the KeyboardInterrupt signal
except KeyboardInterrupt:
    print('\nquit ...')
except Exception as e:
    print('error:%s'%e)
finally:
    Vilib.camera_close()

'''

import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time


with PiCamera() as camera:
    camera.resolution = (640, 480)  
    camera.framerate = 24
    rawCapture = PiRGBArray(camera, size=camera.resolution)  
    time.sleep(2)

    for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
        img = frame.array
        cv2.imshow("video", img)  # OpenCV image show
        rawCapture.truncate(0)  # Release cache
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    print('quit ...') 
    cv2.destroyAllWindows()
    camera.close()  

