#!/usr/bin/env python3
from picarx import Picarx
from time import sleep
import readchar 

manual = '''
----- Picar-X Calibration Helper -------      
                      
    1: direction servo
    2: camera servo 1
    3: camera servo 2
    4: left motor
    5: right motor
    W: increase servo angle           
    S: decrease servo angle
    Q: change motor direction
    E: motors run/stop
    R: servos test 
    SPACE: confirm calibration
    Crtl+C: quit
'''    

px = Picarx()
px_power = 10

servo_num = 0
motor_num = 0
servo_names = ['direction servo', 'camera servo 1', 'camera servo 2']
motor_names = ['left motor', 'right motor']
servos_cali = [px.dir_cal_value, px.cam_cal_value_1, px.cam_cal_value_2]
motors_cali = px.cali_dir_value
servos_offset = list.copy(servos_cali)
motors_offset = list.copy(motors_cali)

def servos_test():
    px.set_dir_servo_angle(-30)
    sleep(0.5)
    px.set_dir_servo_angle(30)
    sleep(0.5)
    px.set_dir_servo_angle(0)
    sleep(0.5)   

def servos_move(servo_num, value):
    if servo_num == 0:
        px.set_dir_servo_angle(value)
    elif servo_num == 1:
        px.set_camera_servo1_angle(value)
    elif servo_num == 2:
        px.set_camera_servo2_angle(value)
    sleep(0.2)

def set_servos_offset(servo_num, value):
    if servo_num == 0:
        px.dir_cal_value = value
    elif servo_num == 1:
        px.cam_cal_value_1 = value
    elif servo_num == 2:
        px.cam_cal_value_2  = value  

def servos_reset():
    for i in range(3):
        servos_move(i,0)

def show_info():
    print("\033[H\033[J", end='')  # clear terminal windows
    print(manual)
    print('[ %s ] [ %s ]'%(servo_names[servo_num], motor_names[motor_num])) 
    print('offset: %s, %s'%(servos_offset, motors_offset))


def cali_helper(): 
    global servo_num, motor_num
    global servos_cali, motors_cali, servos_offset, motors_offset
    motor_run = False
    step = 1
    # reset
    servos_reset()
    # show_info 
    show_info()

    # key control
    while True:
        # readkey
        key = readchar.readkey()
        key = key.lower()
        # select the servo 
        if key in ('123'):
            servo_num = int(key)-1
            show_info()
        if key in ('45'):
            motor_num = int(key)-4
            show_info()
        # servos move
        elif key == 'r':
            servos_test()
        elif key == 'w':
            servos_offset[servo_num] += step
            if servos_offset[servo_num] > 20:
                servos_offset[servo_num] =20
            show_info()
            # angle = servos_offset[servo_num] - servos_cali[servo_num]
            # print(1,angle)
            # servos_move(servo_num, angle)
            set_servos_offset(servo_num, servos_offset[servo_num])
            servos_move(servo_num, 0)
        elif key == 's':
            servos_offset[servo_num] -= step
            if servos_offset[servo_num] < -20:
                servos_offset[servo_num] = -20
            show_info()
            # angle = servos_offset[servo_num] - servos_cali[servo_num]
            # print(2,angle)
            # servos_move(servo_num,servos_offset[servo_num])
            set_servos_offset(servo_num, servos_offset[servo_num])
            servos_move(servo_num, 0)
        # motors move
        elif key == 'q': 
            motors_offset[motor_num] = -1 * motors_offset[motor_num]
            px.cali_dir_value = list.copy(motors_offset)
            motor_run = True
            px.forward(px_power)
            show_info()
        elif key == 'e':
            if motor_run == False:
                motor_run = True
                px.forward(px_power)
            else:
                motor_run = False
                px.stop()
        # save
        elif key == readchar.key.SPACE:
            print('Confirm save ?(y/n)')
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key == 'y':
                    px.dir_servo_angle_calibration(servos_offset[0])
                    px.camera_servo1_angle_calibration(servos_offset[1])
                    px.camera_servo2_angle_calibration(servos_offset[2])
                    px.motor_direction_calibration(motor_num +1 , motors_offset[motor_num])
                    sleep(0.2)
                    servos_offset = [px.dir_cal_value, px.cam_cal_value_1, px.cam_cal_value_2]
                    show_info()
                    print('The calibration value has been saved.')
                    break
                elif key == 'n':
                    show_info()
                    break   
                sleep(0.01) 
        sleep(0.01)


if __name__ == "__main__":
    try:
        cali_helper()
    except KeyboardInterrupt:
        print('quit')
    except Exception as e:
        print(e)
