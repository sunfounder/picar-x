from ezblock.pin import Pin

class Switch(Pin):
    def __init__(self):
        super().__init__()

    def __call__(self):
        return self.value()

    def value(self):
        return not super().value()

    def callback(self, func=None):
        self.irq(handler=func, trigger=self.FALLING)
