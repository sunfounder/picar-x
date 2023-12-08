.. _py_avoid:

4. Obstacle Avoidance
=============================

In this project, PiCar-X will detect obstacles in front of it while moving forward, 
and when the obstacles are too close, it will change the direction of moving forward.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
After running the code, PiCar-X will walk forward. 

If it detects that the distance of the obstacle ahead is less than 20cm, it will go backward. 

If there is an obstacle within 20 to 40cm, it will turn left.

If there is no obstacle in the direction after turning left or the obstacle distance is greater than 25cm, 
it will continue to move forward.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time

    POWER = 50
    SafeDistance = 40   # > 40 safe
    DangerDistance = 20 # > 20 && < 40 turn around, 
                        # < 20 backward

    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
        
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(40)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-40)
                    px.backward(POWER)
                    time.sleep(0.5)

        finally:
            px.forward(0)


    if __name__ == "__main__":
        main()



**How it works?**

The ultrasonic module is also imported in the picarx module, 
and we can use some of its encapsulated functions to detect distance.

.. code-block:: python

    from picarx import Picarx

Because the ultrasonic module is imported into the picarx module, 
we can directly use ``px.ultrasonic.read()`` to get the distance.

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

The following code snippet reads the distance value reported by the ultrasonic module, 
and if the distance is below 40cm it will set the steering servo from 0° (straight) to -40° 
(turn left).

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
