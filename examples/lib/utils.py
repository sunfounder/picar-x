# from .ble import BLE
import time
import os
import re
import math
from pin import Pin

mcu_reset = mcu_reset = Pin("MCURST")

def reset_mcu():
    mcu_reset.off()
    time.sleep(0.001)
    mcu_reset.on() 
    time.sleep(0.1)  
# ble = BLE()

# ble.write('NAME+ezb-RPi')
# ble.write('ADVP+') # 0~F

# __PRINT__ = print

# def print(msg, end='\n', tag='[DEBUG]'):
#     _msg = "Ezblock [{}] [DEBUG] {}".format(time.asctime(), msg)
#     os.system("echo {} >> /opt/ezblock/log".format(_msg))
#     msg = '%s %s %s' % (tag, msg, tag)
#     __PRINT__(msg, end=end)
#     ble.write(msg)

def delay(ms):
    time.sleep(ms/1000)

def set_volume(value):
    value = min(100, max(0, value))
    cmd = "sudo amixer -M sset 'PCM' %d%%" % value
    os.system(cmd)

# def set_audio_device(value):
#     if value > 100:
#         value = 100
#     if value < 0:
#         value = 0
#     cmd = "amixer cset numid=3 %d%%" % value
#     os.system(cmd)

def run_command(cmd):
    import subprocess
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    status = p.poll()
    return status, result

def is_installed(cmd):
    status, _ = run_command("%s -v"%cmd)
    # 0 only tested under "espeak -v"
    if status in [0,]:
        return True
    else:
        return False

def ezblock_update():
    files = os.listdir("/home/pi/")
    if "ezb-pi" in files:
        os.chdir("/home/pi/ezb-pi")
        status, error = run_command("git pull origin master")
        if status == 0:
            return True
        else:
            return error
    else:
        os.chdir("/home/pi")
        status, error = run_command("git clone https://github.com/ezblockcode/ezb-pi.git")
        if status == 0:
            return True
        else:
            return error
        os.chdir("/home/pi/ezb-pi")
    status, error = run_command("sudo python3 install.py")
    if status == 0:
        return True
    else:
        return error
    
def mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def getIP(ifaces=['wlan0', 'eth0']):
    if isinstance(ifaces, str):
        ifaces = [ifaces]
    for iface in list(ifaces):
        search_str = 'ip addr show {}'.format(iface)
        result = os.popen(search_str).read()
        com = re.compile(r'(?<=inet )(.*)(?=\/)', re.M)
        ipv4 = re.search(com, result)
        if ipv4:
            ipv4 = ipv4.groups()[0]
            return ipv4
    return False

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 == 1

def is_whole(n):
    return n % 1 == 0

def is_positive(n):
    return n > 0

def is_negative(n):
    return n < 0

def is_divisible_by(a, b):
    return a % b == 0

def is_prime(n):
    # https://en.wikipedia.org/wiki/Primality_test#Naive_methods
    # If n is not a number but a string, try parsing it.
    if not isinstance(n, int):
        try:
            n = float(n)
        except:
            return False
    if n == 2 or n == 3:
        return True
    # False if n is negative, is 1, or not whole, or if n is divisible by 2 or 3.
    if n <= 1 or n % 1 != 0 or n % 2 == 0 or n % 3 == 0:
        return False
    # Check all the numbers of form 6k +/- 1, up to sqrt(n).
    for x in range(6, int(math.sqrt(n)) + 2, 6):
        if n % (x - 1) == 0 or n % (x + 1) == 0:
            return False
    return True

def average_of(myList):
    localList = [e for e in myList if isinstance(e, int)]
    if not localList: return
    return float(sum(localList)) / len(localList)

def median_of(myList):
    localList = sorted([e for e in myList if isinstance(e, int)])
    if not localList: return
    if len(localList) % 2 == 0:
        return (localList[len(localList) // 2 - 1] + localList[len(localList) // 2]) / 2.0
    else:
        return localList[(len(localList) - 1) // 2]

def modes_of(some_list):
    modes = []
    # Using a lists of [item, count] to keep count rather than dict
    # to avoid "unhashable" errors when the counted item is itself a list or dict.
    counts = []
    maxCount = 1
    for item in some_list:
        found = False
        for count in counts:
            if count[0] == item:
                count[1] += 1
                maxCount = max(maxCount, count[1])
                found = True
        if not found:
            counts.append([item, 1])
    for counted_item, item_count in counts:
        if item_count == maxCount:
            modes.append(counted_item)
    return modes

def standard_deviation_of(numbers):
    n = len(numbers)
    if n == 0: return
    mean = float(sum(numbers)) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return math.sqrt(variance)

def constrain(x, low, high):
    return min(max(x, low), high)

def rindex(seq, item, start=None, stop=None):
    """L.rindex(item, [start, [stop]]) -> integer -- return last index of item.
    Raises itemError if the item is not present."""
    start, stop, _ = slice(start, stop).indices(len(seq))
    if stop == 0:
        # start = 0
        raise ValueError('{!r} is not in list'.format(item))
    else:
        stop -= 1
        start = None if start == 0 else start - 1
    return stop - seq[stop:start:-1].index(item)

def pop_random(seq):
    from random import randrange
    return seq.pop(randrange(len(seq)))

def lists_sort(my_list, type, reverse):
    def try_float(s):
      try:
        return float(s)
      except:
        return 0
    key_funcs = {
      "NUMERIC": try_float,
      "TEXT": str,
      "IGNORE_CASE": lambda s: str(s).lower()
    }
    key_func = key_funcs[type]
    list_cpy = list(my_list) # Clone the list.
    return sorted(list_cpy, key=key_func, reverse=reverse)

# if __name__ == "__main__":
#     is_installed("espeak")