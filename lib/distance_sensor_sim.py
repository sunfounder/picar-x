import time

class DistanceSensor(object):
    def __init__(self) -> None:
        pass

    def _read(self)->float:
        time.sleep(0.02)
        return 10.0

    def __call__(self) -> float:
        return self._read()
