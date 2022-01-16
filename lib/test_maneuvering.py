import unittest
import time
import logging
from picarx_improved import Picarx
from maneuvering import k_turn, move, parallel_park, LEFT, RIGHT

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
    
    def test_parking_left(self)->None:
        px = Picarx()
        parallel_park(px, LEFT)
    
    def test_parking_right(self)->None:
        px = Picarx()
        parallel_park(px, RIGHT)

    def test_parking_both(self)->None:
        px = Picarx()
        parallel_park(px, LEFT)
        time.sleep(2)
        parallel_park(px, RIGHT)
    
    def test_k_turn_left(self)->None:
        px = Picarx()
        k_turn(px, LEFT)

if __name__ == "__main__":
    unittest.main()
