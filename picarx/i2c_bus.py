#!/usr/bin/env python3
import threading

from robot_hat.adc import ADC
from robot_hat.i2c import I2C

bus_lock = threading.RLock()

_TRANSFERS = (
    "_write_byte",
    "_write_byte_data",
    "_write_word_data",
    "_write_i2c_block_data",
    "_read_byte",
    "_read_byte_data",
    "_read_word_data",
    "_read_i2c_block_data",
)


def _locked(func):
    def wrapper(self, *args, **kwargs):
        with bus_lock:
            return func(self, *args, **kwargs)

    wrapper._picarx_locked = True
    return wrapper


def install():
    """Serialise the bus transfers made inside this process

    The HAT serves one conversion result at a time: a read first selects a
    channel and then fetches the value, and a motor or servo write coming from
    another thread can land between those two steps. Holding one lock for every
    transfer keeps such a read consistent. Only this process is affected,
    robot_hat itself stays untouched.
    """
    for name in _TRANSFERS:
        func = getattr(I2C, name, None)
        if func is None or getattr(func, "_picarx_locked", False):
            continue
        setattr(I2C, name, _locked(func))


class LockedADC(ADC):
    """
    Analog to digital converter with a consistent channel read

    The channel select and the two result bytes form one logical read, so they
    are taken while holding the bus lock. Any other transfer from this process
    waits until the value has been assembled.
    """

    def read(self):
        """
        Read the ADC value

        :return: ADC value(0-4095)
        :rtype: int
        """
        with bus_lock:
            return super().read()
