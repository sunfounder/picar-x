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

    from picarx import Picarx


    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
            px.forward(30)
            while True:
                distance = px.ultrasonic.read()
                print("distance: ",distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        px.set_dir_servo_angle(-35)
                    else:
                        px.set_dir_servo_angle(0)
        finally:
            px.forward(0)


    if __name__ == "__main__":
        main()


**How it works?**

The ultrasonic module is also imported in the picarx module, and we can use some of its encapsulated functions to detect distance.

.. code-block:: python

    from picarx import Picarx

Because the ultrasonic module is imported into the picarx module, we can directly use ``px.ultrasonic.read()`` to get the distance.

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

The following code snippet reads the distance value reported by the ultrasonic module, and if the distance is below 25cm (10 inches) it will set the steering servo from 0° (straight) to -35° (turn left).

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
