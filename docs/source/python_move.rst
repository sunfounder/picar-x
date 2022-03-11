Let PiCar-X Move
========================

This is the first project, let’s test the basic movement of Picar-X.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 move.py

After running the code, PiCar-X will move forward, turn in an S-shape, stop and shake its head. 

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time


    if __name__ == "__main__":
        try:
            px = Picarx()
            px.forward(30)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            px.forward(0)
            time.sleep(1)

            for angle in range(0,35):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
                
        finally:
            px.forward(0)

**How it works?**

The basic functionality of Parker is in the ``picarx`` module,
Can be used to control steering gear and wheels,
and will make the PiCar-X move forward, turn in an S-shape, or shake its head. 

Now, the libraries to support the basic functionality of PiCar-X are imported. These lines will appear in all the examples that involve PiCar-X movement.

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

The following function with the ``for`` loop is then used to make PiCar-X move forward, change directions, and move the camera's pan/tilt.

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``: Orders the PiCar-X go forward at a given ``speed``.
* ``set_dir_servo_angle``: Turns the Steering servo to a specific ``angle``.
* ``set_camera_servo1_angle``: Turns the Pan servo to a specific ``angle``.
* ``set_camera_servo2_angle``: Turns the Tilt servo to a specific ``angle``.

.. image:: img/pan_tilt_servo.png
    :width: 400