Obstacle Avoidance
=============================

In this project, PiCar-X will detect obstacles in front of it with an ultrasonic module. When the distance of the detected obstacle is less than 25cm, PiCar-X will turn left, otherwise it will continue to move forward.

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

You can get the distance only by calling the Ultrasonic library.

.. code-block:: python

    from ultrasonic import Ultrasonic

Then initialize the ultrasonic pins.

.. code-block:: python

    trig_pin = Pin("D2") 
    echo_pin = Pin("D3")
    sonar = Ultrasonic(trig_pin, echo_pin)    

Read the distance value of ultrasonic detection, and set the judgment range: below 25cm, set the steering servo to -35° (turn left).

.. code-block:: python

    while True:
    distance = sonar.read()
    print("distance: ",distance)
    if distance > 0 and distance < 300:
        if distance < 25:
            px.set_dir_servo_angle(-35)
        else:
            px.set_dir_servo_angle(0)
