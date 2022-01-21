import logging

class DriveTrain(object):
    def __init__(self, config_file) -> None:
        # Grab config file
        self.config_file = config_file
        # Setup steering servo
        self.steer_cal_value = int(self.config_file.get("picarx_steer_servo", default_value=0))
        logging.info(f"self.steer_cal_value: {self.steer_cal_value}")
        # Setup variables for tracking angle and speed
        self.steer_current_angle = 0
        self.current_speed = 0

    def stop(self)->None:
        pass

    def set_angle(self, angle: int)->None:
        # Enforce angle boundaries
        max_angle = 30
        if angle > max_angle:
            logging.warning(f"Requested steering angle ({angle}) greater than max angle ({max_angle}). Setting steering angle to max angle.")
            angle = max_angle
        elif angle < -max_angle:
            logging.warning(f"Requested steering angle ({angle}) lower than min angle ({max_angle}). Setting steering angle to min angle.")
            angle = -max_angle

        # Save steering command
        self.steer_current_angle = angle

    def set_speed(self, speed: int)->None:
        # Enforce speed boundaries
        max_speed = 100
        if speed > max_speed:
            logging.warning(f"Requested speed ({speed}) greater than max speed ({max_speed}). Set speed to max speed.")
            speed = max_speed
        elif speed < -max_speed:
            logging.warning(f"Requested speed ({speed}) lower than min speed ({-max_speed}). Set speed to min speed.")
            speed = -max_speed

        # Save speed command
        self.current_speed = speed
