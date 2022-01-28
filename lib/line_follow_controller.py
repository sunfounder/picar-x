from bus import Bus
from drivetrain import DriveTrain
from time import sleep

class LineFollowController(object):
    def __init__(self, low_kp: float = 1.0, high_kp: float = 1.0) -> None:
        # kp is proportional gain constant
        # low kp is for when robot is close to line
        # high kp is for when robot is far from line
        self.low_kp = low_kp
        self.high_kp = high_kp

    def _calculate_steering_angle(self, state: float):
        # State is bounded input from [-1,1]
        # negative indicates line is to the left
        # positive indicates line is to the right
        if abs(state) > 0.7:
            return - self.high_kp * state
        else:
            return - self.low_kp * state

    def continuous_bus_control(self, drivetrain: DriveTrain, state_bus: Bus, shutdown_bus: Bus, time_delay: float):
        while not shutdown_bus.message:
            state = state_bus.read()
            steering_angle = self._calculate_steering_angle(state)
            drivetrain.set_angle(steering_angle)
            drivetrain.set_speed(30)
            sleep(time_delay)
