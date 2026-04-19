from picarx import Picarx
from picarx.utils import safe_movement

px = Picarx()


@safe_movement(px)
def move():
    pass
    # while True:
    #     px.forward(30)


if __name__ == "__main__":
    move()