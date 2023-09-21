from picarx import Picarx
import time
import threading
import readchar 
import os

px = Picarx()
config_path = px.CONFIG

manual = f'''\
        ┌────────────────────────────────────┐
        │ Picar-X Grayscale Module Reference │
        │       Calibration Helper           │
        └────────────────────────────────────┘
 config_file: {config_path}

 press [Q] to start line reference calibration,
 press [E] to start cliff reference calibration

 [SPACE]: confirm calibration           [Crtl+C]: quit
'''

current_grayscale_value = [0, 0, 0]
line_reference = px.line_reference
cliff_reference = px.cliff_reference
current_mode = None
thresholds = [
    [4096, 0], # min, max
    [4096, 0],
    [4096, 0],
]
line_min = [
    4096,
    4096,
    4096,
]

run_flag = False
cali_status = 'none' # none, work, done
_lock = threading.Lock()
key = ''

# print control
# ==========================================
def clear_line_and_print(msg, color=''):
    print(f'\033[K\033[{color}m{msg}\033[m')

def noecho():
    os.system("stty -echo")

def echo():
    os.system("stty echo")

def disable_cursor():
    print("\033[?25l", end='', flush=True)

def enable_cursor():
    print("\033[?25h", end='', flush=True)

# test direc servo
# ==========================================
px.set_dir_servo_angle(-30)
time.sleep(0.5)
px.set_dir_servo_angle(30)
time.sleep(0.5)
px.set_dir_servo_angle(0)
time.sleep(0.5)

# read grayscale value thread
# ==========================================
def read_data_loop():
    global current_grayscale_value, thresholds, run_flag, cali_status

    while run_flag:
        try:
            current_grayscale_value = px.get_grayscale_data()

            # calculate the reference
            if cali_status == 'work':
                for i in range(3):
                    if current_grayscale_value[i] < thresholds[i][0]:
                        thresholds[i][0] = current_grayscale_value[i]
                    if current_grayscale_value[i] > thresholds[i][1]:
                        thresholds[i][1] = current_grayscale_value[i]
                    line_reference[i] = int((thresholds[i][0] + thresholds[i][1])/2)
            if cali_status == 'done':
                if (cliff_reference[0] < line_reference[0]) and (cliff_reference[1] < line_reference[1]) and (cliff_reference[2] < line_reference[2]):
                    cliff_reference[0] = int((cliff_reference[0] + line_reference[0]) / 2)
                    cliff_reference[1] = int((cliff_reference[1] + line_reference[1]) / 2)
                    cliff_reference[2] = int((cliff_reference[2] + line_reference[2]) / 2)
                cali_status = 'none'

        except Exception as e:
            run_flag = False
            print(f'\033[31mread_data_loop error: {e}\033[m')
        time.sleep(0.2)

# read key thread
# ==========================================
def read_key_loop():
    global key, run_flag
    while run_flag:
        try:
            key = readchar.readkey()
            time.sleep(0.25)
        except KeyboardInterrupt:
            run_flag = False
            print('quit')
#
def update_info(isback=True):
    if isback:
        print("\033[6A", end='\r') # moves cursor up 6 lines

    if current_mode == None:
        clear_line_and_print(' ---------- ', color='32' )
    elif current_mode == 'line_cali':
        clear_line_and_print("Line reference auto calibrating ...", color='33')
    elif current_mode == 'line_cali_done':
        clear_line_and_print("Line reference auto calibration done.", color='32')
    elif current_mode == 'cliff_cali':
        clear_line_and_print("Cliff reference auto calibrating ...", color='33')
    elif current_mode == 'cliff_cali_done':
        clear_line_and_print("Cliff reference auto calibration done.", color='32')
    elif current_mode == 'saved':
        clear_line_and_print("The reference values has been saved.", color='32')

    _is_val_error = False
    if cali_status == 'none':
        for i in range(3):
            if line_reference[i] < cliff_reference[i]:
                _is_val_error = True
                break
    if _is_val_error:
        clear_line_and_print("Note that cliff reference values shou be less than line reference values.", color='31')
    else:
        clear_line_and_print("")

    clear_line_and_print(f'current value: {current_grayscale_value}')
    clear_line_and_print(f'thresholds: {thresholds}')
    clear_line_and_print(f'line reference: {line_reference}')
    clear_line_and_print(f'cliff reference: {cliff_reference}')


# line reference calibration
# =================================================================
def start_line_calibrate():
    def line_calibrate_work():
        global current_mode, cali_status, thresholds
        current_mode = 'line_cali'
        cali_status = 'work'
        # reset thresholds
        thresholds = [
            [4096, 0], # min, max
            [4096, 0],
            [4096, 0],
        ]
        _angle = 35
        _delay = 0.8
        # front left
        px.set_dir_servo_angle(-_angle)
        px.forward(10)
        time.sleep(_delay)
        # back left
        px.backward(10)
        time.sleep(_delay)
        # stop
        px.set_dir_servo_angle(0)
        px.stop()
        time.sleep(0.2)
        # front right
        px.set_dir_servo_angle(_angle)
        px.forward(10)
        time.sleep(_delay)
        # back right
        px.backward(10)
        time.sleep(_delay)
        # stop
        px.set_dir_servo_angle(0)
        px.stop()
        time.sleep(0.2)
        current_mode = 'line_cali_done'
        cali_status = 'done'
    line_calibrate_thread = threading.Thread(target=line_calibrate_work)
    line_calibrate_thread.daemon = True
    line_calibrate_thread.start()

# cliff reference calibration
def start_cliff_calibrate():
    def cliff_calibrate_work():
        global current_mode, cliff_reference, thresholds
        current_mode = 'cliff_cali'
        count = 0
        _left_val = 0
        _mid_val = 0
        _right_val = 0

        while True:
            _left_val += current_grayscale_value[0]
            _mid_val += current_grayscale_value[1]
            _right_val += current_grayscale_value[2]
            if count >= 10:
                break
            else:
                count += 1
            time.sleep(0.2)

        _left_val /= 10
        _mid_val /= 10
        _right_val /= 10

        if _left_val < thresholds[0][0] and _mid_val < thresholds[1][0] and _right_val < thresholds[2][0]:
            _left_val = int((_left_val + thresholds[0][0]) / 2)
            _mid_val = int((_mid_val + thresholds[1][0]) / 2)
            _right_val = int((_right_val + thresholds[2][0]) / 2)
        cliff_reference = [int(_left_val), int(_mid_val), int(_right_val)]
        current_mode = 'cliff_cali_done'

    cliff_calibrate_thread = threading.Thread(target=cliff_calibrate_work)
    cliff_calibrate_thread.daemon = True
    cliff_calibrate_thread.start()


def main():
    global key, current_mode, run_flag
    # start read data thread
    run_flag = True
    _read_data_thead = threading.Thread(target=read_data_loop)
    _read_data_thead.daemon = True
    _read_data_thead.start()
    # start read key thread
    _read_key_thead = threading.Thread(target=read_key_loop)
    _read_key_thead.daemon = True
    _read_key_thead.start()
    #
    noecho()
    disable_cursor()
    print(manual)
    update_info(False)
    while run_flag:
        key = key.lower()
        if key == 'q':
            current_mode = 'line_cali'
            start_line_calibrate()
        elif key == 'e':
            current_mode = 'cliff_cali'
            start_cliff_calibrate()
        elif key == readchar.key.SPACE:
            print('\033[32mConfirm save ?(y/n)\033[m')
            while True:
                key = key.lower()
                if key == 'y':
                    px.set_line_reference(line_reference)
                    px.set_cliff_reference(cliff_reference)
                    current_mode = 'saved'
                    print("\033[1A\033[J", end='\r')
                    break
                elif key == 'n':
                    current_mode = None
                    print("\033[1A\033[J", end='\r')
                    break
                time.sleep(0.05)
        # update print
        update_info()
        # reset key
        key = ''

        time.sleep(0.2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('quit')
    except Exception as e:
        print(e)
    finally:
        # enable echo
        echo()
        # enable cursor
        enable_cursor()
        # stop
        px.stop()
        time.sleep(0.1)
