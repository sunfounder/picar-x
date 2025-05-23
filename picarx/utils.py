from robot_hat.utils import reset_mcu
from vilib import Vilib
from threading import Lock

# Robot Hat read ADC with I2C, set PWM also use I2C,
# and set and update is not in the same thread, so we need
# a io_lock to prevent the conflict.
ROBOT_HAT_I2C_LOCK = Lock()

def with_robot_hat_i2c_lock(func):
    def wrapper(*args, **kwargs):
        with ROBOT_HAT_I2C_LOCK:
            return func(*args, **kwargs)
    return wrapper

def constrain(value, min_value, max_value):
    return min(max(value, min_value), max_value)

def redirect_error_2_null():
    import os, sys
    # https://github.com/spatialaudio/python-sounddevice/issues/11

    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    return old_stderr

def cancel_redirect_error(stderr=None):
    import os
    if stderr is None:
        stderr = redirect_error_2_null() # ignore error print to ignore ALSA errors
    os.dup2(stderr, 2)
    os.close(stderr)


def volume_gain(input_file, output_file, gain):
    import sox

    try:
        transform = sox.Transformer()
        transform.vol(gain)

        transform.build(input_file, output_file)

        return True
    except Exception as e:
        print(f"[ERROR] volume_gain err: {e}")
        return False


class CameraDetector():
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    MODES = ["face"] + COLORS
    EMPTY_RESULT = {
        'n': 0,
        'x': 0,
        'y': 0,
        'w': 0,
        'h': 0,
    }

    def __init__(self):
        self.mode = None

    def set_mode(self, mode):
        ''' Set the detection mode.
        
        Args:
            mode (str): The detection mode. Can be "face" or one of the colors.
        '''
        if mode not in self.MODES:
            raise ValueError("Invalid mode")
        if self.mode != mode:
            if mode == "face":
                Vilib.face_detect_switch(1)
                Vilib.color_detect('none')
            elif mode in self.COLORS:
                Vilib.face_detect_switch(0)
                Vilib.color_detect(mode)
            self.mode = mode

    @property
    def detect_result(self):
        ''' Get the detection result.
        
        Returns:
            dict: The detection result. The keys are "n", "x", "y", "w", "h". The values are the number of objects, the x, y, width and height of the objects.
        '''
        if self.mode == "face":
            return Vilib.face_obj_parameter
        elif self.mode in self.COLORS:
            return Vilib.color_obj_parameter
        else:
            return self.EMPTY_RESULT

    @property
    def size(self):
        ''' Get the size of the object.
        
        Returns:
            int: The size of the object.
        '''
        return int(self.detect_result['w'])

    @property
    def position(self):
        ''' Get the position of the object relative to the center of the camera.
        
        Returns:
            tuple: The position of the object. The first element is the x coordinate, the second element is the y coordinate. The coordinates are in the range of [-1, 1]. The center of the camera is (0, 0). The x coordinate is positive to the right, the y coordinate is positive to the bottom.
        '''
        x = int(self.detect_result['x'])
        y = int(self.detect_result['y'])
        camera_width = Vilib.camera_width
        camera_height = Vilib.camera_height
        x -= camera_width / 2
        y -= camera_height / 2
        x = round(x, 2)
        y = -round(y, 2)
        return (x, y)

    @property
    def direction(self):
        ''' Get the direction of the object relative to the center of the camera.
        
        Returns:
            tuple: The direction of the object. The first element is the x direction, the second element is the y direction. The directions are in the range of [-1, 1]. The center of the camera is (0, 0). The x direction is positive to the right, the y direction is positive to the bottom.
        '''
        x_direction = 0
        y_direction = 0
        horizontal_margin = Vilib.camera_width / 3 / 2
        vertical_margin = Vilib.camera_height / 3 / 2
        x, y = self.position
        if x < -horizontal_margin:
            x_direction = -1
        elif x > horizontal_margin:
            x_direction = 1
        if y < -vertical_margin:
            y_direction = -1
        elif y > vertical_margin:
            y_direction = 1
        return (x_direction, y_direction)


    @property
    def founded(self):
        ''' Check if the object is founded.

        Returns:
            bool: True if the object is founded, False otherwise.
        '''
        return int(self.detect_result['n']) > 0

    def close(self):
        ''' Close the camera.
        '''
        if self.mode == "face":
            Vilib.face_detect_switch(0)
        elif self.mode in self.COLORS:
            Vilib.color_detect('none')
