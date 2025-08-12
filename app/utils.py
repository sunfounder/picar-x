
from enum import StrEnum

import time
import threading

class Status(StrEnum):
    """ AI Status """
    NOT_INITIALIZED = "NOT_INITIALIZED"
    INITIALIZING = "INITIALIZING"
    IDLE = "IDLE"
    FAILED = "FAILED"
    LISTENING = "LISTENING" 
    STT = "STT"
    TTS = "TTS"
    THINKING = "THINKING"
    SPEAKING = "SPEAKING"
    DOWNLOADING = "DOWNLOADING"
    DOWNLOADED = "DOWNLOADED"
    SUCCESS = "SUCCESS"

class Timer():
    def __init__(self):
        self.start = None
        self.end = None

    def print(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            # 计算函数运行的间隔
            interval = None
            if self.start is not None:
                interval = start - self.start
                interval = round(interval*1000, 2)
            self.start = start

            result = func(*args, **kwargs)
            self.end = time.time()
            duration = self.end - self.start
            duration = round(duration*1000, 2)
            if interval is None:
                print(f"[{duration:>6}] {func.__name__}")
            else:
                print(f"[{interval:>6}, {duration:>6}] {func.__name__}")
            return result
        return wrapper

class Task():
    def __init__(self):
        self.thread = None
        self.running = False

    def start(self, *args, **kwargs):
        if self.thread is None or not self.thread.is_alive():
            self.thread = threading.Thread(target=self._main, args=args, kwargs=kwargs)
            self.thread.start()
            self.running = True
        else:
            raise Exception("Task is running")

    def stop(self):
        if self.thread is not None and self.thread.is_alive():
            self.thread.join()
            self.running = False
        self.thread = None
        self.running = False

    def main(self, *args, **kwargs):
        pass

    def _main(self, *args, **kwargs):
        self.main(*args, **kwargs)
        self.running = False
        self.thread = None


