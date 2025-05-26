import threading
import time
from picarx.utils import constrain, CameraDetector

class AutoDrive():
    def __init__(self, car):
        self.car = car
        self.thread = None
        self.running = False
        self.power = 50

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

    def __del__(self):
        self.stop()

class ObstacleAvoidance(AutoDrive):
    SAFE_DISTANCE = 30
    DANGER_DISTANCE = 15

    def loop(self):
        distance = self.car.get_distance()
        if distance >= self.SAFE_DISTANCE:
            self.car.set_steering_angle(0)
            self.car.forward(self.power)
        elif distance >= self.DANGER_DISTANCE:
            self.car.set_steering_angle(30)
            self.car.forward(self.power)
            time.sleep(0.1)
        else:
            self.car.set_steering_angle(-30)
            self.car.backward(self.power)
            time.sleep(0.5)

class LineTracking(AutoDrive):
    BIG_TURNING_ANGLE = 30
    SMALL_TURNING_ANGLE = 15

    def __init__(self, car):
        super().__init__(car)
        self.direction = "stop"

    def get_direction(self):
        data = self.car.get_grayscale_data()
        status = self.car.get_line_status(data)
        if status == [0, 0, 0]:
            return 'stop'
        elif status == [0, 1, 0]:
            return 'forward'
        elif status == [1, 0, 0]:
            return 'left'
        elif status == [1, 1, 0]:
            return 'little_left'
        elif status == [0, 0, 1]:
            return 'right'
        elif status == [0, 1, 1]:
            return 'little_right'

    def outHandle(self):
        if self.direction in ['left', 'little_left']:
            self.car.set_steering_angle(30)
            self.car.backward(10)
        elif self.direction in ['right', 'little_right']:
            self.car.set_steering_angle(-30)
            self.car.backward(10)
        while self.running:
            new_direction = self.get_direction()
            if new_direction != self.direction:
                break

    def loop(self):
        direction = self.get_direction()

        if direction != "stop":
            self.direction = direction
        if direction == 'forward':
            self.car.set_steering_angle(0)
            self.car.forward(self.power) 
        elif direction == 'left':
            self.car.set_steering_angle(-self.BIG_TURNING_ANGLE)
            self.car.forward(self.power)
        elif direction == 'little_left':
            self.car.set_steering_angle(-self.SMALL_TURNING_ANGLE)
            self.car.forward(self.power)
        elif direction == 'right':
            self.car.set_steering_angle(self.BIG_TURNING_ANGLE)
            self.car.forward(self.power)
        elif direction == 'little_right':
            self.car.set_steering_angle(self.SMALL_TURNING_ANGLE)
            self.car.forward(self.power)
        else:
            self.outHandle()

class Following(AutoDrive):
    STEP = 0.3

    def __init__(self, car):
        super().__init__(car)
        self.detector = CameraDetector()
        self.camera_pan_angle = 0
        self.camera_tilt_angle = 0
        self.steering_angle = 0

    def set_mode(self, mode):
        self.detector.set_mode(mode)

    def loop(self):
        if self.detector.founded and self.detector.size > 50:
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
    from picarx import PiCarX
    try:
        car = PiCarX()
        auto_drive = ObstacleAvoidance(car)
        auto_drive.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        auto_drive.stop()