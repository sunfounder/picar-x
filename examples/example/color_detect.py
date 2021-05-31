# coding=utf-8
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np

color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}  #这里是颜色所代表的HSV颜色空间中的H的范围

kernel_5 = np.ones((5,5),np.uint8) #定义了一个5×5，元素值全为1的卷积核


def color_detect(img,color_name):

    # 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度
        resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  #为了降低计算量，把图片缩小尺寸为(160,120)
        hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
        # print(Vilib.lower_color)
        color_type = color_name
        
        mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )           # 3.inRange()：把介于lower/upper之间的为白色，其余黑色
        if color_type == 'red':
                mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
                mask = cv2.bitwise_or(mask, mask_2)

        morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)              #对图像执行开运算  

        contours, hierarchy = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          # 在morphologyEx_img中发现轮廓，轮廓按照面积从小到大排列
            # p=0
        color_area_num = len(contours) #统计轮廓的数量

        if color_area_num > 0: 
            for i in contours:    #遍历所有的轮廓
                x,y,w,h = cv2.boundingRect(i)      #将轮廓分解为识别对象的左上角坐标和宽、高

                    #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
                if w >= 8 and h >= 8: #因为图片缩减为原来的四分之一，所以要在原来的图片上画矩形把目标圈出来，就要把x,y,w,h乘以4
                    x = x * 4
                    y = y * 4 
                    w = w * 4
                    h = h * 4
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  #画矩形的框
                    cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# 添加字符描述

        return img,mask,morphologyEx_img


#init camera
print("start color detect")
camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=camera.resolution)  


for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
    img = frame.array
    img,img_2,img_3 =  color_detect(img,'red')  #颜色检测函数
    cv2.imshow("video", img)    #opencv显示帧
    cv2.imshow("mask", img_2)    #opencv显示帧
    cv2.imshow("morphologyEx_img", img_3)    #opencv显示帧
    rawCapture.truncate(0)  # 清除缓存
   
    k = cv2.waitKey(1) & 0xFF
    # 27是ESC键，表示如果按ESC键则退出
    if k == 27:
        camera.close()
        break

        