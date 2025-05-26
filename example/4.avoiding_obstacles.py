from picarx import PiCarX
import time

POWER = 50
SAFE_DISTANCE = 30
DANGER_DISTANCE = 15

car = PiCarX()

def main():
    while True:
        distance = car.get_distance()
        print("distance: ", distance)
        if distance >= SAFE_DISTANCE:
            car.set_steering_angle(0)
            car.forward(POWER)
        elif distance >= DANGER_DISTANCE:
            print("Obstacle detected! turn right!")
            car.set_steering_angle(30)
            car.forward(POWER)
            time.sleep(0.1)
        else:
            print("Danger!, backward!")
            car.set_steering_angle(-30)
            car.backward(POWER)
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    finally:
        car.forward(0)

