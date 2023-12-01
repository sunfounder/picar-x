from picarx import Picarx
import time

POWER = 50
SafeDistance = 40   # > 30 safe
DangerDistance = 20 # > 20 && < 30 turn around, 
                    # < 20 backward

def main():
    try:
        px = Picarx()
        # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
       
        while True:
            distance = round(px.ultrasonic.read(), 2)
            print("distance: ",distance)
            if distance >= SafeDistance:
                px.set_dir_servo_angle(0)
                px.forward(POWER)
            elif distance >= DangerDistance:
                px.set_dir_servo_angle(40)
                px.forward(POWER)
                time.sleep(0.1)
            else:
                px.set_dir_servo_angle(-40)
                px.backward(POWER)
                time.sleep(0.5)

    finally:
        px.forward(0)


if __name__ == "__main__":
    main()

