class Bus():
    def __init__(self, message)->None:
        self.message = message

    def read(self):
        return self.message

    def write(self, message)->None:
        self.message = message
        return None
