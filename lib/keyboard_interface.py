""" Provide keyboard interface for basic maneuvers """

from time import sleep
import logging
import sys
from termios import tcflush, TCIFLUSH
from picarx_improved import Picarx
from maneuvering import LEFT, RIGHT, k_turn, parallel_park, move

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO,
    datefmt="%H:%M:%S")

def parse_angle(input_str: str)->int:
    if len(input_str.split(" ")) == 2 and input_str.split(" ")[1].isdecimal():
        angle = int(input_str.split(" ")[1])
    else:
        angle = 0
    return angle

def main()->None:
    print(
        "=========================================================\n"\
        "Starting up keyboard interface for Picar-x\n"\
        "This interface accepts the following commands:\n"\
        "left k turn | right k turn | left park | right park\n"\
        "forward | forward [angle] | backward | backward [angle]\n"\
        "shutdown\n"\
        "=========================================================")
    # Setup picar
    px = Picarx()
    # Take user input until receiving shutdown command
    user_input = ""
    while user_input != "shutdown":
        # Flush any extraneous keyboard input 
        tcflush(sys.stdin, TCIFLUSH)
        # Take in command as user_input
        user_input = input("\nInput: ")
        # Parse input and take appropriate action
        if user_input == "left k turn":
            logging.info("K turning left.")
            k_turn(px, LEFT)
        elif user_input == "right k turn":
            logging.info("K turning right.")
            k_turn(px, RIGHT)
        elif user_input == "left park":
            logging.info("Parallel parking left.")
            parallel_park(px, LEFT)
        elif user_input == "right park":
            logging.info("Parallel parking right.")
            parallel_park(px, RIGHT)
        elif user_input.split(" ")[0] == "forward" or user_input == "forward":
            angle = parse_angle(user_input)
            if angle == 0:
                logging.info(f"Moving forward.")
            else:
                logging.info(f"Moving forward with angle {angle}")
            move(px, 50, angle)
            sleep(2)
            move(px, 0, 0)
        elif user_input.split(" ")[0] == "backward" or user_input == "backward":
            angle = parse_angle(user_input)
            if angle == 0:
                logging.info(f"Moving backward")
            else:
                logging.info(f"Moving backward with angle {angle}")
            move(px, -50, angle)
            sleep(2)
            move(px, 0, 0)
        elif user_input == "shutdown":
            logging.info(f"Shutting down.")
        else:
            logging.warning(f"\"{user_input}\" is not valid input.")

if __name__ == "__main__":
    main()