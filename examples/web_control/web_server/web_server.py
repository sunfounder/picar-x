import asyncio
import websockets
import json
import time
import os
import picar_x as car
# from ezblock import Taskmgr
from ezblock import getIP, TTS, Pin
from ezblock.modules import Ultrasonic
from vilib import Vilib
import Music as music
# import pathlib
# import ssl

ip = getIP()

Vilib.camera_start()
# Vilib.human_detect_switch(True)
# Vilib.color_detect_switch(True)

class Websocket():
    recv_dict = {
        'JA':[0,0],  #小车控制
        'JB':[0,0],  #云台控制
        'SS':['off',0,0.5], #喇叭播放音效
        'SM':['off',0,0.5], #喇叭播放音乐
        # 'SL':['off',0,0.5], #喇叭播放录音
        'TT':['off','you'],  #TTS
        'US':'off',  #超声波
        'GS':"off", #灰度开关
        'OA':'off',  #避障开关
        'TL':['off',950], #巡线开关
        'CD':['off',110], #悬崖开关
        'HT':'off', #人脸开关
        'HF':'off', #人脸跟踪
        'CT':'off', #颜色开关
        'CF':'off', #颜色跟踪
        'MS':['off',0,0], #车轮测试
        'DO':['off',0],  #方向舵机校准
        'PO':['off',0],  #云台左右舵机
        'TO':['off',0] , #云台上下舵机
        'CC':'blue', #颜色选择
        
    }

    send_dict = {
        'TP':'PiCar-X',
        'GS':[0,0,0],
        'US':20,
        'DO':0,  #方向舵机校准值
        'PO':0,  
        'TO':0,
        'CC':'blue',
        'AD':'http://' + ip + ':8888/mjpg',
        # 'FD':'http://' + ip + ':8000/records',
        'FF':'True'
    } 
    
    def __init__(self):
        self.gs_list = [0,0,0]
        self.sound_name = ['Weapon_Armor.wav', 'Emergency_Alarm.wav', 'Emergency_Truck_Honk.wav', 'Weapon_Continue_Shooting.wav', 'Weapon_Shell_Drop.wav']
        self.music_name = ["excitement.mp3", 'peace.mp3', 'power.mp3', 'spry.mp3','angry.mp3']
        self.record_name = ['1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3']
        self.us = Ultrasonic(Pin('D0'), Pin('D1'))
        self.music_flag = True
        self.tts = TTS()
        self.current_music = -1
        
        
    async def recv_server_func(self, websocket):
        while 1:
            tmp = await websocket.recv()
            print(tmp)
            tmp = json.loads(tmp)
            
            for key in tmp:
                self.recv_dict[key] = tmp[key]
            print("recv_dict: %s"%self.recv_dict)
            self.remote_control(self.recv_dict['JA'])
            self.camera_contrl(self.recv_dict['JB'])
            # print(recv_dict)
            if self.recv_dict['MS'][0] =='on':
                car.set_motor_speed(int(self.recv_dict['MS'][1]), int(self.recv_dict['MS'][2]))
            if self.recv_dict['DO'][0] =='on':
                car.dir_servo_angle_calibration(int(self.recv_dict['DO'][1]))
            if self.recv_dict['PO'][0] =='on':
                car.camera_servo1_angle_calibration(-int(self.recv_dict['PO'][1]))
            if self.recv_dict['TO'][0] =='on':
                car.camera_servo2_angle_calibration(-int(self.recv_dict['TO'][1]))
            Vilib.detect_color_name(str(self.recv_dict['CC']))
    
    def map(self, value, inMin, inMax, outMin, outMax):
        return (outMax - outMin) * (value - inMin) / (inMax - inMin) + outMin
            
    def remote_control(self, move):
        dr = int(move[0])
        dr_angle = self.map(dr, -100, 100, -45, 45)
        car.set_dir_servo_angle(dr_angle)
        # print("dr_angle:%s"%dr_angle)
        # time.sleep(0.1)
        pow = int(move[1])
        car.set_power(pow)
        
    
    def camera_contrl(self, value):
        val1 = int(value[0])
        val1 = self.map(val1, -100, 100, -90, 90)
        car.set_camera_servo1_angle(-val1)
        val2 = int(value[1])
        val2 = self.map(val2, -100, 100, -45, 45)
        car.set_camera_servo2_angle(-val2)
    

    async def send_server_func(self, websocket): 
        while 1:
           
            if self.recv_dict['US'] =='on':
                self.send_dict['US'] = self.us.read()
                # print(self.get_us_distance(int(self.recv_dict['US'][1])))
            
            if  self.recv_dict['GS'] =='on': 
                self.send_dict['GS'] = self.gs_list
            self.send_dict['DO'] = car.dir_cal_value
            self.send_dict['PO'] = car.cam_cal_value_1
            self.send_dict['TO'] = car.cam_cal_value_2
            self.send_dict['CC'] = Vilib.detect_obj_parameter['color_default'] 
            # print(self.send_dict)
           
            await websocket.send(json.dumps(self.send_dict))
            await asyncio.sleep(0.01)
    
    
        
    async def main_func(self):
        while 1:
            self.gs_list = car.get_adc_value()
            if self.recv_dict['CD'][0] == 'on':
                if self.is_on_edge(int(self.recv_dict['CD'][1]),self.gs_list):
                    car.backward(50)
                    time.sleep(0.5)
                    car.stop()

            if self.recv_dict['TL'][0] =='on':
                # print("line_follow on")
                car.ref = int(self.recv_dict['TL'][1])
                car.line_follow()

            if self.recv_dict['OA'] == 'on':
                # print("ultrasonic on")
                distance = self.us.read()
                if distance > 40 or distance == -2:
                    car.set_dir_servo_angle(0)
                    car.forward(50)
                elif distance < 10:
                    car.set_dir_servo_angle(-40)
                    car.backward(50)
                    time.sleep(0.5)
                elif distance < 30:
                    car.set_dir_servo_angle(40)
                    car.forward(50)
                    time.sleep(0.5)
                    
            
            if self.recv_dict['HT'] == 'on':
                Vilib.human_detect_switch(True)
            
            if self.recv_dict['HT'] == 'off':
                Vilib.human_detect_switch(False)
                
            if self.recv_dict['HF'] == 'on':
                car.human_follow()
            
            if self.recv_dict['CT'] == 'on':
                Vilib.color_detect_switch(True)
            
            if self.recv_dict['CT'] == 'off':
                Vilib.color_detect_switch(False)
            
            if self.recv_dict['CF'] == 'on':
                car.color_follow()
            
            if self.recv_dict['SS'][0] == 'on':
                music.sound_effect_threading(self.sound_name[int(self.recv_dict['SS'][1])], float(self.recv_dict['SS'][2]))
                self.recv_dict['SS'][0] = 'off' 
            
            if self.recv_dict['SM'][0] == 'on':
                temp = int(self.recv_dict['SM'][1])
                if self.current_music != temp:
                    music.music_stop()
                    self.music_flag = True
                    self.current_music = temp
                if self.music_flag:
                    try:
                        music_file = self.music_name[self.current_music]
                        volume = float(self.recv_dict['SM'][2])
                        music.background_music(music_file, volume=volume) 
                    except IndexError:
                        print("no such music file: ", int(self.recv_dict['SM'][1]) + 1)
                    self.music_flag = False
                # self.recv_dict['SM'][0] = 'off' 
            elif self.recv_dict['SM'][0] == 'off':
                if self.music_flag == False:
                    music.music_stop()
                    self.music_flag = True
            
            # if self.recv_dict['SL'][0] == 'on':
            #     if self.found_name(self.record_name[int(self.recv_dict['SL'][1])]):
            #         self.send_dict['FF'] = 'True'
            #         print("play")
            #         music.record_play(self.record_name[int(self.recv_dict['SL'][1])],volume = float(self.recv_dict['SL'][2]))
            #         self.recv_dict['SL'][0] = 'off'
            #     else:
            #         self.send_dict['FF'] = 'False'
                
                
            if self.recv_dict['TT'][0] == 'on':
                self.tts.say(self.recv_dict['TT'][1]) 
                self.recv_dict['TT'][0] = 'off'  
            
        
            await asyncio.sleep(0.01)
            
    def is_on_edge(self, ref, gs_list):
        ref = int(ref)
        if gs_list[2] <= ref or gs_list[1] <= ref or gs_list[0] <= ref:  
            return True
        else:
            return False 
    
    def found_name(self, name):
        if name in os.listdir("./records"):
            return True
        else:
            return False
        
    
     
    
        
    async def main_logic_1(self, websocket, path):
        while 1:
            await self.recv_server_func(websocket)

    async def main_logic_2(self, websocket, path):
        while 1:
            await self.send_server_func(websocket)
            
    def test(self):
        try:
            for _ in range(10):
                # ip = getIP()
                if ip:
                    print("IP Address: "+ ip)
                    # start_http_server()
                    break
                time.sleep(1)
            # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            # localhost_pem = pathlib.Path(__file__).with_name("server.pem")
            # ssl_context.load_cert_chain(localhost_pem)
            start_server_1 = websockets.serve(self.main_logic_1, ip, 8765)
            start_server_2 = websockets.serve(self.main_logic_2, ip, 8766)
            print('Start!')
            tasks = [self.main_func(),start_server_1,start_server_2]
            asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
            asyncio.get_event_loop().run_forever()
 
        finally:
            print("Finished")
            car.stop()

if __name__ == "__main__":
    ws = Websocket()
    ws.test()


