Obstacle Avoidance
=============================

In this project, the PiCar-X will detect obstacles that are directly in front of the built-in ultrasonic module. When the distance of an obstacle is detected to be less than 25cm (10 inches), the PiCar-X will turn to the left, otherwise it will continue to move forward.

**Code**

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

    from picarx import Picarx
    from ultrasonic import Ultrasonic
    from pin import Pin

    if __name__ == "__main__":
        try:
            trig_pin = Pin("D2") 
            echo_pin = Pin("D3")
            sonar = Ultrasonic(trig_pin, echo_pin)
            px = Picarx()
            px.forward(30)
            while True:
                distance = sonar.read()
                print("distance: ",distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        px.set_dir_servo_angle(-35)
                    else:
                        px.set_dir_servo_angle(0)
        finally:
            px.forward(0)


**How it works?**

The distance function is established by importing the ``Ultrasonic`` library.

.. code-block:: python

    from ultrasonic import Ultrasonic

Then the pins on the ultrasonic module are initialized.

.. code-block:: python

    trig_pin = Pin("D2") 
    echo_pin = Pin("D3")
    sonar = Ultrasonic(trig_pin, echo_pin)    

The following code snippet reads the distance value reported by the ultrasonic module, and if the distance is below 25cm (10 inches) it will set the steering servo from 0° (straight) to -35° (turn left).

.. code-block:: python

    while True:
    distance = sonar.read()
    print("distance: ",distance)
    if distance > 0 and distance < 300:
        if distance < 25:
            px.set_dir_servo_angle(-35)
        else:
            px.set_dir_servo_angle(0)
