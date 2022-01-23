class LineFollowController(object):
    def __init__(self, low_kp: float = 1.0, high_kp: float = 1.0) -> None:
        # kp is proportional gain constant
        # low kp is for when robot is close to line
        # high kp is for when robot is far from line
        self.low_kp = low_kp
        self.high_kp = high_kp

    def calculate_steering_angle(self, state: float):
        # State is bounded input from [-1,1]
        # negative indicates line is to the left
        # positive indicates line is to the right
        if abs(state) > 0.7:
            return - self.high_kp * state
        else:
            return - self.low_kp * state
