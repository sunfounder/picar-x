from picarx import PiCarX
import time

car = PiCarX()

while True:
    
    time_start = time.time()
    distance = car.get_distance()
    during = time.time() - time_start
    during = round(during, 3)
    print(f"Distance: {distance} cm, during: {during} sec")
    time.sleep(0.1)