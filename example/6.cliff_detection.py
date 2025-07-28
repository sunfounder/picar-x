'''
    Cliff detection program for Picar-X:

    Pay attention to modify the reference value of the grayscale module 
    according to the practical usage scenarios.
    Auto calibrate grayscale values:
        Please run ./calibration/grayscale_calibration.py
    Manual modification:
        Use the tracking: 
            car.set_cliff_reference([200, 200, 200])
        The reference value be close to the middle of the line gray value
        and the background gray value.

'''
from picarx.picarx import PiCarX, TTS
from time import sleep

tts = TTS()
tts.lang("en-US")

car = PiCarX()
# manual modify reference value
car.set_cliff_reference([200, 200, 200])

current_state = None
px_power = 10
offset = 20
last_state = "safe"

def main():
    while True:

        if car.is_on_cliff():
            state = "danger"   
            car.backward(80)
            if last_state == "safe":
                print("Danger!")
                tts.say("danger")
                sleep(0.1)
        else:
            state = "safe"
            car.stop()
        last_state = state


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        car.stop()
        print("Stop and exit")
        sleep(0.1)


                