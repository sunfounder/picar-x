# coding=utf-8
import sys
sys.path.append(r'/home/pi/picar-x/lib')
import cv2
from utils import reset_mcu
reset_mcu()
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
from picarx import Picarx
from utils import run_command
import datetime


camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
rawCapture = PiRGBArray(camera, size=camera.resolution)  

power_val = 0
px = Picarx()


try:
    while True:
        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
            img = frame.array
            cv2.imshow("video", img)    #opencv显示帧
            # 清除缓存
        
            k = cv2.waitKey(1) & 0xFF
            # 27是ESC键，表示如果按ESC键则退出
            # print(ord('esc'))
            if k == 27:
                camera.close()
                continue
            elif k == ord('o'):
                if power_val <=90:
                    power_val += 10
                    print("power_val:",power_val)  # 增大电机速度
            elif k == ord('p'):
                if power_val >=10:
                    power_val -= 10
                    print("power_val:",power_val)  #减小电机速度
            elif k == ord('w'):
                # print("w:",)
                px.set_dir_servo_angle(0)
                px.forward(power_val)
            elif k == ord('a'):
                px.set_dir_servo_angle(-30) # 左转
                px.forward(power_val)
            elif k == ord('s'):
                px.set_dir_servo_angle(0) # 后退
                px.backward(power_val)
            elif k == ord('d'):
                px.set_dir_servo_angle(30) # 右转
                px.forward(power_val)
            elif k == ord('f'):    
                px.stop()  #停下来

            

            elif k == ord('t'):   # 拍照
                camera.close()
                break
            rawCapture.truncate(0)

        print("take a photo wait...")
        picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

        a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path
        

        print(a_t)
        run_command(a_t)

        # Vilib.shuttle_button() 
        camera = PiCamera()
        camera.resolution = (640,480)
        camera.framerate = 24
        camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
finally:
    px.stop()
    camera.close()




        