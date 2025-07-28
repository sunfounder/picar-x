
from picarx.picarx import PiCarX

car = PiCarX()

def print_position(position, data, length: int = 30):
    value = int(position * length)
    left_count = length + value
    right_count = length - value
    print(f"{'-' * left_count}#{'-' * right_count}  {position:.2f}, {data}")
    
def loop():
    data = car.get_grayscale_data()
    # print(f"{data}")
    if car.is_on_cliff(data=data):
        print(f"!! Cliff !! ({data})")
    elif car.is_on_line(data=data):
        position = car.get_line_position(data=data)
        print_position(position, data)
        steering_angle = position * 30
        car.set_steering_angle(steering_angle)
    else:
        print(f"Lost line ({data})")


if __name__ == "__main__":
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        car.stop()
