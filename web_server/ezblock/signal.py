class Signal(object):
    def __init__(self, Pin, invert=False):
        self.pin = Pin
        self.invert = invert

    def value(self, value=None):
        if value == None:
            if self.invert:
                return self.pin.value()+1&1
            else:
                return self.pin.value()
        else:
            if self.invert:
                self.pin.value(value+1&1)
            else:
                self.pin.value(value)
            return value

    def on(self):
        self.value(1)
        return 1

    def off(self):
        self.value(0)
        return 0
