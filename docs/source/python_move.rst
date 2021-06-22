Let PiCar-X Move
========================

The basic functions of PiCar-X have been encapsulated in ``picarx.py`` under the path ``/home/pi/picar-x/lib``, chiefly controlling the servo and wheels.

Let PiCar-X move forward, walk in a smart S-shape, and then stop and shake its head. This will allow us to command the method of driving the motor and three servos on the car body.

You can open ``move.py`` in the folder of the ``example`` or directly copy the following code to the Python IDE to run.

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

First, import the libraries to support the basic functionality of PiCar-X. These lines will appear in all the examples that get PiCar-X moving.

.. code-block:: python
    :emphasize-lines: 0

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

    from picarx import Picarx
    import time

Then use the following function with the ``for`` loop to make PiCar-X move.

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``: Make PiCar-X go forward in ``speed``.
* ``set_dir_servo_angle``: Turns the steering servo to ``angle``.
* ``set_camera_servo1_angle``: Turns the Pan servo to ``angle``.
* ``set_camera_servo2_angle``: Turns the Tilt servo to ``angle``.

.. image:: img/pan_tilt_servo.png
    :width: 400