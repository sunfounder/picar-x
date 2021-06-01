# coding=utf-8
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

#init camera
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=camera.resolution)  


for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
    img = frame.array
    cv2.imshow("video", img)  # OpenCV image show
    rawCapture.truncate(0)  # Release cache
    
    # click ESC key to exit.
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        camera.close()
        break

        