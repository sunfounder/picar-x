#!/usr/bin/env python3
from picarx import Picarx
from time import sleep
import readchar 

manual = '''
--------------- Picar-X Calibration Helper -----------------

    [1]: direction servo            [W/D]: increase servo angle
    [2]: camera pan servo           [S/A]: decrease servo angle
    [3]: camera tilt servo          [R]: servos test

    [4]: left motor                 [Q]: change motor direction
    [5]: right motor                [E]: motors run/stop

    [SPACE]: confirm calibration                [Crtl+C]: quit
                                      
'''    

px = Picarx()
px_power = 30

servo_num = 0
motor_num = 0
servo_names = ['direction servo', 'camera pan servo', 'camera tilt servo']
motor_names = ['left motor', 'right motor']
servos_cali = [px.dir_cali_val, px.cam_pan_cali_val, px.cam_tilt_cali_val]
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
    px.set_cam_pan_angle(-30)
    sleep(0.5)
    px.set_cam_pan_angle(30)
    sleep(0.5)
    px.set_cam_pan_angle(0)
    sleep(0.5)
    px.set_cam_tilt_angle(-30)
    sleep(0.5)
    px.set_cam_tilt_angle(30)
    sleep(0.5)
    px.set_cam_tilt_angle(0)
    sleep(0.5)

def servos_move(servo_num, value):
    if servo_num == 0:
        px.set_dir_servo_angle(value)
    elif servo_num == 1:
        px.set_cam_pan_angle(value)
    elif servo_num == 2:
        px.set_cam_tilt_angle(value)
    sleep(0.2)

def set_servos_offset(servo_num, value):
    if servo_num == 0:
        px.dir_cali_val = value
    elif servo_num == 1:
        px.cam_pan_cali_val = value
    elif servo_num == 2:
        px.cam_tilt_cali_val  = value  

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
    step = 0.4
    # step = (180 / 2000) * (20000 / 4095)  # actual precision of steering gear

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
        elif key == 'w' or key == 'd':
            servos_offset[servo_num] += step
            if servos_offset[servo_num] > 20:
                servos_offset[servo_num] =20
            servos_offset[servo_num] = round(servos_offset[servo_num], 2) 
            show_info()
            set_servos_offset(servo_num, servos_offset[servo_num])
            servos_move(servo_num, 0)
        elif key == 's' or key == 'a':
            servos_offset[servo_num] -= step
            if servos_offset[servo_num] < -20:
                servos_offset[servo_num] = -20
            servos_offset[servo_num] = round(servos_offset[servo_num], 2) 
            show_info()
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
                    px.dir_servo_calibrate(servos_offset[0])
                    px.cam_pan_servo_calibrate(servos_offset[1])
                    px.cam_tilt_servo_calibrate(servos_offset[2])
                    px.motor_direction_calibrate(motor_num +1 , motors_offset[motor_num])
                    sleep(0.2)
                    servos_offset = [px.dir_cali_val, px.cam_pan_cali_val, px.cam_tilt_cali_val]
                    show_info()
                    print('The calibration value has been saved.')
                    break
                elif key == 'n':
                    show_info()
                    break   
                sleep(0.01) 

        # quit
        elif key == readchar.key.CTRL_C or key in readchar.key.ESC:
            print('quit')
            break 

        sleep(0.01)


if __name__ == "__main__":
    try:
        cali_helper()
    except KeyboardInterrupt:
        print('quit')
    except Exception as e:
        print(e)
    finally:
        px.stop()
        sleep(0.1)
