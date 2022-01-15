""" How to setup and use logging """
import logging

# These lines setup the basic logging format
logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO,
    datefmt="%H:%M:%S")

# This sets the logging level to DEBUG so all DEBUG level messages are printed
logging.getLogger().setLevel(logging.DEBUG)

# This logs a message
variable = 10
message = f"Variable is set to {variable}"
logging.debug(message)

""" How to setup and use logging decorators """
from logdecorator import log_on_start, log_on_end, log_on_error

@log_on_start(logging.DEBUG, "Input: {input} | Message when function starts")
@log_on_error(logging.DEBUG, "Message when function encounters an error before completing")
@log_on_end(logging.DEBUG, "Result {result!r} | Message when function ends successfully")
def myfunc(input = 5):
    return input*2

myfunc()