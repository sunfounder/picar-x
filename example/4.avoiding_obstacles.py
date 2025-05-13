from picarx import PiCarX
import time

POWER = 50
SafeDistance = 40   # > 40 safe
DangerDistance = 20 # > 20 && < 40 turn around, 
                    # < 20 backward

def main():
    try:
        px = PiCarX()
       
        while True:
            distance = round(px.ultrasonic.read(), 2)
            print("distance: ",distance)
            if distance >= SafeDistance:
                px.set_steering_angle(0)
                px.forward(POWER)
            elif distance >= DangerDistance:
                px.set_steering_angle(30)
                px.forward(POWER)
                time.sleep(0.1)
            else:
                px.set_steering_angle(-30)
                px.backward(POWER)
                time.sleep(0.5)

    finally:
        px.forward(0)


if __name__ == "__main__":
    main()

