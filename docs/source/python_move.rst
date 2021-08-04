Let PiCar-X Move
========================

The basic functions of PiCar-X are in the ``picarx.py`` program file, 
under the path ``/home/pi/picar-x/lib``. The ``picarx.py`` program is used for controlling the servo and wheels, 
and will make the PiCar-X move forward, turn in an S-shape, and then stop and shake its head. 

The code shows how to control driving the two motors and the three servos on the car body.

Open ``move.py`` in the folder of the ``example`` directory, or copy the code below directly to the Python IDE to run.


**Code**

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

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

First, the libraries to support the basic functionality of PiCar-X are imported. These lines will appear in all the examples that involve PiCar-X movement.

.. code-block:: python
    :emphasize-lines: 0

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

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