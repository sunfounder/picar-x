import numpy as np
import cv2
import threading

from importlib import import_module
import os
from flask import Flask, render_template, Response
from multiprocessing import Process, Manager
import time
import tflite_runtime.interpreter as tflite
from pyzbar import pyzbar
import datetime

from picamera.array import PiRGBArray
from picamera import PiCamera
from PIL import Image, ImageDraw, ImageFont
import threading
from utils import run_command

# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.read("/home/pi/face_recognizer.yml")
# master_name = ["","chentao","zhangguoliang"]

traffic_num_list = [i for i in range(4)]
ges_num_list = [i for i in range(3)]
# ges_list = [chr(i) for i in range(97,101)]
# ges_list.remove('j')

traffic_list = ['stop','right','left','forward']
gesture_list = ["paper","scissor","rock"]
# rock, scissor, paper

traffic_dict = dict(zip(traffic_num_list,traffic_list))
ges_dict = dict(zip(ges_num_list,gesture_list))


# test_image_dir = './ges_pic/'
# traffic_sign_model_path = "/home/pi/sport_camera/example/tf_150_dr0.2.tflite"
# gesture_model_path = "/home/pi/sport_camera/example/3bak_ges_200_dr0.2.tflite"

traffic_sign_model_path = "/home/pi/sport_camera/picarx_python_example/tf_150_dr0.2.tflite"
gesture_model_path = "/home/pi/sport_camera/picarx_python_example/3bak_ges_200_dr0.2.tflite"
# gesture_model_path = "/home/pi/sport_camera/example/mb1_gesture_200_dr0.2.tflite"



interpreter_1 = tflite.Interpreter(model_path=traffic_sign_model_path)
interpreter_1.allocate_tensors()

interpreter_2 = tflite.Interpreter(model_path=gesture_model_path)
interpreter_2.allocate_tensors()

# Get input and output tensors.
input_details_1 = interpreter_1.get_input_details()
# print(str(input_details_1))
output_details_1 = interpreter_1.get_output_details()
# print(str(output_details_1))


# Get input and output tensors.
input_details_2 = interpreter_2.get_input_details()
# print(str(input_details_2))
output_details_2 = interpreter_2.get_output_details()
# print(str(output_details_2))


app = Flask(__name__)
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def get_frame():
    return cv2.imencode('.jpg', Vilib.img_array[0])[1].tobytes()


def get_qrcode_pictrue():
    return cv2.imencode('.jpg', Vilib.img_array[1])[1].tobytes()

def get_png_frame():
    return cv2.imencode('.png', Vilib.img_array[0])[1].tobytes()

def gen():
    """Video streaming generator function."""
    while True:  
        # start_time = time.time()
        # frame = cv2.imread("123.jpeg")Vilib.q.get()  
        # print("1")
        # if Vilib.conn2.recv()
        # frame = cv2.imencode('.jpg', Vilib.conn2.recv())[1].tobytes() 
        # rt_img = np.ones((320,240),np.uint8)
        # print("2")
        frame = get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.03)
        # end_time = time.time() - start_time
        # print(int(1/end_time))

@app.route('/mjpg')   ## video
def video_feed():
    # from camera import Camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    response = Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame') 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/mjpg.jpg')  ##picture
def video_feed_jpg():
    # from camera import Camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    # path = "/home/pi/sport_camera/example/cali.jpg"
    response = Response(get_frame(), mimetype="image/jpeg")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/mjpg.png')  ##picture
def video_feed_png():
    # from camera import Camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    # path = "/home/pi/sport_camera/example/cali.jpg"
    response = Response(get_png_frame(), mimetype="image/png")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# @app.route('/mjpg.jpg')  ##picture
# def video_feed_jpg():
    # from camera import Camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    # path = "/home/pi/sport_camera/example/cali.jpg"
    # return Response(get_qrcode_pictrue(), mimetype="image/jpeg") 
# @app.route('/mjpg.jpg', methods=['post', 'get'])
# def video_feed_jpg():
#     path = request.args.get('path')
#     print(path)
#     path = "/home/pi/http.jpg/%s" % path

#     resp = Response(open(path, 'rb'), mimetype="image/jpeg")
#     return resp


def web_camera_start():
    app.run(host='0.0.0.0', port=9000,threaded=True)

EFFECTS = [ 
    "none",
    "negative",#
    "solarize",#
    # "sketch",
    # "denoise",
    "emboss",#
    # "oilpaint",
    # "hatch",
    # "gpen",
    # "pastel",
    # "watercolor",
    # "film",
    # "blur",
    # "saturation",
    # "colorswap",
    # "washedout",
    "posterise",#
    # "colorpoint",
    # "colorbalance",
    "cartoon",#
    # "deinterlace1",
    # "deinterlace2",
]

Camera_SETTING = [
        "resolution",    #max(4056,3040)
        #"framerate 
        "rotation",      #(0 90 180 270)
        # "shutter_speed",
        "brightness",    # 0~100  default 50
        "sharpness",    # -100~100  default 0
        "contrast",    # -100~100  default 0
        "saturation",    # -100~100  default 0
        "iso",           #Vaild value:0(auto) 100,200,320,400,500,640,800
        "exposure_compensation",       # -25~25  default 0
        "exposure_mode",       #Valid values are: 'off', 'auto' (default),'night', 'nightpreview', 'backlight', 'spotlight', 'sports', 'snow', 'beach','verylong', 'fixedfps', 'antishake', or 'fireworks'
        "meter_mode",     #Valid values are: 'average' (default),'spot', 'backlit', 'matrix'.
        "awb_mode",       #'off', 'auto' (default), ‘sunlight', 'cloudy', 'shade', 'tungsten', 'fluorescent','incandescent', 'flash', or 'horizon'.
        "hflip",          # Default:False ,True
        "vflip",          # Default:False ,True
        # "crop",           #Retrieves or sets the zoom applied to the camera’s input, as a tuple (x, y, w, h) of floating point
                          #values ranging from 0.0 to 1.0, indicating the proportion of the image to include in the output
                          #(the ‘region of interest’). The default value is (0.0, 0.0, 1.0, 1.0), which indicates that everything
                          #should be included.
]

time_font = lambda x: ImageFont.truetype('/home/pi/sport_camera/picarx_python_example/Roboto-Light-2.ttf', int(x / 320.0 * 6))
text_font = lambda x: ImageFont.truetype('/home/pi/sport_camera/picarx_python_example/Roboto-Light-2.ttf', int(x / 320.0 * 10))
company_font = lambda x: ImageFont.truetype('/home/pi/sport_camera/picarx_python_example/Roboto-Light-2.ttf', int(x / 320.0 * 8))


def add_text_to_image(name, text_1):
    # rgba_image = image.convert('RGB')
    # text_overlay = Image.new('RGB', rgba_image.size, (255, 255, 255))
    image_target = Image.open(name)

    image_draw = ImageDraw.Draw(image_target)

    
    time_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time_size_x, time_size_y = image_draw.textsize(time_text, font=time_font(image_target.size[0]))
    text_size_x, text_size_y = image_draw.textsize(text_1, font=text_font(image_target.size[0]))

  # 设置文本文字位置
    # print(rgba_image)
    time_xy = (image_target.size[0] - time_size_x - time_size_y, image_target.size[1] - int(1.5*time_size_y))
    text_xy = (text_size_y, image_target.size[1] - int(1.5*text_size_y))
    company_xy = (text_size_y, image_target.size[1] - int(1.5*text_size_y) - text_size_y)

  # 设置文本颜色和透明度
    image_draw.text(time_xy, time_text, font=time_font(image_target.size[0]), fill=(255, 255, 255))
    image_draw.text(company_xy, text_1, font=text_font(image_target.size[0]), fill=(255, 255, 255))
    # image_draw.text(text_xy, text_2, font=company_font(image_target.size[0]), fill=(255, 255, 255))
    # run_command("sudo rm " + str(name))
    image_target.save(name,quality=95,subsampling=0)# 


class Vilib(object): 

    video_flag = False
    # video_path = './video_file/tst.avi'

    # picture_path = './picture_file'
    # video_recorder = cv2.VideoWriter(video_path, fourcc, 20.0, (320, 240))

    face_cascade = cv2.CascadeClassifier('/home/pi/sport_camera/picarx_python_example/haarcascade_frontalface_default.xml') 
    kernel_5 = np.ones((5,5),np.uint8)#4x4的卷积核
    # color_default = 'blue'
    # color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[166,180]}
    # lower_color = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60])  
    # upper_color = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])
    # hdf_flag = False 
    # cdf_flag = False
    # stf_flag = False
    video_source = 0
    roi = cv2.imread("/home/pi/sport_camera/picarx_python_example/cali.jpg")
    roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # obj_roi = cv2.imread("/home/pi/sport_camera/example/object.jpg")
    # h,w = obj_roi.shape[:2]

    # obj_hsv = cv2.cvtColor(obj_roi, cv2.COLOR_BGR2HSV)

    # track_window = (0, 0, w, h)

    # roi_hist = cv2.calcHist([obj_hsv],[0,1],None,[180,256],[0,180,0,256]) #计算直方图
    # cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

    
    # human_object_counter = 0
    # detect_obj_parameter = np.array([0,0])
    # human_object_size = np.array([0,0]) 

    # color_object_counter = 0
    detect_obj_parameter = Manager().dict()
    img_array = Manager().list(range(2))
#Color_obj_parameter
    detect_obj_parameter['color_default'] = 'red'

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}
    # lower_color = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60])  
    # upper_color = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])

    detect_obj_parameter['color_x'] = 320
    detect_obj_parameter['color_y'] = 240
    detect_obj_parameter['color_w'] = 0
    detect_obj_parameter['color_h'] = 0
    detect_obj_parameter['color_n'] = 0
    detect_obj_parameter['lower_color'] = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60]) 
    detect_obj_parameter['upper_color'] = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])
    

#Human_obj_parameter
    detect_obj_parameter['human_x'] = 320
    detect_obj_parameter['human_y'] = 240
    detect_obj_parameter['human_w'] = 0
    detect_obj_parameter['human_h'] = 0
    detect_obj_parameter['human_n'] = 0

#traffic_sign_obj_parameter
    detect_obj_parameter['traffic_sign_x'] = 320
    detect_obj_parameter['traffic_sign_y'] = 240
    detect_obj_parameter['traffic_sign_w'] = 0
    detect_obj_parameter['traffic_sign_h'] = 0
    detect_obj_parameter['traffic_sign_t'] = 'None'
    detect_obj_parameter['traffic_sign_acc'] = 0

#gesture_obj_parameter
    detect_obj_parameter['gesture_x'] = 320
    detect_obj_parameter['gesture_y'] = 240
    detect_obj_parameter['gesture_w'] = 0
    detect_obj_parameter['gesture_h'] = 0
    detect_obj_parameter['gesture_t'] = 'None'
    detect_obj_parameter['gesture_acc'] = 0
    # detect_obj_parameter['human_n'] = 0


#detect_switch
    detect_obj_parameter['hdf_flag'] = False
    detect_obj_parameter['cdf_flag'] = False
    detect_obj_parameter['ts_flag'] = False
    detect_obj_parameter['gs_flag'] = False
    detect_obj_parameter['calibrate_flag'] = False   
    detect_obj_parameter['object_follow_flag'] = False
    detect_obj_parameter['qr_flag'] = False

#QR_code
    detect_obj_parameter['qr_data'] = "None"
    detect_obj_parameter['qr_x'] = 320
    detect_obj_parameter['qr_y'] = 240
    detect_obj_parameter['qr_w'] = 0
    detect_obj_parameter['qr_h'] = 0
#video
    # detect_obj_parameter['vi_fps'] = 20
    # detect_obj_parameter['video_flag'] = False
    # detect_obj_parameter['video_path'] = './video_file/1.avi'

    # detect_obj_parameter['new_video'] = False
    # detect_obj_parameter['process_video'] = True

#picture
    detect_obj_parameter['picture_flag'] = False
    detect_obj_parameter['process_picture'] = True
    detect_obj_parameter['picture_path'] = '/home/pi/picture_file/' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ '.jpg'
    # detect_obj_parameter['color_default'] = 'red'

    # color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[166,180]}
    # lower_color = np.array([min(color_dict[detect_obj_parameter['color_default']]), 60, 60])  
    # upper_color = np.array([max(color_dict[detect_obj_parameter['color_default']]), 255, 255])
    detect_obj_parameter['video_flag'] = None

    detect_obj_parameter['ensure_flag'] = False
    detect_obj_parameter['clarity_val'] = 0

#diy
    detect_obj_parameter['human_n'] = 0
    # detect_obj_parameter['hdf_flag'] = False

#picture
    detect_obj_parameter['eff'] = 0
    detect_obj_parameter['setting'] = 0
    detect_obj_parameter['setting_flag'] = False
    detect_obj_parameter['setting_val'] = 0
    # detect_obj_parameter['current_setting_val'] = None
    detect_obj_parameter['setting_resolution'] = (3840,2880)
    detect_obj_parameter['change_setting_flag'] = False
    detect_obj_parameter['change_setting_type'] = 'None'
    detect_obj_parameter['change_setting_val'] = 0

    detect_obj_parameter['photo_button_flag'] = False
    detect_obj_parameter['content_length'] = 0
    detect_obj_parameter['content_num'] = 0
    detect_obj_parameter['process_content_1'] = []
    detect_obj_parameter['process_si'] = []
    # detect_obj_parameter['process_dict'] = {}

    detect_obj_parameter['watermark_flag'] = True
    detect_obj_parameter['camera_flip'] = False
    detect_obj_parameter['watermark'] = "Shot by Picar-x"
    # detect_obj_parameter['google_upload_flag'] = False

    rt_img = np.ones((320,240),np.uint8)
    front_view_img = np.zeros((240,320,3), np.uint8)
# 使用白色填充图片区域,默认为黑色
    # front_view_img.fill(255)       
    img_array[0] = rt_img
    img_array[1] = rt_img
    # img_array = rt_img
    vi_img = np.ones((320,240),np.uint8)  


    # @staticmethod
    # def clarity_val():
    #     return Vilib.detect_obj_parameter['clarity_val']


    # @staticmethod
    # def camera_start():
        # from multiprocessing import Process
        
        
        # worker_2 = Process(name='worker 2',target=Ras_Cam.camera_clone)
        # worker_1 = Process(name='worker 1',target=dis)
        # worker_3 = Process(name='worker 3',target=web_camera_start)
        # worker_1.start()
        # worker_2.start()
        # worker_3.start()

    # @staticmethod
    # def gamma_method(img):
    #     (b, g, r) = cv2.split(img)
    #     b_mean = np.mean(b)
    #     g_mean = np.mean(g)
    #     r_mean = np.mean(r)
        
    #     b_gamma_val = math.log10(0.5)/math.log10(b_mean/255)
    #     g_gamma_val = math.log10(0.5)/math.log10(g_mean/255)
    #     r_gamma_val = math.log10(0.5)/math.log10(r_mean/255)

    #     b_gamma_table = [np.power(x / 255.0, b_gamma_val) * 255.0 for x in range(256)]  # 建立映射表
    #     g_gamma_table = [np.power(x / 255.0, g_gamma_val) * 255.0 for x in range(256)]  # 建立映射表
    #     r_gamma_table = [np.power(x / 255.0, r_gamma_val) * 255.0 for x in range(256)]  # 建立映射表

    #     b_gamma_table = np.round(np.array(b_gamma_table)).astype(np.uint8)  # 颜色值为整数
    #     g_gamma_table = np.round(np.array(g_gamma_table)).astype(np.uint8)  # 颜色值为整数
    #     r_gamma_table = np.round(np.array(r_gamma_table)).astype(np.uint8)  # 颜色值为整数

    #     bh = cv2.LUT(b, b_gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。   
    #     gh = cv2.LUT(g, g_gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。   
    #     rh = cv2.LUT(r, r_gamma_table)  # 图片颜色查表。另外可以根据光强（颜色）均匀化原则设计自适应算法。   


    #     # cv2.normalize(b,b, 0, 255, cv2.NORM_MINMAX)
    #     # cv2.normalize(g,g, 0, 255, cv2.NORM_MINMAX)
    #     # cv2.normalize(r,r, 0, 255, cv2.NORM_MINMAX)
    #     # #归一化
    #     # bh= cv2.convertScaleAbs(b)
    #     # gh= cv2.convertScaleAbs(g)
    #     # rh= cv2.convertScaleAbs(r)
    #     # #将格式从uint16转为uint8

    #     # fgamma = 120.0
    #     # img_gamma = np.power((bh/255.0),1/fgamma)*255.0
    #     # img_gamma = np.power((gh/255.0),1/fgamma)*255.0
    #     # img_gamma = np.power((rh/255.0),1/fgamma)*255.0

    #     img = cv2.merge((bh, gh, rh))
        
    #     return img

    @staticmethod
    def photo_effect(shirt_way = 'Shift_left'):
        print(shirt_way)
        shirt_way = str(shirt_way)
        if shirt_way == 'Shift_left':
            Vilib.detect_obj_parameter['eff'] += 1
            if Vilib.detect_obj_parameter['eff'] >= len(EFFECTS):
                Vilib.detect_obj_parameter['eff'] = 0
        elif shirt_way == 'Shift_right':
            Vilib.detect_obj_parameter['eff'] -= 1
            if Vilib.detect_obj_parameter['eff'] < 0:
                Vilib.detect_obj_parameter['eff'] = len(EFFECTS) - 1
        else:
            raise Exception("parameter error!")


    # @staticmethod
    # def change_show_setting(shirt_way = 'None'):
    #     global button_motion
    #     if shirt_way == 'Shift_left':
    #         Vilib.detect_obj_parameter['setting'] += 1
    #         if Vilib.detect_obj_parameter['setting'] >= len(Camera_SETTING):
    #             Vilib.detect_obj_parameter['setting'] = 0

    #     elif shirt_way == 'Shift_right':
    #         Vilib.detect_obj_parameter['setting'] -= 1
    #         if Vilib.detect_obj_parameter['setting'] < 0:
    #             Vilib.detect_obj_parameter['setting'] = len(Camera_SETTING) - 1

    #     elif shirt_way == 'None':
    #         pass

    #     else:
    #         raise Exception("parameter error!")


    #     # print(Camera_SETTING[Ras_Cam.detect_obj_parameter['setting']])
    #     if type(Vilib.detect_obj_parameter['setting_val']) == str:
    #         Vilib.detect_obj_parameter['setting_val'] = "'" + Vilib.detect_obj_parameter['setting_val'] + "'"
    #     return Camera_SETTING[Vilib.detect_obj_parameter['setting']], Vilib.detect_obj_parameter['setting_val']



    # @staticmethod
    # def google_upload(flag):
    #     # global button_motion
    #     Ras_Cam.detect_obj_parameter['google_upload_flag'] = flag

    @staticmethod
    def video_flag(flag):
        # global button_motion
        Vilib.detect_obj_parameter['video_flag'] = flag

    # @staticmethod
    # def show_content(id_num,content,content_coordinate,content_color,font_size):

    #     cmd_test = "Vilib.detect_obj_parameter['process_content_" + str(id_num) + "'" + "] = [" + "'" + str(content) + "'" + "," + str(content_coordinate)+","+str(content_color)+","+str(font_size)+"]"
    #     exec(cmd_test)
    #     if id_num > Vilib.detect_obj_parameter['content_num']:
    #         Vilib.detect_obj_parameter['content_num'] = id_num

    @staticmethod
    def watermark(watermark = "Shot by Picar-x"):
        # global button_motion
        watermark = str(watermark)
        Vilib.detect_obj_parameter['watermark_flag'] = True
        Vilib.detect_obj_parameter['watermark'] = watermark

    @staticmethod
    def show_setting(flag):
        # global button_motion

        Vilib.detect_obj_parameter['setting_flag'] = flag
        # button_motion = 'free'

    @staticmethod
    def change_setting_type_val(setting_type,setting_val):
        # global button_motion
        if setting_type == 'resolution':
            Vilib.detect_obj_parameter['setting_resolution'] = setting_val
        else:
            Vilib.detect_obj_parameter['change_setting_type'] = setting_type
            Vilib.detect_obj_parameter['change_setting_val'] = setting_val
            Vilib.detect_obj_parameter['change_setting_flag'] = True


    @staticmethod
    def shuttle_button():
        # global button_motion
        Vilib.detect_obj_parameter['photo_button_flag']  = True
        # button_motion = 'free'
        

    @staticmethod
    def make_qrcode_picture(data):
        # data = 'hello'
        # 生成二维码
        Vilib.img_array = qrcode.make(data=data)


    @staticmethod
    def color_detect_object(obj_parameter):
        if obj_parameter == 'x':
            # print(Vilib.detect_obj_parameter['x'])          
            return int(Vilib.detect_obj_parameter['color_x']/214.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['color_y']/160.2)-1) #max_size_object_coordinate_y
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
            return int(Vilib.detect_obj_parameter['human_x']/214.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['human_y']/160.2)-1) #max_size_object_coordinate_y
        elif obj_parameter == 'width':
            return Vilib.detect_obj_parameter['human_w']   #objects_max_width
        elif obj_parameter == 'height':
            return Vilib.detect_obj_parameter['human_h']   #objects_max_height
        elif obj_parameter == 'number':      
            return Vilib.detect_obj_parameter['human_n']   #objects_count
        return None

    @staticmethod
    def traffic_sign_detect_object(obj_parameter):
        if obj_parameter == 'x':
            # print(Vilib.detect_obj_parameter['x'])          
            return int(Vilib.detect_obj_parameter['traffic_sign_x']/214.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['traffic_sign_y']/160.2)-1) #max_size_object_coordinate_y
        elif obj_parameter == 'width':
            return Vilib.detect_obj_parameter['traffic_sign_w']   #objects_max_width
        elif obj_parameter == 'height':
            return Vilib.detect_obj_parameter['traffic_sign_h']   #objects_max_height
        # elif obj_parameter == 'number':      
        #     return Vilib.detect_obj_parameter['traffic_sign_n']   #objects_count
        elif obj_parameter == 'type':      
            return Vilib.detect_obj_parameter['traffic_sign_t']   #objects_type
        elif obj_parameter == 'accuracy':      
            return Vilib.detect_obj_parameter['traffic_sign_acc']   #objects_type
        return 'none'

    @staticmethod
    def gesture_detect_object(obj_parameter):
        if obj_parameter == 'x':
            # print(Vilib.detect_obj_parameter['x'])          
            return int(Vilib.detect_obj_parameter['gesture_x']/214.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['gesture_y']/160.2)-1) #max_size_object_coordinate_y
        elif obj_parameter == 'width':
            return Vilib.detect_obj_parameter['gesture_w']   #objects_max_width
        elif obj_parameter == 'height':
            return Vilib.detect_obj_parameter['gesture_h']   #objects_max_height
        elif obj_parameter == 'type':      
            return Vilib.detect_obj_parameter['gesture_t']   #objects_type
        elif obj_parameter == 'accuracy':      
            return Vilib.detect_obj_parameter['gesture_acc']   #objects_type
        return 'none'

    @staticmethod
    def qrcode_detect_object(obj_parameter = 'data'):
        if obj_parameter == 'x':
            # print(Vilib.detect_obj_parameter['x'])          
            return int(Vilib.detect_obj_parameter['qr_x']/214.0)-1
        elif obj_parameter == 'y':
            # print(Vilib.detect_obj_parameter['y']) 
            return -1*(int(Vilib.detect_obj_parameter['qr_y']/160.2)-1) #max_size_object_coordinate_y
        elif obj_parameter == 'width':
            return Vilib.detect_obj_parameter['qr_w']   #objects_max_width
        elif obj_parameter == 'height':
            return Vilib.detect_obj_parameter['qr_h']   #objects_max_height
        elif obj_parameter == 'data':      
            return Vilib.detect_obj_parameter['qr_data']   #objects_count
        return 'none'
        # return Vilib.detect_obj_parameter['qr_data']

    @staticmethod
    def detect_color_name(color_name):
        Vilib.detect_obj_parameter['color_default'] = color_name
        Vilib.detect_obj_parameter['lower_color'] = np.array([min(Vilib.color_dict[Vilib.detect_obj_parameter['color_default']]), 60, 60])  
        Vilib.detect_obj_parameter['upper_color'] = np.array([max(Vilib.color_dict[Vilib.detect_obj_parameter['color_default']]), 255, 255])
        Vilib.detect_obj_parameter['cdf_flag']  = True
        # Vilib.detect_obj_parameter['color_x'] = 160
        # Vilib.detect_obj_parameter['color_y'] = 120
        # Vilib.detect_obj_parameter['color_w'] = 0
        # Vilib.detect_obj_parameter['color_h'] = 0
        # Vilib.detect_obj_parameter['color_n'] = 0



    @staticmethod
    def camera_start(web_func = True,inverted_flag = False):
        # from multiprocessing import Process

        if inverted_flag == True:
            Vilib.detect_obj_parameter['camera_flip'] = True
        else:
            Vilib.detect_obj_parameter['camera_flip'] = False

        worker_2 = threading.Thread(target=Vilib.camera_clone, name="Thread1")
        # worker_2.setDaemon(True)
        if web_func == True: 
            worker_1 = threading.Thread(name='worker 1',target=web_camera_start)
            # worker_1.setDaemon(True)
            worker_1.start()
            # print("worker_1:",worker_1.pid)
        worker_2.start()
        # # print("worker_2:",worker_2.pid)


        # if inverted_flag == True:
        #     Vilib.detect_obj_parameter['camera_flip'] = True
        # else:
        #     Vilib.detect_obj_parameter['camera_flip'] = False

        # worker_2 = Process(target=Vilib.camera_clone, name="Thread1")
        # worker_2.daemon = True
        # if web_func == True: 
        #     worker_1 = Process(name='worker 1',target=web_camera_start)
        #     worker_1.daemon = True
        #     worker_1.start()
        #     print("worker_1:",worker_1.pid)
        # worker_2.start()
        # print("worker_2:",worker_2.pid)
        # timer.start()
        
        # worker_2 = Process(name='worker 2',target=Vilib.camera_clone)
        # if web_func == True:
        #     worker_1 = Process(name='worker 1',target=web_camera_start)
        #     worker_1.start()
        # worker_2.start()
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
    def gesture_detect_switch(flag=False):
        Vilib.detect_obj_parameter['gs_flag']  = flag

    @staticmethod
    def traffic_sign_detect_switch(flag=False):
        Vilib.detect_obj_parameter['ts_flag']  = flag

    @staticmethod
    def gesture_calibrate_switch(flag=False):
        Vilib.detect_obj_parameter['calibrate_flag']  = flag

    @staticmethod
    def object_follow_switch(flag=False):
        Vilib.detect_obj_parameter['object_follow_flag'] = flag

    @staticmethod
    def qrcode_detect_switch(flag=False):
        Vilib.detect_obj_parameter['qr_flag']  = flag

    
    @staticmethod
    def camera_clone():
        Vilib.camera()     

    @staticmethod
    def camera():
        global effect
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.image_effect = EFFECTS[Vilib.detect_obj_parameter['eff']]
        camera.framerate = 24
        camera.rotation = 0
        # camera.rotation = 180   
        camera.brightness = 50    #(0 to 100)
        camera.sharpness = 0      #(-100 to 100)
        camera.contrast = 0       #(-100 to 100)
        camera.saturation = 0     #(-100 to 100)
        camera.iso = 0            #(automatic)(100 to 800)
        camera.exposure_compensation = 0   #(-25 to 25)
        camera.exposure_mode = 'auto'
        camera.meter_mode = 'average'
        camera.awb_mode = 'auto'
        camera.hflip = False
        camera.vflip = Vilib.detect_obj_parameter['camera_flip']
        camera.crop = (0.0, 0.0, 1.0, 1.0)
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        last_e ='none'
        camera_val = 0
        last_show_content_list = []
        show_content_list = []
        change_type_val  = []
        change_type_dict = {"shutter_speed":0,"resolution":[2592,1944], "brightness":50, "contrast":0, "sharpness":0, "saturation":0, "iso":0, "exposure_compensation":0, "exposure_mode":'auto', \
            "meter_mode":'average' ,"rotation":0 ,"awb_mode":'auto',"drc_strength":'off',"hflip":False,"vflip":True}
        start_time = 0
        end_time = 0
        # camera.framerate = 10
        # 
        try:
            while True:


                for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
                    
                    start_time = time.time()
                    img = frame.array
                    # img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    # Vilib.detect_obj_parameter['clarity_val'] = round(cv2.Laplacian(img2gray, cv2.CV_64F).var(),2)
                    # img = Vilib.human_detect_func(img)
                    # img = Vilib.gamma_method(img)
                    img = Vilib.gesture_calibrate(img)
                    img = Vilib.traffic_detect(img)
                    img = Vilib.color_detect_func(img)
                    img = Vilib.human_detect_func(img)
                    img = Vilib.gesture_recognition(img)
                    img = Vilib.qrcode_detect_func(img)
                    # cv2.rectangle(img, (280,10), (310,20), (255,255,255))
                    # cv2.rectangle(img, (310,13), (311,17), (255,255,255))
                    # cv2.rectangle(img, (282,12), (int((1-round(4.3 - power_val(),3)) / 1 * 26 + 282),18), (0,255,0),thickness=-1)
                    
                    # change_camera_setting
                    if Vilib.detect_obj_parameter['change_setting_flag'] == True:
                        Vilib.detect_obj_parameter['change_setting_flag'] = False

                        change_setting_cmd = "camera." + Vilib.detect_obj_parameter['change_setting_type'] + '=' + str(Vilib.detect_obj_parameter['change_setting_val'])
                        print(change_setting_cmd)
                        exec(change_setting_cmd)
                        # change_type_dict[Vilib.detect_obj_parameter['change_setting_type']] = Vilib.detect_obj_parameter['change_setting_val']
                        # change_type_val.append(change_setting_cmd)
                        change_type_dict[Vilib.detect_obj_parameter['change_setting_type']] = Vilib.detect_obj_parameter['change_setting_val']
                    if Vilib.detect_obj_parameter['content_num'] != 0:

                        for i in range(Vilib.detect_obj_parameter['content_num']):
                            exec("Vilib.detect_obj_parameter['process_si'] = Vilib.detect_obj_parameter['process_content_" + str(i+1) + "'" + "]")
                            cv2.putText(img, str(Vilib.detect_obj_parameter['process_si'][0]),Vilib.detect_obj_parameter['process_si'][1],cv2.FONT_HERSHEY_SIMPLEX,Vilib.detect_obj_parameter['process_si'][3],Vilib.detect_obj_parameter['process_si'][2],2)
                    
                    if Vilib.detect_obj_parameter['setting_flag'] == True:
                        setting_type = Camera_SETTING[Vilib.detect_obj_parameter['setting']]
                        if setting_type == "resolution":
                            Vilib.detect_obj_parameter['setting_val'] = Vilib.detect_obj_parameter['setting_resolution']
                            # print(Vilib.detect_obj_parameter['change_setting_type'])
                            # print(list(Vilib.detect_obj_parameter['setting_resolution']))
                            change_type_dict["resolution"] = list(Vilib.detect_obj_parameter['setting_resolution'])
                            cv2.putText(img, 'resolution:' + str(Vilib.detect_obj_parameter['setting_resolution']),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
                        elif setting_type == "shutter_speed":
                            change_type_dict["shutter_speed"] = Vilib.detect_obj_parameter['change_setting_val']
                            cv2.putText(img, 'shutter_speed:' + str(Vilib.detect_obj_parameter['change_setting_val']),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
                        else:
                            cmd_text = "Vilib.detect_obj_parameter['setting_val'] = camera." + Camera_SETTING[Vilib.detect_obj_parameter['setting']]
                            # print('mennu:',Ras_Cam.detect_obj_parameter['setting_val'])
                            exec(cmd_text)
                            cv2.putText(img, setting_type + ': ' + str(Vilib.detect_obj_parameter['setting_val']),(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)


                    e = EFFECTS[Vilib.detect_obj_parameter['eff']]
                    
                    
                    if last_e != e:
                        camera.image_effect = e
                    last_e = e
                    if last_e != 'none':
                        cv2.putText(img, str(last_e),(0,15),cv2.FONT_HERSHEY_SIMPLEX,0.6,(204,209,72),2)

                        
                    if Vilib.detect_obj_parameter['photo_button_flag'] == True:
                        camera.close()
                        break
                            
    
                    Vilib.img_array[0] = img
                    rawCapture.truncate(0)
                    end_time = time.time()
                    end_time = end_time - start_time
                    # print(int(1/end_time))
                    # print("FPS:",round(time.time() - s_time,2),camera.framerate)


                # camera = PiCamera()


                # imu_x,imu_y = imu_rotate()
                # # print("change_type_val:",change_type_val)
                # for i in change_type_val:
                #     exec(i)
                # if imu_y < 35 and imu_y >-35 and imu_x <= 90 and imu_x > 45:
                #     # if Vilib.detect_obj_parameter['setting_resolution'][0] < 3040:
                #     #     camera.resolution = (Vilib.detect_obj_parameter['setting_resolution'][1],Vilib.detect_obj_parameter['setting_resolution'][0])
                #     # else:
                #     # camera.resolution = (Vilib.detect_obj_parameter['setting_resolution'][1],Vilib.detect_obj_parameter['setting_resolution'][0])
                #     # camera.rotation = 270
                #     change_type_dict['rotation'] = 270
                #     image_width, image_height = change_type_dict['resolution'][1],change_type_dict['resolution'][0]
                # elif imu_y < 35 and imu_y >-35 and imu_x < -45 and imu_x >= -90:
                #     # if Vilib.detect_obj_parameter['setting_resolution'][0] < 3040:
                #     #     camera.resolution = (Vilib.detect_obj_parameter['setting_resolution'][1],Vilib.detect_obj_parameter['setting_resolution'][0])
                #     # else:
                #     # camera.resolution = (Vilib.detect_obj_parameter['setting_resolution'][1],Vilib.detect_obj_parameter['setting_resolution'][0])
                #     # camera.rotation = 90
                #     image_width, image_height  = change_type_dict['resolution'][1],change_type_dict['resolution'][0]
                #     change_type_dict['rotation'] = 90
                # elif imu_y < -65 and imu_y >=-90 and imu_x < 45 and imu_x >= -45:
                #     # camera.resolution = Vilib.detect_obj_parameter['setting_resolution']
                #     # camera.rotation = 180
                #     image_width, image_height = change_type_dict['resolution'][0],change_type_dict['resolution'][1]
                #     change_type_dict['rotation'] = 180
                # else:
                #     image_width, image_height = change_type_dict['resolution'][0],change_type_dict['resolution'][1]
                #     change_type_dict['rotation'] = 0
                #     # camera.resolution = Vilib.detect_obj_parameter['setting_resolution']

                # camera.image_effect = e
                # rawCapture = PiRGBArray(camera, size=camera.resolution) 
                # print("12")
                picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                Vilib.detect_obj_parameter['picture_path'] = '/home/pi/picture_file/' + picture_time + '.jpg'
                # print(Vilib.detect_obj_parameter['picture_path']) 


                # camera.close()
                # print(camera.brightness,camera.sharpness,camera.contrast,camera.saturation,camera.iso,camera.exposure_compensation,camera.exposure_mode,camera.meter_mode,camera.awb_mode,camera.shutter_speed)
                a_t = "sudo raspistill -t 250  -w 2592 -h 1944 -vf" + " -rot " + str(change_type_dict['rotation']) + " -ifx " + str(EFFECTS[Vilib.detect_obj_parameter['eff']]) +" -o " + Vilib.detect_obj_parameter['picture_path']
                

                print(a_t)
                run_command(a_t)
                # camera.capture(Vilib.detect_obj_parameter['picture_path'])
                # cv2.imread()
                if Vilib.detect_obj_parameter['watermark_flag'] == True:
                    add_text_to_image(Vilib.detect_obj_parameter['picture_path'],Vilib.detect_obj_parameter['watermark'])

                # if Vilib.detect_obj_parameter['google_upload_flag'] == True:
                #     upload(file_path='/home/pi/Pictures/rascam_picture_file/', file_name=picture_time + '.jpg')

                #init again
                # camera.close()
                camera = PiCamera()
                camera.resolution = (640,480)
                camera.vflip = Vilib.detect_obj_parameter['camera_flip']
                # camera.rotation = Vilib.detect_obj_parameter['camera_rot']
                camera.image_effect = e
                rawCapture = PiRGBArray(camera, size=camera.resolution) 
                Vilib.detect_obj_parameter['photo_button_flag'] = False
                   
        finally:
            camera.close()



    @staticmethod
    def gesture_calibrate(img):
        if Vilib.detect_obj_parameter['calibrate_flag'] == True:
            # cv2.VideoWriter("./video_file/tt.avi", fourcc, 20.0, (640, 480))
                # roi_hsv = roi_hsv
            cv2.imwrite('/home/pi/sport_camera/picarx_python_example/cali.jpg', img[190:290,270:370])
            # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.rectangle(img,(270,190),(370,290),(255,255,255),2)

        return img



    @staticmethod
    def get_picture(process_picture):
        Vilib.detect_obj_parameter['picture_flag'] = True
        Vilib.detect_obj_parameter['process_picture'] = process_picture
        # if Vilib.detect_obj_parameter['picture_flag'] == True:
        # Vilib.detect_obj_parameter['picture_path'] = '/home/pi/picture_file/' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.jpg'
        Vilib.detect_obj_parameter['picture_path'] = '/home/pi/picture_file/' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '.jpg'
            # cv2.VideoWriter("./video_file/tt.avi", fourcc, 20.0, (640, 480))
            # cv2.imwrite(pic_path, Vilib.img_array[0])

    @staticmethod
    def take_photo(img):
        if img is not None:
        # if Vilib.detect_obj_parameter['picture_flag'] == True:
            # print(Vilib.detect_obj_parameter['picture_path'])
            cv2.imwrite(Vilib.detect_obj_parameter['picture_path'], img)
            Vilib.detect_obj_parameter['picture_flag'] = False


    @staticmethod
    def cnt_area(cnt):
        x,y,w,h = cv2.boundingRect(cnt)
        return w*h



    @staticmethod
    def traffic_predict(input_img,x,y,w,h):
        # new_x = x
        # new_y = y
        # new_w = w
        # new_h = h
        x1 = int(x)
        x2 = int(x + w)
        y1 = int(y)
        y2 = int(y + h)

        # print(x1,x2,y1,y2)
        new_img = input_img[y1:y2,x1:x2]
        # new_img = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
        # cv2.imwrite(str(x)+str(y)+'.jpg',new_img)
        new_img = (new_img / 255.0)
        # img = img / 255.
        new_img = (new_img - 0.5) * 2.0

        resize_img = cv2.resize(new_img, (96,96), interpolation=cv2.INTER_LINEAR)
        flatten_img = np.reshape(resize_img, (96,96,3))
        im5 = np.expand_dims(flatten_img,axis = 0)

    # Perform the actual detection by running the model with the image as input
        image_np_expanded = im5.astype('float32') # 类型也要满足要求

        interpreter_1.set_tensor(input_details_2[0]['index'],image_np_expanded)
        interpreter_1.invoke()
        output_data_2 = interpreter_1.get_tensor(output_details_2[0]['index'])

    #     # 出来的结果去掉没用的维度   np.where(result==np.max(result)))[0][0]
        result = np.squeeze(output_data_2)
        result_accuracy =  round(np.max(result),2)
        ges_class = np.where(result==np.max(result))[0][0]


        return result_accuracy,ges_class


### detection
    @staticmethod
    def gesture_predict(input_img,x,y,w,h):
        # new_x = x
        # new_y = y
        # new_w = w
        # new_h = h
        x1 = int(x)
        x2 = int(x + w)
        y1 = int(y)
        y2 = int(y + h)

        if x1 <= 0:
            x1 = 0
        elif x2 >= 640:
            x2 = 640
        if y1 <= 0:
            y1 = 0
        elif y2 >= 640:
            y2 = 640

        # print(x1,x2,y1,y2)
        new_img = input_img[y1:y2,x1:x2]
        # new_img = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
        # cv2.imwrite(str(x)+str(y)+'.jpg',new_img)
        new_img = (new_img / 255.0)
        # img = img / 255.
        new_img = (new_img - 0.5) * 2.0

        resize_img = cv2.resize(new_img, (96,96), interpolation=cv2.INTER_LINEAR)
        flatten_img = np.reshape(resize_img, (96,96,3))
        im5 = np.expand_dims(flatten_img,axis = 0)

    # Perform the actual detection by running the model with the image as input
        image_np_expanded = im5.astype('float32') # 类型也要满足要求

        interpreter_2.set_tensor(input_details_2[0]['index'],image_np_expanded)
        interpreter_2.invoke()
        output_data_2 = interpreter_2.get_tensor(output_details_2[0]['index'])

    #     # 出来的结果去掉没用的维度   np.where(result==np.max(result)))[0][0]
        result = np.squeeze(output_data_2)
        result_accuracy =  round(np.max(result),2)
        ges_class = np.where(result==np.max(result))[0][0]

        # if result_accuracy >= 0.95:
        #     interpreter_1.set_tensor(input_details_1[0]['index'],image_np_expanded)
        #     interpreter_1.invoke()
        #     output_data_1 = interpreter_2.get_tensor(output_details_1[0]['index'])
        #     result_1 = np.squeeze(output_data_1)

        #     result_accuracy_1 =  round(np.max(result_1),2)
        #     ges_class_1 = np.where(result_1==np.max(result_1))[0][0]

        #     if (ges_class_1 == 0 and result_accuracy_1 >= 0.95) or (ges_class_1 == 1 and result_accuracy_1 >= 0.95):
        #         return result_accuracy_1,ges_class_1


        return result_accuracy,ges_class

    @staticmethod
    def traffic_detect(img):

        if Vilib.detect_obj_parameter['ts_flag']  == True:
            # resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
            cv2.circle(img, (160,120), 1, (255,255,255), -1)
            # print(hsv[160,120])
            # print(Vilib.lower_color)
            
            ### red
            mask_red_1 = cv2.inRange(hsv,(157,20,20), (180,255,255))
            mask_red_2 = cv2.inRange(hsv,(0,20,20), (10,255,255))
            # mask_red_2 = cv2.inRange(hsv, (175,50,20), (180,255,255))

            ### blue
            mask_blue = cv2.inRange(hsv,(92,10,10), (125,255,255))

            ### all
            mask_all = cv2.bitwise_or(mask_red_1, mask_blue)
            
            mask_all = cv2.bitwise_or(mask_red_2, mask_all)
            

        # color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[166,180]}

            open_img = cv2.morphologyEx(mask_all, cv2.MORPH_OPEN,Vilib.kernel_5,iterations=1)              #开运算 
            # open_img = cv2.dilate(open_img, Vilib.kernel_5,iterations=5)  

            contours, hierarchy = cv2.findContours(open_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          ####在binary中发现轮廓，轮廓按照面积从小到大排列
                # p=0
            contours = sorted(contours,key = Vilib.cnt_area, reverse=False)
            traffic_n = len(contours)
            max_area = 0
            traffic_sign_num = 0

            if traffic_n > 0: 
                for i in contours:    #遍历所有的轮廓
                    x,y,w,h = cv2.boundingRect(i)      #将轮廓分解为识别对象的左上角坐标和宽、高

                        #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
                    if w > 32 and h > 32: 
                        # cv2.drawContours(img,i,0,(0,0,255),3)

                        # if corners == 3:
                        #     count = self.shapes['triangle']
                        #     count = count+1
                        #     self.shapes['triangle'] = count
                        #     shape_type = "三角形"
                        # if corners == 4:
                        #     count = self.shapes['rectangle']
                        #     count = count + 1
                        #     self.shapes['rectangle'] = count
                        #     shape_type = "矩形"

                        #     self.shapes['circles'] = count
                        #     shape_type = "圆形"
                        # else if 4 < corners < 10:
                        #     count = self.shapes['polygons']
                        #     count = count + 1
                        #     self.shapes['polygons'] = count
                        #     shape_type = "多边形"
                        # x = x*2
                        # y = y*2
                        # w = w*2
                        # h = h*2
                        acc_val, traffic_type = Vilib.traffic_predict(img,x,y,w,h)
                        # print(traffic_type,acc_val)
                        acc_val = round(acc_val*100)
                        if acc_val >= 75:   

                            if traffic_type == 1 or traffic_type == 2 or traffic_type == 3:
                                # hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV   'blue':[92,110]  
            # print(Vilib.lower_color)
                                # mask = cv2.inRange(hsv, (92,50,20), (110,255,255))           # 3.inRange()：介于lower/upper之间的为白色，其余黑色

                                simple_gray = cv2.cvtColor(img[y:y+h,x:x+w], cv2.COLOR_BGR2GRAY)
                                # new_mask_blue = cv2.inRange(hsv[y:y+h,x:x+w],(92,70,50), (118,255,255))
                                circles = cv2.HoughCircles(simple_gray,cv2.HOUGH_GRADIENT,1,32,\
                                param1=140,param2=70,minRadius=int(w/4.0),maxRadius=max(w,h))
                               
                                if circles is not None:
                                    for i in circles[0,:]:
                                    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
                                        traffic_sign_coor = (int(x+i[0]),int(y+i[1]))
                                        cv2.circle(img,traffic_sign_coor,i[2],(255,0,255),2)
                                        cv2.putText(img,str(traffic_dict[traffic_type]) +': ' + str(round(acc_val)),(int(x+i[0]-i[2]),int(y+i[1]-i[2])), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),2)#加减10是调整字符位置
                                        if w * h > max_area:
                                            max_area = w * h
                                            max_obj_x = x
                                            max_obj_y = y
                                            max_obj_w = w
                                            max_obj_h = h
                                            max_obj_t = traffic_type
                                            max_obj_acc = acc_val
                                            traffic_sign_num += 1

                            elif traffic_type == 0:
                                # small_hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)
                                red_mask_1 = cv2.inRange(hsv[y:y+h,x:x+w],(0,50,20), (4,255,255))           # 3.inRange()：介于lower/upper之间的为白色，其余黑色
                                red_mask_2 = cv2.inRange(hsv[y:y+h,x:x+w],(163,50,20), (180,255,255))
                                red_mask_all = cv2.bitwise_or(red_mask_1,red_mask_2)

                                        
                                # circles = np.uint16(np.around(circles))

                                # ret, new_binary = cv2.threshold(simple_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
                                new_binary = cv2.GaussianBlur(red_mask_all, (5, 5), 0)

                                open_img = cv2.morphologyEx(red_mask_all, cv2.MORPH_OPEN,Vilib.kernel_5,iterations=1)              #开运算  
                                open_img = cv2.dilate(open_img, Vilib.kernel_5,iterations=5) 

                                blue_contours, hierarchy = cv2.findContours(open_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)          ####在binary中发现轮廓，轮廓按照面积从小到大排列
                                
                                contours_count = len(blue_contours)
                                if contours_count >=1:
                                # print("contours:",contours_count)
                                    blue_contours = sorted(blue_contours,key = Vilib.cnt_area, reverse=True)
                                
                                # cv2.drawContours(img,contours,0,(0,0,255),3)
                                # print(len(blue_contours[0]))
                                
                                    epsilon = 0.025 * cv2.arcLength(blue_contours[0], True)
                                    approx = cv2.approxPolyDP(blue_contours[0], epsilon, True)

                                #     # 分析几何形状
                                    corners = len(approx)
                                    
                                #     # shape_type = ""
                                #     cv2.drawContours(img,blue_contours,0,(0,0,255),1)
                                    # print(corners)
                                    if corners >= 0:
                                        # print("corners:",corners)
                                        # print("eight")
                                        traffic_sign_coor = (int(x+w/2),int(y+h/2))
                                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                                        cv2.putText(img,str(traffic_dict[traffic_type]) +': ' + str(round(acc_val)),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,255),2)#加减10是调整字符位置
                                        if w * h > max_area:
                                            max_area = w * h
                                            max_obj_x = x
                                            max_obj_y = y
                                            max_obj_w = w
                                            max_obj_h = h
                                            max_obj_t = traffic_type
                                            max_obj_acc = acc_val
                                            traffic_sign_num += 1

                                        
                # print("traffic_sign_num:",traffic_sign_num)         
                if traffic_sign_num > 0:

                    Vilib.detect_obj_parameter['traffic_sign_x'] = int(max_obj_x + max_obj_w/2)
                    Vilib.detect_obj_parameter['traffic_sign_y'] = int(max_obj_y + max_obj_h/2)
                    Vilib.detect_obj_parameter['traffic_sign_w'] = max_obj_w
                    Vilib.detect_obj_parameter['traffic_sign_h'] = max_obj_h
                    # print("traffic_sign_type:",)
                    Vilib.detect_obj_parameter['traffic_sign_t'] = traffic_dict[max_obj_t]
                    Vilib.detect_obj_parameter['traffic_sign_acc'] = max_obj_acc
                else:
                    Vilib.detect_obj_parameter['traffic_sign_x'] = 320
                    Vilib.detect_obj_parameter['traffic_sign_y'] = 240
                    Vilib.detect_obj_parameter['traffic_sign_w'] = 0
                    Vilib.detect_obj_parameter['traffic_sign_h'] = 0
                    Vilib.detect_obj_parameter['traffic_sign_t'] = 'none'
                    Vilib.detect_obj_parameter['traffic_sign_acc'] = 0
                                    # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                                        

                                    # cv2.putText(img,str(ges_dict[ges_type]) +': ' + str(round(acc_val*100)),(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)#加减10是调整字符位置
 
        #                 object_area = w*h
        #                 if object_area > max_area: 
        #                     max_area = object_area
        #                     Vilib.detect_obj_parameter['color_x'] = int(x + w/2)
        #                     Vilib.detect_obj_parameter['color_y'] = int(y + h/2)
        #                     Vilib.detect_obj_parameter['color_w'] = w
        #                     Vilib.detect_obj_parameter['color_h'] = h
        #                     # print()
        #     else:
        #         Vilib.detect_obj_parameter['color_x'] = 160
        #         Vilib.detect_obj_parameter['color_y'] = 120
        #         Vilib.detect_obj_parameter['color_w'] = 0
        #         Vilib.detect_obj_parameter['color_h'] = 0
        #         Vilib.detect_obj_parameter['color_n'] = 0
        #     return img
        # else:
        else:
            Vilib.detect_obj_parameter['traffic_sign_x'] = 320
            Vilib.detect_obj_parameter['traffic_sign_y'] = 240
            Vilib.detect_obj_parameter['traffic_sign_w'] = 0
            Vilib.detect_obj_parameter['traffic_sign_h'] = 0
            Vilib.detect_obj_parameter['traffic_sign_t'] = 'none'
            Vilib.detect_obj_parameter['traffic_sign_acc'] = 0

        return img


    @staticmethod
    def gesture_recognition(img):
        if Vilib.detect_obj_parameter['gs_flag'] == True:

    ###肤色部分

            target_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # 首先对样本图像计算2D直方图
            roi_hsv_hist = cv2.calcHist([Vilib.roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 255])
            # 对得到的样本2D直方图进行归一化
            # 这样可以方便显示，归一化后的直方图就变成0-255之间的数了
            # cv2.NORM_MINMAX表示对数组所有值进行转换，线性映射到最大最小值之间
            cv2.normalize(roi_hsv_hist, roi_hsv_hist, 0, 255, cv2.NORM_MINMAX)
            # 对待检测图像进行反向投影
            # 最后一个参数为尺度参数
            dst = cv2.calcBackProject([target_hsv], [0, 1], roi_hsv_hist, [0, 180, 0, 256], 1)
            # 构建一个圆形卷积核，用于对图像进行平滑，连接分散的像素
            disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            dst = cv2.filter2D(dst, -1, disc,dst)
            ret, thresh = cv2.threshold(dst, 1, 255, 0)
            dilate = cv2.dilate(thresh, Vilib.kernel_5, iterations=3)
                # 注意由于原图是三通道BGR图像，因此在进行位运算之前，先要把thresh转成三通道
            # thresh = cv2.merge((dilate, dilate, dilate))
                # 对原图与二值化后的阈值图像进行位运算，得到结果
            # res = cv2.bitwise_and(img, thresh)
            
            # ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)

            # cr_skin = cv2.inRange(ycrcb, (85,124,121), (111,131,128))

            # open_img = cv2.morphologyEx(cr_skin, cv2.MORPH_OPEN,Vilib.kernel_5,iterations=1)

            contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            ges_num = len(contours)
            # max_area = 0
            # max_x = 0
            # max_y = 0
            # max_w = 0
            # max_h = 0
            # point_size = 1
            # point_color = (0, 0, 255) # BGR
            # thickness = 4 # 可以为 0 、4、8
            
            # acc_val,ges_type = Vilib.gesture_predict(img,x,y,w,h) 
            # print(ycrcb[160,120])
            # cv2.rectangle(img,(160-96,120-96),(160+96, 120+96),(0,125,0),2, cv2.LINE_AA)
            # acc_val,ges_type = Vilib.gesture_predict(img,160-96,120-96,192,192) 

            # # cv2.rectangle(img,(160-96,120-96),(160+96, 120+96),(0,125,125),2, cv2.LINE_AA)
            # cv2.putText(img,str(ges_type)+': '+str(round(acc_val*100)) + '%',(160-96,120-96),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,97,240),2)

            if ges_num > 0:
                contours = sorted(contours,key = Vilib.cnt_area, reverse=True)
                # for i in range(0,len(contours)):    #遍历所有的轮廓
                x,y,w,h = cv2.boundingRect(contours[0])      #将轮廓分解为识别对象的左上角坐标和宽、高
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
                faces = Vilib.face_cascade.detectMultiScale(gray[y:y+h,x:x+w], 1.3, 2)
            # print(len(faces))
                face_len = len(faces)
                    

                        #在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）

                    
                if w >= 60 and h >= 60 and face_len == 0:
                    # acc_val,ges_type = Vilib.gesture_predict(img,x-2.2*w,y-2.8*h,4.4*w,5.6*h) 
                    acc_val,ges_type = Vilib.gesture_predict(img,x-0.1*w,y-0.2*h,1.1*w,1.2*h) 
                        # x = x*2
                        # y = y*2
                        # w = w*2
                        # h = h*2
                    acc_val = round(acc_val*100,3)
                    if acc_val >= 75:
                        # print(x,y,w,h)
                        cv2.rectangle(img,(int(x-0.1*w),int(y-0.2*h)),(int(x+1.1*w), int(y+1.2*h)),(0,125,0),2, cv2.LINE_AA)
                        cv2.rectangle(img,(0,0),(125,27),(204,209,72),-1, cv2.LINE_AA)
                        cv2.putText(img,ges_dict[ges_type]+': '+str(acc_val) + '%',(0,17),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)  ##(0,97,240)

                        # object_area = w*h
                        # if object_area > max_area: 
                        #     max_area = object_area

                        # max_x = int(x + w/2)
                        # max_y = int(y + h/2)
                        # max_w = w
                        # max_h = h

                        Vilib.detect_obj_parameter['gesture_x'] = int(x + w/2)
                        Vilib.detect_obj_parameter['gesture_y'] = int(y + h/2)
                        Vilib.detect_obj_parameter['gesture_w'] = w
                        Vilib.detect_obj_parameter['gesture_h'] = h
                        Vilib.detect_obj_parameter['gesture_t'] = ges_dict[ges_type]
                        Vilib.detect_obj_parameter['gesture_acc'] = acc_val
                                # print()
                    else:
                        Vilib.detect_obj_parameter['gesture_x'] = 320
                        Vilib.detect_obj_parameter['gesture_y'] = 240
                        Vilib.detect_obj_parameter['gesture_w'] = 0
                        Vilib.detect_obj_parameter['gesture_h'] = 0
                        Vilib.detect_obj_parameter['gesture_t'] = 'none'
                        Vilib.detect_obj_parameter['gesture_acc'] = 0

            # else:
            #     # cv2.rectangle(img,(55,35),(210,160),(255,0,0),2, cv2.LINE_AA)
            #     return img
            #     # cv2.rectangle(img,(55,35),(210,160),(255,0,0),2, cv2.LINE_AA)
                else:
                    Vilib.detect_obj_parameter['gesture_x'] = 320
                    Vilib.detect_obj_parameter['gesture_y'] = 240
                    Vilib.detect_obj_parameter['gesture_w'] = 0
                    Vilib.detect_obj_parameter['gesture_h'] = 0
                    Vilib.detect_obj_parameter['gesture_t'] = 'none'
                    Vilib.detect_obj_parameter['gesture_acc'] = 0

            else:
                Vilib.detect_obj_parameter['gesture_x'] = 320
                Vilib.detect_obj_parameter['gesture_y'] = 240
                Vilib.detect_obj_parameter['gesture_w'] = 0
                Vilib.detect_obj_parameter['gesture_h'] = 0
                Vilib.detect_obj_parameter['gesture_t'] = 'none'
                Vilib.detect_obj_parameter['gesture_acc'] = 0

        return img

    @staticmethod
    def human_detect_func(img):
        if Vilib.detect_obj_parameter['hdf_flag'] == True:
            resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)            # 2.从BGR转换到RAY
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
                    # face_gray = cv2.cvtColor(img[y:y + w, x:x + h], cv2.COLOR_BGR2GRAY) 
                    # label = face_recognizer.predict(face_gray)
                    # if round(label[1],2) > 80:
                    #     cv2.putText(img, master_name[label[0]] + ": " + str(round(label[1],2)), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 0), 2)
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                    object_area = w*h
                    if object_area > max_area: 
                        object_area = max_area
                        Vilib.detect_obj_parameter['human_x'] = int(x + w/2)
                        Vilib.detect_obj_parameter['human_y'] = int(y + h/2)
                        Vilib.detect_obj_parameter['human_w'] = w
                        Vilib.detect_obj_parameter['human_h'] = h
            
            else:
                Vilib.detect_obj_parameter['human_x'] = 320
                Vilib.detect_obj_parameter['human_y'] = 240
                Vilib.detect_obj_parameter['human_w'] = 0
                Vilib.detect_obj_parameter['human_h'] = 0
                Vilib.detect_obj_parameter['human_n'] = 0
            return img
        else:
            return img


    # @staticmethod
    # def new_color_detect(img):
    #     # resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)
    #     brightLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    #     bgr = [40, 158, 16]
    #     thresh = 40
    #     lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]

    #     minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
    #     maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])

    #     maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
    #     resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)

    #     return resultLAB



    @staticmethod
    def color_detect_func(img):

        # 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度
        if Vilib.detect_obj_parameter['cdf_flag']  == True:
            resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)
            hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
            # print(Vilib.lower_color)
            color_type = Vilib.detect_obj_parameter['color_default']
            
            mask = cv2.inRange(hsv,np.array([min(Vilib.color_dict[color_type]), 60, 60]), np.array([max(Vilib.color_dict[color_type]), 255, 255]) )           # 3.inRange()：介于lower/upper之间的为白色，其余黑色
            if color_type == 'red':
                 mask_2 = cv2.inRange(hsv, (167,0,0), (180,255,255))
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
                    if w >= 8 and h >= 8: 
                        x = x*4
                        y = y*4
                        w = w*4
                        h = h*4
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                                #给识别对象写上标号
                        cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)#加减10是调整字符位置
 
                        object_area = w*h
                        if object_area > max_area: 
                            max_area = object_area
                            Vilib.detect_obj_parameter['color_x'] = int(x + w/2)
                            Vilib.detect_obj_parameter['color_y'] = int(y + h/2)
                            Vilib.detect_obj_parameter['color_w'] = w
                            Vilib.detect_obj_parameter['color_h'] = h
                            # print()
            else:
                Vilib.detect_obj_parameter['color_x'] = 320
                Vilib.detect_obj_parameter['color_y'] = 240
                Vilib.detect_obj_parameter['color_w'] = 0
                Vilib.detect_obj_parameter['color_h'] = 0
                Vilib.detect_obj_parameter['color_n'] = 0
            return img
        else:
            return img


    @staticmethod
    def qrcode_detect_func(img):
        if Vilib.detect_obj_parameter['qr_flag']  == True:
            barcodes = pyzbar.decode(img)
            # 循环检测到的条形码
            if len(barcodes) > 0:
                for barcode in barcodes:
                    # 提取条形码的边界框的位置
                    # 画出图像中条形码的边界框
                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

                    # 条形码数据为字节对象，所以如果我们想在输出图像上
                    # 画出来，就需要先将它转换成字符串
                    barcodeData = barcode.data.decode("utf-8")
                    # barcodeType = barcode.type

                    # 绘出图像上条形码的数据和条形码类型
                    # text = "{} ({})".format(barcodeData, barcodeType)
                    text = "{}".format(barcodeData)
                    if len(text) > 0:
                        Vilib.detect_obj_parameter['qr_data'] = text
                        Vilib.detect_obj_parameter['qr_h'] = h
                        Vilib.detect_obj_parameter['qr_w'] = w
                        Vilib.detect_obj_parameter['qr_x'] = x 
                        Vilib.detect_obj_parameter['qr_y'] = y
                    # print("Vilib.qr_date:%s"%Vilib.qr_date)
                    cv2.putText(img, text, (x - 20, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (0, 0, 255), 2)
            else:
                Vilib.detect_obj_parameter['qr_data'] = "None"
                Vilib.detect_obj_parameter['qr_x'] = 320
                Vilib.detect_obj_parameter['qr_y'] = 240
                Vilib.detect_obj_parameter['qr_w'] = 0
                Vilib.detect_obj_parameter['qr_h'] = 0
            return img
        else:
            return img

    @staticmethod
    def new_color_detect_func(img,color):
        Vilib.detect_color_name(color)

        # 蓝色的范围，不同光照条件下不一样，可灵活调整   H：色度，S：饱和度 v:明度
        if Vilib.detect_obj_parameter['cdf_flag']  == True:
            resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)
            hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # 2.从BGR转换到HSV
            # print(Vilib.lower_color)
            color_type = Vilib.detect_obj_parameter['color_default']
            
            mask = cv2.inRange(hsv,np.array([min(Vilib.color_dict[color_type]), 60, 60]), np.array([max(Vilib.color_dict[color_type]), 255, 255]) )           # 3.inRange()：介于lower/upper之间的为白色，其余黑色
            if color_type == 'red':
                 mask_2 = cv2.inRange(hsv, (167,0,0), (180,255,255))
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
                    if w >= 8 and h >= 8: 
                        x = x*2
                        y = y*2
                        w = w*2
                        h = h*2
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                                #给识别对象写上标号
                        cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)#加减10是调整字符位置
 
                        object_area = w*h
                        if object_area > max_area: 
                            max_area = object_area
                            Vilib.detect_obj_parameter['color_x'] = int(x + w/2)
                            Vilib.detect_obj_parameter['color_y'] = int(y + h/2)
                            Vilib.detect_obj_parameter['color_w'] = w
                            Vilib.detect_obj_parameter['color_h'] = h
                            # print()
            else:
                Vilib.detect_obj_parameter['color_x'] = 320
                Vilib.detect_obj_parameter['color_y'] = 240
                Vilib.detect_obj_parameter['color_w'] = 0
                Vilib.detect_obj_parameter['color_h'] = 0
                Vilib.detect_obj_parameter['color_n'] = 0
            return img
        else:
            return img


    # @staticmethod
    # def object_follow(img):
    #     if Vilib.detect_obj_parameter['object_follow_flag']  == True:
    #         hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #         dst = cv2.calcBackProject([hsv],[0,1],Vilib.roi_hist,[0,180,0,256],1)#反向投影
    #         disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    #         dst = cv2.filter2D(dst,-1,disc,dst)
    #         ret,thresh = cv2.threshold(dst,1,255,0)
    #         # dilate = cv2.dilate(thresh,kernel_5,iterations=3)

    #         #使用 meanshift获得新位置
    #         ret, track_window = cv2.CamShift(thresh,Vilib.track_window, term_crit)
    #         # print(ret)

    #         #显示标记
    #         print(ret)
    #         pts = cv2.boxPoints(ret)
    #         pts = np.int0(pts)
    #         img = cv2.polylines(img,[pts],True, (255,0,0),2)
    #         return img
    #     else:
    #         return img

if __name__ == "__main__":
    Vilib.camera_start()
    while True:
        pass