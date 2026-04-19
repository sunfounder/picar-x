from picarx import Picarx
import time


if __name__ == "__main__":
    try:
        print("Initializing Picar-x...")
        px = Picarx()
        px.forward(30)
        px.set_dir_servo_angle(-30)
        px.set_cam_pan_angle(-30)
        time.sleep(1)
        px.set_dir_servo_angle(30)
        px.set_cam_pan_angle(30)
        time.sleep(1)
        px.backward(30)
        px.set_dir_servo_angle(-30)
        px.set_cam_pan_angle(-30)
        time.sleep(1)
        px.set_dir_servo_angle(30)
        px.set_cam_pan_angle(30)
        time.sleep(1)
    finally:
        print("Stopping & shutting down...")
        px.set_cam_pan_angle(0)
        time.sleep(0.2)
        px.stop()
        px.set_dir_servo_angle(0)
        time.sleep(0.2)
