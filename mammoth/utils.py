
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

def constrain(value, min_value, max_value):
    return min(max(value, min_value), max_value)


def clear_terminal():
    """清除终端内容"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_at_fixed_position(text, line=1, column=1):
    import os
    """在终端的固定位置打印文本"""
    if os.name == 'nt':  # Windows系统
        print(f"\033[{line};{column}H{text}")
    else:  # Linux/Mac系统
        print(f"\033[{line};{column}f{text}")
