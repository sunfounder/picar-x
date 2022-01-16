import unittest
import time
import logging
from picarx_improved import Picarx
from maneuvering import move

# Setup logging format
logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO,
    datefmt="%H:%M:%S")

class TestManeuvering(unittest.TestCase):
    def test_move(self)->None:
        px = Picarx()

        move(px, 100, 30)
        logging.info("Move forward right")
        time.sleep(5)

        move(px, 100, -30)
        logging.info("Move forward left")
        time.sleep(5)

        move(px, -100, 30)
        logging.info("Move backward right")
        time.sleep(5)

        move(px, -100, -30)
        logging.info("Move backward left")
        time.sleep(5)

        move(px, 10, 0)
        logging.info("Move forward straight")
        time.sleep(5)

        move(px, 2000, -200)
        logging.info("Move forward left with out of bounds values")
        time.sleep(5)


if __name__ == "__main__":
    unittest.main()