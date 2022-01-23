class LineFollowController(object):
    def __init__(self, kp: float = 1.0) -> None:
        # kp is proportional gain constant
        self.kp = kp

    def calculate_steering_angle(self, state: float):
        # State is bounded input from [-1,1]
        # negative indicates line is to the left
        # positive indicates line is to the right
        return - self.kp * state
