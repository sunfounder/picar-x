import numpy as np
import cv2
import threading

from importlib import import_module
import os
from flask import Flask, render_template, Response
from multiprocessing import Process, Manager
import time
# from utils import cpu_temperature
# from rgb_matrix import RGB_Matrix

app = Flask(__name__)
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def gen():
    """Video streaming generator function."""
    while True:  
        # frame = cv2.imread("123.jpeg")Vilib.q.get()  
        # print("1")
        # if Vilib.conn2.recv()
        # frame = cv2.imencode('.jpg', Vilib.conn2.recv())[1].tobytes() 
        # rt_img = np.ones((320,240),np.uint8)
        # print("2")
        # Vilib.frame = cv2.imencode('.jpg', Vilib.img_array[0])[1].tobytes()
        frame = cv2.imencode('.jpg', Vilib.img_array[0])[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        

@app.route('/mjpg')
def video_feed():
    # from camera import Camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame') 

def web_camera_start():
    app.run(host='0.0.0.0', port=8888,threaded=True)



class Vilib(object): 

    face_cascade = cv2.CascadeClassifier('/opt/ezblock/haarcascade_frontalface_default.xml') 
    kernel_5 = np.ones((5,5),np.uint8)#4x4的卷积核
    # color_default = 'blue'
    # color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[166,180]}
    # lower_color = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60])  
    # upper_color = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])
    # hdf_flag = False 
    # cdf_flag = False
    # stf_flag = False
    video_source = 0
    
    # human_object_counter = 0
    # detect_obj_parameter = np.array([0,0])
    # human_object_size = np.array([0,0]) 

    # color_object_counter = 0
    detect_obj_parameter = Manager().dict()
    img_array = Manager().list(range(2))
#Color_obj_parameter
    detect_obj_parameter['color_default'] = 'red'

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[166,180]}
    # lower_color = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60])  
    # upper_color = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])

    detect_obj_parameter['color_x'] = 160
    detect_obj_parameter['color_y'] = 120
    detect_obj_parameter['color_w'] = 0
    detect_obj_parameter['color_h'] = 0
    detect_obj_parameter['color_n'] = 0
    detect_obj_parameter['lower_color'] = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60]) 
    detect_obj_parameter['upper_color'] = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])
    

#Human_obj_parameter
    detect_obj_parameter['human_x'] = 160
    detect_obj_parameter['human_y'] = 120
    detect_obj_parameter['human_w'] = 0
    detect_obj_parameter['human_h'] = 0
    detect_obj_parameter['human_n'] = 0

#detect_switch
    detect_obj_parameter['hdf_flag'] = False
    detect_obj_parameter['cdf_flag'] = False
    # detect_obj_parameter['color_default'] = 'red'

    # color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[166,180]}
    # lower_color = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60])  
    # upper_color = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])


    rt_img = np.ones((320,240),np.uint8)
    front_view_img = np.zeros((240,320,3), np.uint8)
# 使用白色填充图片区域,默认为黑色
    # front_view_img.fill(255)       
    img_array[0] = rt_img
    # img_array = rt_img
    vi_img = np.ones((320,240),np.uint8)  

    @staticmethod
    def color_detect_object(obj_parameter):
        if obj_parameter == 'x':
            # print(Vilib.detect_obj_parameter['x'])          
            return int(Vilib.detect_obj_parameter['color_x']/107.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['color_y']/80.1)-1) #max_size_object_coordinate_y
        elif obj_parameter == 'width':
            return Vilib.detect_obj_parameter['color_w']   #objects_max_width
        elif obj_parameter == 'height':
            return Vilib.detect_obj_parameter['color_h']   #objects_max_height
        elif obj_parameter == 'number':      
            return Vilib.detect_obj_parameter['color_n']   #objects_count
        return None

    @staticmethod
    def human_detect_object(obj_parameter):
        if obj_parameter == 'x':
            # print(Vilib.detect_obj_parameter['x'])          
            return int(Vilib.detect_obj_parameter['human_x']/107.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['human_y']/80.1)-1) #max_size_object_coordinate_y
        elif obj_parameter == 'width':
            return Vilib.detect_obj_parameter['human_w']   #objects_max_width
        elif obj_parameter == 'height':
            return Vilib.detect_obj_parameter['human_h']   #objects_max_height
        elif obj_parameter == 'number':      
            return Vilib.detect_obj_parameter['human_n']   #objects_count
        return None


    @staticmethod
    def detect_color_name(color_name):
        Vilib.detect_obj_parameter['color_default'] = color_name
        Vilib.detect_obj_parameter['lower_color'] = np.array([min(Vilib.color_dict[Vilib.detect_obj_parameter['color_default']]), 60, 60])  
        Vilib.detect_obj_parameter['upper_color'] = np.array([max(Vilib.color_dict[Vilib.detect_obj_parameter['color_default']]), 255, 255])

    @staticmethod
    def camera_start(web_func = True):
        from multiprocessing import Process
        # Vilib.conn1, Vilib.conn2 = Pipe()
        # Vilib.q = Queue()
        
        
        worker_2 = Process(name='worker 2',target=Vilib.camera_clone)
        if web_func == True:
            worker_1 = Process(name='worker 1',target=web_camera_start)
            worker_1.start()
        worker_2.start()
        
        # if web_func == True:
        #     print("1")
        #     # from flask_camera import web_camera_start
        #     t2 = threading.Thread(target=web_camera_start)  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
        #     print("2")
        #     t2.start() #线程执行
        # print('cam')
        # t1 = threading.Thread(target=Vilib.camera_clone)  #Thread是一个类，实例化产生t1对象，这里就是创建了一个线程对象t1
        # t1.start() #线程执行
        # print('yes')
    
    @staticmethod
    def human_detect_switch(flag=False):
        Vilib.detect_obj_parameter['hdf_flag'] = flag

    @staticmethod
    def color_detect_switch(flag=False):
        Vilib.detect_obj_parameter['cdf_flag']  = flag

    @staticmethod
    def camera_clone():
        Vilib.camera()     

    @staticmethod
    def camera():
        # from PIL import Image
        # rm = RGB_Matrix(0X74)  #RGB
        # k_img = []   
        camera = cv2.VideoCapture(Vilib.video_source)

        camera.set(3,320)
        camera.set(4,240)
 
        width = int(camera.get(3))
        height = int(camera.get(4))
 
        M = cv2.getRotationMatrix2D((width / 2, height / 2), 180, 1)
        camera.set(cv2.CAP_PROP_BUFFERSIZE,1)
        cv2.setUseOptimized(True)

        # pj_img = cv2.imread("javars.png") 
        # pj_img = cv2.resize(pj_img, (320, 240), interpolation=cv2.INTER_LINEAR)
        
        # print(Vilib.front_view_img.shape)
        # front_view_coor_1 = ()
        # front_view_coor_2 = ()
        while True:
            _, img = camera.read()
            # if not _:
        # 如果图片没有读取成功
                # print("图像获取失败，请按照说明进行问题排查")
            # img = cv2.warpAffine(img, M, (320, 240))
            # Vilib.front_view_img =img.copy()
            
            # img = cv2.resize(img, (8,8), interpolation=cv2.INTER_LINEAR) 
            # img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)
            # img = cv2.warpAffine(img, M, (320, 240))
            # Vilib.img_array[0] = Vilib.human_detect_func(img)
            Vilib.img_array[0] = Vilib.color_detect_func(Vilib.human_detect_func(img)) 
            # Vilib.frame = cv2.imencode('.jpg', Vilib.img_array[0])[1].tobytes()
            # Vilib.img_array[0] = img
         #jar
        #     img = Vilib.color_detect_func(img)
        #     # print(Vilib.color_detect_func(img).shape)
        #     front_view_coor_1 = (Vilib.detect_obj_parameter['color_x'], Vilib.detect_obj_parameter['color_y'])
        #     front_view_coor_2 = (Vilib.detect_obj_parameter['color_x']+40, Vilib.detect_obj_parameter['color_y']+40)
        #     cv2.rectangle(Vilib.front_view_img, front_view_coor_1, front_view_coor_2, (255, 144, 30), -1)
        #     cv2.rectangle(Vilib.front_view_img, (0,0), (320,20), (46,139,87), -1)
        #     cv2.putText(Vilib.front_view_img,"temp: "+str(cpu_temperature()),(0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)
        #     cv2.putText(Vilib.front_view_img,'hello world!',(160,160), cv2.FONT_HERSHEY_SIMPLEX, 1.5,(255,255,255),2, cv2.LINE_AA)
        #    # cv2.line(Vilib.front_view_img, (Vilib.detect_obj_parameter['color_x'], Vilib.detect_obj_parameter['color_y']), (120, 200), (255, 144, 30), 5)
        #     Vilib.img_array[0] = cv2.addWeighted(img, 0.5, Vilib.front_view_img, 0.5, 0)
          #RGB
            # cv2.rectangle(Vilib.front_view_img, (0, 0), (320, 240), (255, 144, 30), 40)
            # k_img = list(Image.fromarray(cv2.cvtColor(Vilib.img_array[0],cv2.COLOR_BGR2RGB)).getdata())#opencv转PIL
            # rm.image(k_img)

            # Vilib.img_array[0] = Vilib.color_detect_func(img)


            # if w == True:
            #     q.send(Vilib.vi_img)


    @staticmethod
    def human_detect_func(img):
        if Vilib.detect_obj_parameter['hdf_flag'] == True:
            resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)            # 2.从BGR转换到RAY
            gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY) 
            faces = Vilib.face_cascade.detectMultiScale(gray, 1.3, 2)
            # print(len(faces))
            Vilib.detect_obj_parameter['human_n'] = len(faces)
            max_area = 0
            if Vilib.detect_obj_parameter['human_n'] > 0:
                for (x,y,w,h) in faces:
                    x = x*2
                    y = y*2
                    w = w*2
                    h = h*2
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    object_area = w*h
                    if object_area > max_area: 
                        object_area = max_area
                        Vilib.detect_obj_parameter['human_x'] = int(x + w/2)
                        Vilib.detect_obj_parameter['human_y'] = int(y + h/2)
                        Vilib.detect_obj_parameter['human_w'] = w
                        Vilib.detect_obj_parameter['human_h'] = h
            
            else:
                Vilib.detect_obj_parameter['human_x'] = 160
                Vilib.detect_obj_parameter['human_y'] = 120
                Vilib.detect_obj_parameter['human_w'] = 0
                Vilib.detect_obj_parameter['human_h'] = 0
                Vilib.detect_obj_parameter['human_n'] = 0
            return img
        else:
            return img

    @staticmethod
    def color_detect_func(img):

        # 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度
        if Vilib.detect_obj_parameter['cdf_flag']  == True:
            # print('color open')
            resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)
            hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
            # print(Vilib.lower_color)
            mask = cv2.inRange(hsv, Vilib.detect_obj_parameter['lower_color'],  Vilib.detect_obj_parameter['upper_color'])           # 3.inRange()：介于lower/upper之间的为白色，其余黑色
            if Vilib.detect_obj_parameter['color_default'] == 'red':
                 mask_2 = cv2.inRange(hsv, (175,50,20), (180,255,255))
                 mask = cv2.bitwise_or(mask, mask_2)

            open_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN,Vilib.kernel_5,iterations=1)              #开运算  

            contours, hierarchy = cv2.findContours(open_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          ####在binary中发现轮廓，轮廓按照面积从小到大排列
                # p=0
            Vilib.detect_obj_parameter['color_n'] = len(contours)
            max_area = 0

            if Vilib.detect_obj_parameter['color_n'] > 0: 
                for i in contours:    #遍历所有的轮廓
                    x,y,w,h = cv2.boundingRect(i)      #将轮廓分解为识别对象的左上角坐标和宽、高

                        #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
                    if w > 8 and h > 8: 
                        x = x*2
                        y = y*2
                        w = w*2
                        h = h*2
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                                #给识别对象写上标号
                        cv2.putText(img,Vilib.detect_obj_parameter['color_default'],(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)#加减10是调整字符位置
 
                        object_area = w*h
                        if object_area > max_area: 
                            object_area = max_area
                            Vilib.detect_obj_parameter['color_x'] = int(x + w/2)
                            Vilib.detect_obj_parameter['color_y'] = int(y + h/2)
                            Vilib.detect_obj_parameter['color_w'] = w
                            Vilib.detect_obj_parameter['color_h'] = h
                            # print()
            else:
                Vilib.detect_obj_parameter['color_x'] = 160
                Vilib.detect_obj_parameter['color_y'] = 120
                Vilib.detect_obj_parameter['color_w'] = 0
                Vilib.detect_obj_parameter['color_h'] = 0
                Vilib.detect_obj_parameter['color_n'] = 0
            return img
        else:
            return img
