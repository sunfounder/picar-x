Obstacle Avoidance
=============================

In this project, PiCar-X will detect obstacles in front of it while moving forward, and when the obstacles are too close, it will change the direction of moving forward.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 avoiding_obstacles.py
    
After running the code, PiCar-X will walk forward. 

If it detects that the distance of the obstacle ahead is less than 25cm, it will turn left. 

If there is no obstacle in the direction after turning left or the obstacle distance is greater than 25cm, it will continue to move forward.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

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
