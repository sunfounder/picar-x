from picarx import PiCarX
from picarx.utils import constrain
from time import sleep
from vilib import Vilib

car = PiCarX()

def main():
    Vilib.camera_start()
    Vilib.display()
    Vilib.color_detect("red")
    speed = 50
    dir_angle=0
    x_angle =0
    y_angle =0
    while True:
        if Vilib.detect_obj_parameter['color_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['color_x']
            coordinate_y = Vilib.detect_obj_parameter['color_y']
            
            # change the pan-tilt angle for track the object
            x_angle +=(coordinate_x*10/640)-5
            x_angle = constrain(x_angle,-35,35)
            car.set_camera_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = constrain(y_angle,-35,35)
            car.set_camera_tilt_angle(y_angle)

            # move
            # The movement direction will change slower than the pan/tilt direction 
            # change to avoid confusion when the picture changes at high speed.
            if dir_angle > x_angle:
                dir_angle -= 1
            elif dir_angle < x_angle:
                dir_angle += 1
            car.set_steering_angle(x_angle)
            car.forward(speed)
            sleep(0.05)

        else :
            car.forward(0)
            sleep(0.05)


if __name__ == "__main__":
    try:
       main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")    
    finally:
        car.reset()
        Vilib.camera_close()
        print("Stop and exit")
        sleep(0.1)
