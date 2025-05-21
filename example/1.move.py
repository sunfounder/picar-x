from picarx import PiCarX
import time


if __name__ == "__main__":
    try:
        # init picarx
        car = PiCarX()

        # test motor
        car.forward(30)
        time.sleep(0.5)
        # test direction servo
        for angle in range(0, 35):
            car.set_steering_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            car.set_steering_angle(angle)
            time.sleep(0.01)
        for angle in range(-35, 0):
            car.set_steering_angle(angle)
            time.sleep(0.01)
        car.stop()
        time.sleep(1)
        # test cam servos
        for angle in range(0, 35):
            car.set_camera_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35, -1):
            car.set_camera_pan_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35, 0):
            car.set_camera_pan_angle(angle)
            time.sleep(0.01)
        for angle in range(0, 35):
            car.set_camera_tilt_angle(angle)
            time.sleep(0.01)
        for angle in range(35, -35,-1):
            car.set_camera_tilt_angle(angle)
            time.sleep(0.01)        
        for angle in range(-35, 0):
            car.set_camera_tilt_angle(angle)
            time.sleep(0.01)
    finally:
        car.stop()
        time.sleep(0.2)


