from ezblock.basic import _Basic_class
import RPi.GPIO as GPIO

class IRQ(_Basic_class):
    IRQ_FALLING = GPIO.FALLING
    IRQ_RISING = GPIO.RISING
    IRQ_RISING_FALLING = GPIO.BOTH

    def __init__(self, pin, trigger, callback):
        super().__init__()
        self.pin = pin
        self.trigger = trigger
        self.callback = callback
        self.pin.mode(self.pin.IN)
        GPIO.add_event_detect(self.pin._pin, trigger, callback=callback)

    def disable(self):
        # Disable the interrupt associated with the ExtInt object. This could be useful for debouncing.
        pass

    def enable(self):
        # Enable a disabled interrupt.
        pass

    def line(self):
        # Return the line number that the pin is mapped to.
        pass

    def swint(self):
        # Trigger the callback from software.
        self.callback()
