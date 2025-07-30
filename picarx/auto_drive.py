import threading
import time
from picarx.utils import constrain, CameraDetector

import logging

class AutoDrive():
    def __init__(self, car, log=None):
        self.car = car
        self.thread = None
        self.running = False
        self.power = 50
        self.log = log or logging.getLogger(__name__)

    def set_power(self, power):
        power = constrain(power, 0, 100)
        self.power = power

    def loop(self):
        pass

    def run(self):
        self.running = True
        while self.running:
            self.loop()
        self.thread = None

    def start(self):
        if self.thread is not None:
            return
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()
            self.thread = None
        self.car.stop()

class ObstacleAvoidance(AutoDrive):
    SAFE_DISTANCE = 30
    DANGER_DISTANCE = 15

    def loop(self):
        distance = self.car.get_distance()
        if distance >= self.SAFE_DISTANCE:
            self.log.debug("[ObstacleAvoidance] safe distance")
            self.car.set_steering_angle(0)
            self.car.forward(self.power)
        elif distance >= self.DANGER_DISTANCE:
            self.log.debug("[ObstacleAvoidance] danger distance")
            self.car.set_steering_angle(30)
            self.car.forward(self.power)
            time.sleep(0.1)
        else:
            self.log.debug("[ObstacleAvoidance] too close")
            self.car.set_steering_angle(-30)
            self.car.backward(self.power)
            time.sleep(0.5)

class LineTracking(AutoDrive):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = 0

    def loop(self):
        data = self.car.get_grayscale_data()

        if self.car.is_on_line(data=data):
            self.log.debug("[LineTracking] on line")
            position = self.car.get_line_position(data=data)
            self.log.debug(f"[LineTracking] position: {position}")
            steering_angle = position * 30
            self.car.set_steering_angle(steering_angle)
            self.car.forward(self.power)
            self.position = position
        else:
            self.log.debug("[LineTracking] off line")
            if self.position < 0:
                self.log.debug("[LineTracking] turn right")
                self.car.set_steering_angle(30)
                self.car.backward(10)
            else:
                self.log.debug("[LineTracking] turn left")
                self.car.set_steering_angle(-30)
                self.car.backward(10)
            while self.running:
                if self.car.is_on_line():
                    break

class Following(AutoDrive):
    STEP = 0.3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.detector = CameraDetector()
        self.camera_pan_angle = 0
        self.camera_tilt_angle = 0
        self.steering_angle = 0

    def set_mode(self, mode):
        self.detector.set_mode(mode)

    def loop(self):
        if self.detector.founded and self.detector.size > 50:
            self.log.debug(f"[Following] founded: {self.detector.founded}, size: {self.detector.size}, direction: {self.detector.direction}")
            x, y = self.detector.direction
            self.steering_angle += x * self.STEP
            self.camera_pan_angle += x * self.STEP
            self.camera_tilt_angle += y * self.STEP
            self.steering_angle = constrain(self.steering_angle, -30, 30)
            self.camera_pan_angle = constrain(self.camera_pan_angle, -90, 90)
            self.camera_tilt_angle = constrain(self.camera_tilt_angle, -90, 90)
            self.car.set_steering_angle(self.steering_angle)
            self.car.set_camera_pan_angle(self.camera_pan_angle)
            self.car.set_camera_tilt_angle(self.camera_tilt_angle)
            self.car.forward(self.power)
        else:
            self.car.stop()
    
    def stop(self):
        super().stop()
        self.detector.close()

if __name__ == "__main__":
    from picarx.picarx import PiCarX
    try:
        car = PiCarX()
        auto_drive = ObstacleAvoidance(car)
        auto_drive.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        auto_drive.stop()