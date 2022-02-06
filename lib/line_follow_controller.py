from time import sleep
from bus import Bus # custom Bus class, not from rossros
from drivetrain_sim import DriveTrain
# No DriveTrain object should be instantiated in this script
# Drivetrain object is only here for typehints

class LineFollowController(object):
    def __init__(self, low_kp: float = 1.0, high_kp: float = 1.0, drivetrain = DriveTrain) -> None:
        # kp is proportional gain constant
        # low kp is for when robot is close to line
        # high kp is for when robot is far from line
        self.low_kp = low_kp
        self.high_kp = high_kp
        self.drivetrain = drivetrain

    def _calculate_steering_angle(self, state: float):
        """Calculate steering angle to follow line"""
        # State is bounded input from [-1,1]
        # negative indicates line is to the left
        # positive indicates line is to the right
        if abs(state) > 0.7:
            return - self.high_kp * state
        else:
            return - self.low_kp * state

    def update_steering_angle(self, state: float)->None:
        """Calculates steering angle for line following
        AND directly comamnds steering servo to calculated angle"""
        angle = self._calculate_steering_angle(state)
        self.drivetrain.set_angle(angle)

    def continuous_bus_control(self, state_bus: Bus, shutdown_bus: Bus, time_delay: float):
        while not shutdown_bus.message:
            state = state_bus.read()
            steering_angle = self._calculate_steering_angle(state)
            self.drivetrain.set_angle(steering_angle)
            sleep(time_delay)

    def __call__(self, state: float)->None:
        return self.update_steering_angle(state)
