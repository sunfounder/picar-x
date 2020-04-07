import spidev
class SPI(object):
    def __init__(self, bus, device):
        spi = spidev.SPiDev()
        spi.open(bus, device)
