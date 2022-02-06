from drivetrain_sim import DriveTrain
# No DriveTrain object should be instantiated in this script
# Drivetrain object is only here for typehints

class DistanceController(object):
    def __init__(self, stop_distance: float, drivetrain: DriveTrain) -> None:
        # Stop at any distance less than stop_distance
        self.stop_distance = stop_distance
        self.drivetrain = drivetrain

    def _calculate_speed(self, distance:float):
        # A distance reading < 0 indicates nothing was detected
        if distance >= 0 and distance < self.stop_distance:
            return 0
        else:
            return 30

    def update_speed(self, distance: float):
        """Directly update motor speed"""
        speed = self._calculate_speed(distance)
        self.drivetrain.set_speed(speed)

    def __call__(self, distance: float) -> None:
        return self.update_speed(distance)
