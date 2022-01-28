from email import message
from readerwriterlock import rwlock

class Bus():
    def __init__(self, message)->None:
        self.lock = rwlock.RWLockWriteD()
        self.message = message

    def read(self):
        with self.lock.gen_rlock():
            message = self.message
        return message

    def write(self, message)->None:
        with self.lock.gen_wlock():
            self.message = message
        return None
