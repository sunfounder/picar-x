from ezblock.pin import Pin
from ezblock.led import LED
from ezblock.pwm import PWM
from ezblock.servo import Servo
from ezblock.signal import Signal
from ezblock.spi import SPI
from ezblock.switch import Switch
from ezblock.uart import UART
from ezblock.i2c import I2C
from ezblock.adc import ADC
from ezblock.ble import BLE
from ezblock.ble import Remote
from ezblock.music import Music
from ezblock.color import Color
from ezblock.camera import Camera
from ezblock.iot import IOT
from ezblock.tts import TTS
from ezblock.irq import IRQ
from ezblock.wifi import WiFi
from ezblock.utils import *
from ezblock.taskmgr import Taskmgr
from ezblock.modules import *
from ezblock.send_email import SendMail
from ezblock.info import Info
from ezblock.rgb_matrix import RGB_Matrix
from ezblock.oled import SSD1306_128_64 as SSD1306
from ezblock.lcd1602_i2c import LCD
from ezblock.serial_sound import Serial_Sound
from ezblock.nrf24 import NRF24
from ezblock.filedb import fileDB

def __reset_mcu__():
    mcurst = Pin("MCURST")
    mcurst.on()
    delay(1)
    mcurst.off()

def __main__():
    import sys
    from ezblock.utils import __PRINT__

    usage = '''
Usage:
    ezblock [option]

Options:
    reset-mcu   Reset MCU on Ezblock
    -h          Show this help text and exit
'''
    option = ""
    if len(sys.argv) <= 1:
        __PRINT__(usage)
        quit()
    elif len(sys.argv) > 1:
        option = sys.argv[1]

    if "-h" == option:
        __PRINT__(usage)
        quit()
    elif option == "reset-mcu":
        __PRINT__("MCU Reset.")
        __reset_mcu__()
    else:
        __PRINT__(usage)
        quit()
    