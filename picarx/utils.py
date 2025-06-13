from robot_hat.utils import reset_mcu
from vilib import Vilib
import os, sys
import subprocess
import json
import time

def mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(value, min_value, max_value):
    return min(max(value, min_value), max_value)

def redirect_error_2_null():
    # https://github.com/spatialaudio/python-sounddevice/issues/11

    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    return old_stderr

def cancel_redirect_error(stderr=None):
    if stderr is None:
        stderr = redirect_error_2_null() # ignore error print to ignore ALSA errors
    os.dup2(stderr, 2)
    os.close(stderr)

def run_command(cmd):
    """
    Run command and return status and output

    :param cmd: command to run
    :type cmd: str
    :return: status, output
    :rtype: tuple
    """
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    return status, result

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
    CLOSE = ["none", "close"]
    FACE = ["face"]
    MODES = COLORS + CLOSE + FACE
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
            if mode in self.FACE:
                Vilib.face_detect_switch(1)
                Vilib.color_detect('none')
            elif mode in self.COLORS:
                Vilib.face_detect_switch(0)
                Vilib.color_detect(mode)
            elif mode in self.CLOSE:
                Vilib.face_detect_switch(0)
                Vilib.color_detect('none')
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

GRAY = '1;30'
RED = '0;31'
GREEN = '0;32'
YELLOW = '0;33'
BLUE = '0;34'
PURPLE = '0;35'
DARK_GREEN = '0;36'
WHITE = '0;37'

def print_color(msg, end='\n', file=sys.stdout, flush=False, color=''):
    print('\033[%sm%s\033[0m'%(color, msg), end=end, file=file, flush=flush)

def gray_print(msg, end='\n', file=sys.stdout, flush=False):
    print_color(msg, end=end, file=file, flush=flush, color=GRAY)

def warn(msg, end='\n', file=sys.stdout, flush=False):
    print_color(msg, end=end, file=file, flush=flush, color=YELLOW)

def error(msg, end='\n', file=sys.stdout, flush=False):
    print_color(msg, end=end, file=file, flush=flush, color=RED)

class Config():
    def __init__(self, config_file):
        self.config_file = config_file
        
        if not os.path.exists(config_file):
            os.system(f'touch {config_file}')
            os.system(f'chown 1000:1000 {config_file}')
        with open(config_file, 'r') as f:
            content = f.read()
            if content == '':
                content = '{}'
            self._config = json.loads(content)

    def get(self, key, default_value=None):
        return self._config.get(key, default_value)

    def set(self, key, value):
        self._config[key] = value
        with open(self.config_file, 'w') as f:
            json.dump(self._config, f, indent=4)

    def delete(self, key):
        if key in self._config:
            del self._config[key]
            with open(self.config_file, 'w') as f:
                json.dump(self._config, f, indent=4)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return key in self._config

    def __iter__(self):
        return iter(self._config)

    def __len__(self):
        return len(self._config)

    def __str__(self):
        return json.dumps(self._config, indent=4)

    def __repr__(self):
        return f'Config({self.config_file})'
    def close(self):
        ''' Close the camera.
        '''
        if self.mode == "face":
            Vilib.face_detect_switch(0)
        elif self.mode in self.COLORS:
            Vilib.color_detect('none')

class LazyReader():
    ''' Lazy reader. Read something in a given interval,
    even if you read it multiple times in a short time.
    For those who don't need to read it too frequently.
    '''
    def __init__(self, read_function, interval=10):
        ''' Initialize the lazy reader.

        Args:
            read_function (function): The function to read.
            interval (int): The interval to read.
        '''
        self.read_function = read_function
        self.interval = interval
        self.value = None
        self.last_read_time = 0

    def read(self):
        ''' Read the value.

        Returns:
            The value.
        '''
        if time.time() - self.last_read_time > self.interval:
            self.value = self.read_function()
            self.last_read_time = time.time()
        return self.value

def print_line_position(position, length: int = 30):
    value = int(position * length)
    left_count = length + value
    right_count = length - value
    print(f"[{' ' * left_count}▓▓{' ' * right_count}]  [{position:.2f}]")
