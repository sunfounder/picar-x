import time

from .picarx import Picarx

def safe_movement(px: Picarx):
    def decorator(f):
        def inner(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            finally:
                print("Stopping & exiting")
                px.stop()
                time.sleep(0.1)
        return inner
    return decorator
