# coding=utf-8
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 


def human_face_detect(img):
        resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)         # 为了减少计算量，把图片resize to 为 320 x 240的尺寸
        gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # 转为灰度图
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # 在灰度图上检测人脸
        # print(len(faces))
        face_num = len(faces)   # 检测到的人脸数量
        max_area = 0
        if face_num  > 0:
            for (x,y,w,h) in faces:
                
                x = x*2   # 因为图像缩减为原本的二分之一，这里的x,y,w,h要乘以2
                y = y*2
                w = w*2
                h = h*2
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 用矩形框框住人脸位置
        
        return img

#init camera
print("start human face detect")
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=camera.resolution)  


for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
    img = frame.array
    img =  human_face_detect(img) # 人脸检测
    cv2.imshow("video", img)  # opencv显示帧
    rawCapture.truncate(0)  # 清除缓存
   
    k = cv2.waitKey(1) & 0xFF
    # 27是ESC键，表示如果按ESC键则退出
    if k == 27:
        camera.close()
        break

        