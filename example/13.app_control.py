from sunfounder_controller import SunFounderController
from picarx import Picarx
from robot_hat import utils, Music
from vilib import Vilib
import os
from time import sleep

# reset robot_hat
utils.reset_mcu()
sleep(0.2)

# init SunFounder Controller class
sc = SunFounderController()
sc.set_name('Picarx-001')
sc.set_type('Picarx')
sc.start()

# init picarx
px = Picarx()
speed = 50
line_following_speed = 20
line_following_angle_offset = 20
avoid_obstacles_speed = 30

# init music player
music = Music()
if os.geteuid() != 0:
    print('\033[33mPlay sound needs to be run with sudo.\033[m')

def horn(): 
    _status, _result = utils.run_command('sudo killall pulseaudio')
    music.sound_play_threading('./sounds/car-double-horn.wav')


def avoid_obstacles():
    px.forward(avoid_obstacles_speed)
    distance = px.get_distance()
    if distance > 0 and distance < 300:
        if distance < 25:
            px.set_dir_servo_angle(-35)
        else:
            px.set_dir_servo_angle(0)   


def line_following():
    gm_val_list = px.get_grayscale_data()
    gm_status = px.get_line_status(gm_val_list)
    if gm_status == 'forward':
        px.forward(line_following_speed) 
    elif gm_status == 'left':
        px.set_dir_servo_angle(line_following_angle_offset)
        px.forward(line_following_speed) 
    elif gm_status == 'right':
        px.set_dir_servo_angle(-line_following_angle_offset)
        px.forward(line_following_speed) 
    else:
        px.set_dir_servo_angle(0)
        px.stop()



def main():
    global speed

    ip = utils.get_ip()
    print('ip : %s'%ip)

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=False, web=True)
    speak = None
    while True:
        # sleep(0.2)

        # send data 
        sc.set('video','http://'+ip+':9000/mjpg')
        sc.set("A", speed)

        grayscale_data = px.get_grayscale_data()
        # print(px.get_grayscale_data())
        sc.set("D", grayscale_data )
        

        distance = px.get_distance()
        # sc.set("L", [0,distance])
        sc.set("F", distance)

        # if sc.get('J') == True:
        #     horn()

        # print(sc.get('J'), type(sc.get('J')), speak)
        if sc.get('J') != None:
            speak=sc.get('J')
        if speak == "forward":
            px.forward(speed)
        elif speak == "backward":
            px.backward(speed)
        elif speak == "left":
            px.left(speed)
        elif speak == "right":
            px.right(speed)
        else:
            px.stop()
            
        Joystick_K_Val = sc.get('K')
        if Joystick_K_Val != None:
            dir_angle = utils.mapping(Joystick_K_Val[0], -100, 100, -45, 45)
            speed = Joystick_K_Val[1]
            px.set_dir_servo_angle(dir_angle)
            if speed > 0:
                px.forward(speed)
            elif speed < 0:
                speed = -speed
                px.backward(speed)
            else:
                px.stop()

        if sc.get('I') == True:
            line_following()
        elif sc.get('E') == True:
            avoid_obstacles()


        if sc.get('N') == True:
            Vilib.color_detect("red")
        else:
            Vilib.color_detect_switch(False)

        if sc.get('O') == True:
            Vilib.human_detect_switch(True)  
        else:
            Vilib.human_detect_switch(False)  

        if sc.get('P') == True:
            Vilib.object_detect_switch(True) 
        else:
            Vilib.object_detect_switch(False)

        
        Joystick_Q_Val = sc.get('Q')
        if Joystick_Q_Val != None:
            pan = min(90, max(-90, Joystick_Q_Val[0]))
            tilt = min(65, max(-35, Joystick_Q_Val[1]))
            px.set_cam_pan_angle(pan)
            px.set_camera_tilt_angle(tilt)


def servos_test():
    px = Picarx()
    px.set_cam_pan_angle(0)
    px.set_camera_tilt_angle(0)
    sleep(0.5)

    while True:
        for angle in range(0,75):
            px.set_camera_tilt_angle(angle)
            sleep(0.01)
        for angle in range(75,-35,-1):
            px.set_camera_tilt_angle(angle)
            sleep(0.01)        
        for angle in range(-35,0):
            px.set_camera_tilt_angle(angle)
            sleep(0.01)


if __name__ == "__main__":
    try:
        main()
    finally:
        px.stop()
    # servos_test()


