from picarx.picarx import PiCarX
from time import sleep

# init picarx
car = PiCarX()

def main():

    # test motor
    print("Go forward")
    car.forward(30)
    sleep(2)

    print("Sweep steering servos to right")
    for angle in range(0, 30):
        print(angle)
        car.set_steering_angle(angle)
        print("set_steering_angle Done")
        sleep(0.01)
    sleep(2)

    print("Sweep steering servos to left")
    for angle in range(30, -30, -1):
        car.set_steering_angle(angle)
        sleep(0.01)
    sleep(2)

    print("Sweep steering servos back to center")
    for angle in range(-30, 0):
        car.set_steering_angle(angle)
        sleep(0.01)
    
    print("Stop")
    car.stop()
    sleep(2)

    # test cam servos
    print("Sweep camera pan servo right")
    for angle in range(0, 180):
        car.set_camera_pan_angle(angle)
        sleep(0.01)
    sleep(2)

    print("Sweep camera pan servo left")
    for angle in range(180, -180, -1):
        car.set_camera_pan_angle(angle)
        sleep(0.01)
    sleep(2)

    print("Sweep camera pan servo back to center")
    for angle in range(-180, 0):
        car.set_camera_pan_angle(angle)
        sleep(0.01)

    print("Sweep camera tilt servo up")
    for angle in range(0, 30):
        car.set_camera_tilt_angle(angle)
        sleep(0.01)
    sleep(2)

    print("Sweep camera tilt servo down")
    for angle in range(30, -25, -1):
        car.set_camera_tilt_angle(angle)
        sleep(0.01)
    sleep(2)

    print("Sweep camera tilt servo back to center")   
    for angle in range(-25, 0):
        car.set_camera_tilt_angle(angle)
        sleep(0.01)

    print("Finished")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        car.reset()
        print("Stop and exit")
        sleep(0.1)



