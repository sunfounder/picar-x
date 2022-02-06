import logging
from rossros import Producer, ConsumerProducer, Consumer, Bus, Timer, runConcurrently
from picarx_improved import Picarx
from line_interpreter import DARKLINE, LineInterpreter
from line_follow_controller import LineFollowController
from terminal_monitor import TerminalMonitor

Logger = logging.getLogger()
Logger.setLevel(level=0)

def main():
    # Setup picar and line following classes
    px = Picarx()
    interpreter = LineInterpreter(sensitivity_threshold=100, polarity=DARKLINE)
    line_follow_controller = LineFollowController(low_kp=10.0, high_kp=50.0, drivetrain=px.drivetrain)
    # Setup terminal for easy shutdown
    terminal = TerminalMonitor()

    # Setup busses
    keyboard_termination_bus = Bus(initial_message=False, name="KeyboardBus")
    timer_bus = Bus(initial_message=False, name="TimerBus")
    ir_sensors_bus = Bus(initial_message=[0,0,0], name="IrSensorsBus")
    state_bus = Bus(initial_message=0, name="StateBus")
    all_termination_busses = (keyboard_termination_bus, timer_bus)

    # Setup time delays
    keyboard_shutdown_delay = 0.05
    timer_delay=0
    ir_delay = 0.05
    interpreter_delay = 0.1
    line_follow_controller_delay = 0.15

    # Setup timeout for script
    timeout = 20 # seconds

    # Setup consumers, producers, and consumer-producers
    # Setup Timer
    timer_producer = Timer(
        timer_busses = timer_bus,
        duration = timeout,
        delay=timer_delay,
        termination_busses=all_termination_busses,
        name="Timer"
    )
    # Setup keyboard for stop when recieve key input
    keyboard_producer = Producer(
        producer_function = terminal,
        output_busses = keyboard_termination_bus,
        delay = keyboard_shutdown_delay,
        termination_busses = all_termination_busses,
        name = "Keyboard"
    )
    # Setup ir sensor producer
    ir_sensors_producer = Producer(
        producer_function=px.ir_sensors,
        output_busses = ir_sensors_bus,
        delay = ir_delay,
        termination_busses = all_termination_busses,
        name = "IRSensors"
    )
    # Setup Interpreter consumer-producer
    line_interpreter_consumer_producer = ConsumerProducer(
        consumer_producer_function=interpreter,
        input_busses=ir_sensors_bus,
        output_busses=state_bus,
        delay=interpreter_delay,
        termination_busses=all_termination_busses,
        name="LineInterpreter"
    )
    # Line Follow Controller Consumer
    line_follow_controller_consumer = Consumer(
        consumer_function=line_follow_controller,
        input_busses=state_bus,
        delay=line_follow_controller_delay,
        termination_busses=all_termination_busses,
        name="LineFollowController"
    )

    # Run all processes
    runConcurrently([timer_producer, keyboard_producer, ir_sensors_producer, line_interpreter_consumer_producer, line_follow_controller_consumer])

if __name__ == "__main__":
    main()
