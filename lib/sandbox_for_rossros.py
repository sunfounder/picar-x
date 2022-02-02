from cProfile import run
from rossros import Producer, Bus, runConcurrently
from ir_sensors_sim import IRSensors
from terminal_monitor import TerminalMonitor
import logging

Logger = logging.getLogger()
Logger.setLevel(level=0)

# Setup shutdown bus
monitor = TerminalMonitor()
shutdown_bus = Bus(initial_message=False, name="ShutdownBus")
shutdown_producer = Producer(
    monitor,
    shutdown_bus,
    delay=0.05,
    termination_busses=(shutdown_bus),
    name="ShutdownProducer"
)

# Setup sensor producer
ir_sensors = IRSensors()
ir_sensors_bus = Bus(initial_message=[0,0,0], name="IRSensorsBus")
ir_sensors_producer = Producer(
    ir_sensors,
    ir_sensors_bus,
    delay=0.1,
    termination_busses=(shutdown_bus),
    name="IRSensorsProducer"
)

runConcurrently([shutdown_producer, ir_sensors_producer])
