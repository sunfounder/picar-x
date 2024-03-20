from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        # init picarx
        px = Picarx()

        # test motor
        px.forward(30)
        time.sleep(0.5)
        # test direction servo
        for angle in range(0, 35):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            px.set_dir_servo_angle(angle)
            time.sleep(0.01)
        px.stop()
        time.sleep(1)
        # test cam servos
        for angle in range(0, 35):
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35, 0):
            px.set_cam_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(0, 35):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35,-1):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35, 0):
            px.set_cam_tilt_angle(angle)
            time.sleep(0.01)
    finally:
        px.stop()
        time.sleep(0.2)


